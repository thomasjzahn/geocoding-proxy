#!/usr/bin/env python

import os
from ExternalResource import ExternalResource

SERVICE_SERVER = 'geocoder.cit.api.here.com'

class HereGeocodingService(ExternalResource):

	def __init__(self):
		return None

	def get_lat_lng(self, addressString):
		endpoint = "{0}/6.2/geocode.json".format(SERVICE_SERVER)
		APP_ID = os.environ.get('HERE_APP_ID')
		APP_CODE = os.environ.get('HERE_APP_CODE')
		params = {
			"app_id": APP_ID,
			"app_code": APP_CODE,
			"searchtext": addressString
		}

		(response, errors) = self.make_request(endpoint, params=params)

		if errors == None:
			latLngData = {
				"source": "Here.com"
			}
			if len(response['Response']['View']) > 0 :
				firstView = response['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']
				latLngData['lat'] = firstView['Latitude']
				latLngData['lng'] = firstView['Longitude']
			else:
				latLngData = {
					"message": "No results found",
					"lat": None,
					"lng": None
				}
			return (latLngData, None)
		else:
			return (response, errors) 



