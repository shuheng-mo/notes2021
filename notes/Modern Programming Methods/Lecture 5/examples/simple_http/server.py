import http.server
import socketserver

PORT = 8000


class Handler(http.server.BaseHTTPRequestHandler):

    def do_POST(self):
        """This function is called when a POST request is received"""

        # Let's print the body of the request
        content_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_len)
        print(post_body)

        self.do_GET()

    def do_GET(self):
        """This function is called when a GET request is received"""

        print(self.path)

        self.protocol_version = 'HTTP/1.1'
        self.send_response(200, 'OK')
        self.send_header('Content-type', 'text/html')
        self.end_headers()
#         self.wfile.write(bytes("<h1> Hello World!</h1>", 'UTF-8'))
        self.wfile.write(bytes("<h1>Your GET request has been completed!</h1>", 'UTF-8'))


with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
