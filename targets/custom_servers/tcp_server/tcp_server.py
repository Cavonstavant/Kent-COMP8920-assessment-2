import socketserver
import sys

class ExampleTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        if b'secret' in self.data:
            self.request.sendall(b"TCP secret: 5678!\n")
        else:
            self.request.sendall(b"Basic TCP server\n")

if __name__ == "__main__":
    HOST, PORT = sys.argv[1] or "0.0.0.0", int(sys.argv[2]) or 9999
    with socketserver.TCPServer((HOST, PORT), ExampleTCPHandler) as server:
        server.allow_reuse_address = True
        server.serve_forever()