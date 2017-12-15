#!/usr/bin/env python

import os
from ExternalResource import ExternalResource

SERVICE_SERVER = 'maps.googleapis.com'

class GoogleGeocodingService(ExternalResource):

	def __init__(self):
		return None

	def get_lat_lng(self, addressString):
		endpoint = "{0}/maps/api/geocode/json".format(SERVICE_SERVER)
		API_KEY = os.environ.get('GOOGLE_API_KEY')
		params = {
			"key": API_KEY,
			"address": addressString
		}

		(response, errors) = self.make_request(endpoint, params=params)

		if errors == None:
			latLngData = {
				"source": "Google Maps"
			}
			if len(response['results']) > 0 :
				firstResult = response['results'][0]
				firstResultLocation = firstResult['geometry']['location']
				latLngData['lat'] = firstResultLocation['lat']
				latLngData['lng'] = firstResultLocation['lng']
			else:
				latLngData = {
					"message": "No results found",
					"lat": None,
					"lng": None
				}
			return (latLngData, None)
		else:
			return (response, errors) 



