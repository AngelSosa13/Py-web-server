# HTPP SERVER
from http.server import BaseHTTPRequestHandler, HTTPServer, ThreadingHTTPServer
import time

hostName = "localhost"      #Host
serverPort = 4080           #Exposed Port

class PythonServer(BaseHTTPRequestHandler):     #create the handler
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>PYTHON WEB SERVER</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>Hello world.</p>", "utf-8"))
        self.wfile.write(bytes("<p>This is a simple web server with Python and http.server</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), PythonServer)            #Normal Server, passing the to needed args, the server_address and the RequestHandler
    #webServer = ThreadingHTTPServer((hostName, serverPort), PythonServer)  #thread Server, "   "   "   "   "   "   "   "   "   "   "   "   "   "   "   "   "   "
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:       #Stop listening by typing ctrl+c or command+c 
        pass

    webServer.server_close()    #Closing the server once the KeyBoardInterrupt is triggered
    print("Server stopped.")