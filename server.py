import os, sys, socketserver

os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import http.server

PORT = int(os.environ.get('PORT', 3457))
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(('', PORT), Handler) as httpd:
    print(f'Serving on port {PORT}', flush=True)
    httpd.serve_forever()
