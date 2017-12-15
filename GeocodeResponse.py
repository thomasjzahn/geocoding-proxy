#!/usr/bin/env python

from RequestResponse import RequestResponse
from HereGeocodingService import HereGeocodingService
from GoogleGeocodingService import GoogleGeocodingService

class GeocodeResponse(RequestResponse):

	SERVICE_PRIMARY = 'Here'
	SERVICE_ALTERNATE = 'Google'

	def __init__(self):
		return None

	def get_lat_lng(self, addressString):
		response = None
		errors = None

		# addressString is required:
		if addressString == None or addressString == '':
			return (None, "Invalid Address provided")

		# Attempt primary geocoding service, fallback to alternate:
		geo_service = self.get_service(self.SERVICE_PRIMARY)
		(response, errors) = geo_service.get_lat_lng(addressString)
		if errors != None:
			geo_service = self.get_service(self.SERVICE_ALTERNATE)
			(response, errors) = geo_service.get_lat_lng(addressString)
		if errors != None:
			return (None, "ERRORS!")
		
		return (response, errors)

	def get_service(self, serviceName):
		if serviceName == 'Here':
			return HereGeocodingService()
		elif serviceName == 'Google':
			return GoogleGeocodingService()
			return None
		else:
			raise NameError('Invalid Geocoding Service name provided')
		
