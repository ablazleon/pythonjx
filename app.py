#!/usr/bin/python

from http.server import BaseHTTPRequestHandler, HTTPServer

PORT_NUMBER = 8080

class MyHandler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type','text/html')
    self.end_headers()
    # Send the html message
    output = 'v1'
    self.wfile.write(output.encode('utf-8'))
    return

  try:
    server = HTTPServer(('', PORT_NUMBER), MyHandler)
    print('Started httpserver on port', PORT_NUMBER)
    server.serve_forever()

  except KeyboardInterrupt:
    server.server_close()
    print('Stopping server')
