#!/usr/bin/env python3
import os
import http.server
import socketserver

port = int(os.getenv('PORT', 8000))
directory = 'website/public'

os.chdir(directory)

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", port), Handler) as httpd:
    print(f"Serving {directory} at http://localhost:{port}/")
    httpd.serve_forever()
