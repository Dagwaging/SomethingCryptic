import SimpleHTTPServer
import SocketServer
import cgi

class Handler(SimpleHTTPServer.SimpleHTTPRequestHandler):
	def do_POST(self):
		self.send_response(200)
		request = cgi.FieldStorage(fp = self.rfile, headers=self.headers, environ={'REQUEST_METHOD':'POST', 'CONTENT_TYPE':self.headers['Content-Type'],})
		messageSid = request.getvalue("MessageSid")
		answer(messageSid)

httpd = SocketServer.TCPServer(("", 80), Handler)
httpd.serve_forever()
