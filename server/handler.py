from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from notification.trigger import sendMessageWA

# Buat kelas handler yang akan menangani permintaan HTTP
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parsing URL untuk mendapatkan path dan query parameter
        parsed_url = urlparse(self.path)
        path = parsed_url.path
        query_params = parse_qs(parsed_url.query)
        
        # Panggil fungsi yang sesuai berdasarkan path
        if path == '/send':
            self.handle_send(query_params)
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'404 Not Found')
    
    def handle_send(self, query_params):
        # Mendapatkan nilai dari query parameter 'id' & 'message'
        id = query_params.get('id', [''])[0]
        message = query_params.get('message', [''])[0]
        
        if not id:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b'Bad Request: Query parameter \'id\' harus diisi.')
        
        if not message:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b'Bad Request: Query parameter \'message\' harus diisi.')
        
        wasend = sendMessageWA(id, message)
        if not wasend:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(b'Server Error: telah terjadi di sisi server silakan cek log.')
            
        print('Pesan berhasil di kirim')
        
        # Set status response
        self.send_response(200)
        
        # Set header response
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        # Tulis body response dengan menyertakan nilai dari query parameter 'name'
        message = 'OK'
        self.wfile.write(message.encode('utf-8'))

# Buat objek server dan tentukan port yang akan digunakan
server = HTTPServer(('', 5055), RequestHandler)