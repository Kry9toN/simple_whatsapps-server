from server.handler import server

if __name__ == '__main__':
    print('Server berjalan di http://localhost:5055')
    # Jalankan server secara terus menerus (dalam loop)
    server.serve_forever()