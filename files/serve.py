#!/usr/bin/env python3
"""
Warren Library Document Server
Run this script to open the document in your browser with images loaded.
Usage: python3 serve.py
"""
import http.server
import socketserver
import webbrowser
import os
import threading

PORT = 8765
FILE = "warren_library.html"

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args): pass  # suppress logs

print(f"Opening Warren Library document at http://localhost:{PORT}/{FILE}")
print("Press Ctrl+C to stop.\n")

def open_browser():
    import time; time.sleep(0.5)
    webbrowser.open(f"http://localhost:{PORT}/{FILE}")

threading.Thread(target=open_browser, daemon=True).start()

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nDone.")
