from http.server import HTTPServer, BaseHTTPRequestHandler
import time

class BestzHTTP(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        with open("index.html", "r") as file:
            content = file.read()
            self.wfile.write(bytes(content, "utf-8"))

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        self.wfile.write(bytes('{"time": "' + date + '"}', "utf-8"))

if __name__=='__main__':
    HOST = "localhost"
    PORT = 9999

    server = HTTPServer((HOST, PORT), BestzHTTP)
    print(f"Server running.. http://{HOST}:{PORT}")
    server.serve_forever()
    server.server_close()
    print("Server Stopped....")
