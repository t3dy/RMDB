# BLUNDER2: Windows Console Encoding Crashes (cp1252 vs UTF-8)

**Type:** BUG
**Severity:** HIGH
**Status:** RESOLVED
**Sprint discovered:** SPRINT-01
**Related:** TICKET-018

## What Happened

PDF conversion scripts crashed twice during Slice 2 bulk conversion due to Windows console encoding issues:

### Crash 1: Arrow character in print statement
```
UnicodeEncodeError: 'charmap' codec can't encode character '\u2192' in position 4
```
The script used `->` (Unicode right arrow) in a print statement. Windows cp1252 console can't render this character.

### Crash 2: Macron character in filename
```
UnicodeEncodeError: 'charmap' codec can't encode character '\u0101' in position 152
```
A Pico della Mirandola PDF filename contained a macron (a with bar) from a transliterated title. When the script tried to print the filename, cp1252 encoding choked.

## Root Cause

**Windows terminal default encoding is cp1252, not UTF-8.** Python's `print()` uses `sys.stdout` encoding, which inherits from the terminal. Academic filenames with diacritics, macrons, and special characters are common in this corpus (German umlauts, French accents, transliterated names).

## Impact

- First crash: lost partial conversion progress (had to reconvert 1 file)
- Second crash: mid-way through 321 PDFs, ~250 already converted. Had to resume from where it stopped. Some files in the Pico folder were left in an intermediate state.
- Manifest tracking was incomplete because crashed runs didn't write final manifest entries

## Fix Applied

1. Replaced Unicode arrow `->` with ASCII `->` in all print statements
2. Added UTF-8 stdout/stderr wrapper to all conversion scripts:
```python
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
```

## Secondary Issue: Manifest Tracking Gap

The idempotent skip logic (`if md_path.exists() and newer: SKIP`) didn't write manifest entries for cached files. This meant that after a crash-and-resume, the manifest only contained files converted in the latest run, not the full corpus. Fixed by having the skip logic still register a manifest entry.

## How To Avoid Next Time

1. **Always set UTF-8 encoding on stdout/stderr in scripts that process filenames.** This is a Windows-specific issue that should be a standard boilerplate pattern for this project.
2. **Never use non-ASCII characters in print statements.** Stick to ASCII for logging.
3. **Test conversion on a folder with known encoding-problematic filenames early** (Pico folder has several).
4. **Manifest should always reflect the full state of md/**, not just the latest run.

## Lessons for Project Infrastructure

Add to CLAUDE.md or a script template: all Python scripts in this project MUST include the UTF-8 stdout wrapper because the corpus contains filenames with diacritics across multiple European languages.
