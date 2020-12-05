#!/usr/bin/env python3

import sys
from socket import *

# No valid arguments
try:
	if(len(sys.argv) != 2):
		raise Exception()
	tmp = int(sys.argv[1])
	if(type(tmp) != int):
		raise Exception()
except Exception:
	print("Usage: ./Webserver.py {port}")
	exit()

# Extract host and port
server_host = 'localhost'
server_port = int(sys.argv[1])

# Set server's TCP socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((server_host, server_port))
serverSocket.listen(1)

# Display that the server is ready
print("--- The server is ready to receive --- \n")

while True:
	connectionSocket, addr = serverSocket.accept()

	# Get and parse the request; assuming only GET requests
	request = connectionSocket.recv(2048).decode('utf-8')
	print(request)
	request_list = request.split(' ')
	# If the method is not a GET request, then return error message
	method = request_list[0]
	resource = request_list[1]
	if(method != "GET"):
		header = "HTTP/1.1 405 Method Not Allowed\nContent-Type: " + "text/html" + "\n\n"
		message = """<html>\n\t<body>\n\t<h3>Error 405: Method Not Allowed</h3>\n\t</body>\n</html>"""
		response = header + message
		response = request.encode('utf-8')
		connectionSocket.send(response)
		connectionSocket.close()
		continue
	# Parse the requested resource
	if(resource == "/"):
		resource = 'index.html'
	else:
		resource = resource[1:]

	try:
		# Build header for success case
		header = "HTTP/1.1 200 OK\n"
		# Check the type of the resource
		if '.png' in resource.split():
			mimetype = 'image/png'
		else:
			mimetype = 'text/html'
		header += "Content-Type " + mimetype + '\n\n'
		# Read requested resource to memory
		file = open(resource, 'rb')
		message = file.read()
		file.close()
	except Exception:
		# File is not found 
		header = "HTTP/1.1 404 Not Found\nContent-Type: " + "text/html" + "\n\n"
		message = """<html>\n<body>\t\n\t\t\n<h3>Error 404: Not Found</h3>\n\t</body>\n</html>""".encode('utf-8')
	finally:
		response = header.encode('utf-8') + message
		connectionSocket.send(response)
	connectionSocket.close()

# Close the TCP socket
serverSocket.close()