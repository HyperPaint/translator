from http.server import HTTPServer, CGIHTTPRequestHandler

# установить прослушивание со всех ip и порт сервера
server_address = ("", 80)
# создать сервер
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
# запустить сервер навсегда
httpd.serve_forever()