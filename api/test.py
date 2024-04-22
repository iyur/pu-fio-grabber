import json
from datetime import datetime
from http.server import BaseHTTPRequestHandler

def test():
    data = {
        "test": True
    }
    with open("\\data\\" + datetime.now().strftime("%m-%d") + ".json", "w") as file:
        json.dump(data, file)


class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        test()
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('Just a test'.encode('utf-8'))
        return
