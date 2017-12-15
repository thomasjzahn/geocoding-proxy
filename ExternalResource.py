#!/usr/bin/env python

import requests
from requests.exceptions import ConnectionError, Timeout

class ExternalResource():

	def __init__(self):
		return None

	def make_request(self, url, headers=None, params=None, data=None, expected_status_code=200):
		response_data = None
		errors = None

		if headers == None:
			headers = {
				"Content-Type": "application/json",
				"Accept": "application/json"
			}

		# Make the request:
		try:
			endpoint = "https://{0}".format(url)
			response = requests.get(endpoint, headers=headers, params=params, data=data)
			if response.status_code == expected_status_code:
				response_data = response.json()
			else:
				errors = "Unexpected status code (expected {0}, received {1})".format(expected_status_code, response.status_code)
		except ConnectionError as e:
			errors = "Error making request ({0})".format(e)
		except Timeout as e:
			errors = "Error making request ({0})".format(e)

		return (response_data, errors)
 

