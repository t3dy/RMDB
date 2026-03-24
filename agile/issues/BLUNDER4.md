# BLUNDER4: Background Agents Can't Run Bash/Python

**Type:** DESIGN_DECISION
**Severity:** HIGH
**Status:** RESOLVED
**Sprint discovered:** SPRINT-01

## What Happened

Launched two background agents to generate document summaries in parallel. Both agents needed to:
1. Read a JSON batch file (Python)
2. Generate summaries from text excerpts (LLM judgment)
3. Insert results into SQLite database (Python)

Both agents hit the same wall: they couldn't run Bash/Python because the user hadn't pre-approved those permissions for background agents. Batch 2 explicitly reported "Could you grant Bash permission so I can proceed?" Batch 1 appears to have written only 6 summaries before stalling.

## Root Cause

**Violated the AtalantaClaudiens SWARMGUIDELINES.md pattern.** That project explicitly documented: "Background agents CANNOT run Bash/Python." The working pattern is:
1. Agents write JSON to `staging/`
2. Main session reads staging + runs pipeline

We had this documented in PKDSKILLSRMDB.md and even in the AtalantaClaudiens exploration, but ignored it when launching the summary agents.

## Impact

- ~2 wasted agent invocations
- Only 6/161 summaries generated (agent 1 managed a few before stalling)
- Time lost waiting for agents that couldn't complete

## How To Avoid Next Time

1. **Do NOT launch background agents that need to write to the database.** The main session must do all DB writes.
2. **For LLM content generation: do it in the main session, not in agents.** The main session IS the LLM.
3. **If parallelism is needed:** have agents write to staging JSON files, then main session ingests them. Or just process sequentially — 161 summaries is not that many.

## Resolution

Generate all summaries directly in the main session using a Python script that prepares context and has the main Claude session produce structured output.
