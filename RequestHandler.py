#!/usr/bin/env python

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import json

from GeocodeResponse import GeocodeResponse

class RequestHandler(BaseHTTPRequestHandler):
	""" Defines a basic HTTP Request Handler """
 
	def do_GET(self):
		""" Handle GET Request """
		# Get correct route for request:
		(response_code, response_data) = self.get_response()

		# Send response status code
		self.send_response(response_code)
 
		# Send headers
		self.send_header('Content-type','application/json')
		self.end_headers()
 
		# Send data back to client
		response_body = {
			"status": response_code
		}
		# Send "data" for succesful responses, otherwise send "message":
		if response_code == 200:
			response_body['data'] = response_data
		else:
			response_body['message'] = response_data

		response_body_text = json.dumps(response_body)
		
		# Write content as utf-8 data
		self.wfile.write(bytes(response_body_text, "utf8"))
		return

	def get_response(self):
		""" Return response based on Request route """
		status_code = 200
		response_data = None

		parsed_url = urlparse(self.path)
		request_path = parsed_url.path
		url_params = parse_qs(parsed_url.query)

		if request_path == '/':
			response_data = self.get_all_routes()
		elif request_path == '/geocode':
			#addressString = '425 Market Street, San Francisco, California, USA'
			thisAddress = url_params.get('address', None)
			addressString = None
			if thisAddress != None:
				addressString = thisAddress[0]
			response = GeocodeResponse()
			(response_data, errors) = response.get_lat_lng(addressString)
			if errors != None:
				status_code = 400
				response_data = errors
		else:
			status_code = 404
			response_data = "Unknown resource specified."

		return (status_code, response_data)

	def get_all_routes(self):
		""" Returns an array of all possible routes in this API """
		return [
			{
				"path": "/",
				"methods": ["GET"],
				"description": "Root resource.  Describes all possible routes."
			},{
				"path": "/geocode",
				"methods": ["GET"],
				"description": "Geocode resource.  Returns geo lat & long from client IP address."
			}
		]

