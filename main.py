#!/usr/bin/env python
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from RequestHandler import RequestHandler


def main():
	"""Main function 
	Set up the HTTP Server and listen for requests
	"""
	server_ip = '127.0.0.1'
	server_port = 8000
	server_address = (server_ip, server_port)
	httpd = HTTPServer(server_address, RequestHandler)
	print("Running HTTP Server on {0} on port {1}...\nPress Ctrl+C to exit".format(server_ip, server_port))
	httpd.serve_forever()


if __name__ == '__main__':
	main()
