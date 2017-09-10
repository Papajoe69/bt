import json

import connection

class Kraken:
	def __init__(self):
		self.apiversion = '0'

		self.api = 'api.kraken.com'
		self.uri = 'https://api.kraken.com'
		self.conn = connection.Connection(self.api)
		
	def close(self):
		self.conn.close()

	def _query(self, urlpath, req = {}, headers = {}):
		"""Low-level query handling.
		
		Arguments:
		urlpath -- API URL path sans host (string, no default)
		req     -- additional API request parameters (default: {})
		conn    -- kraken.Connection object (default: None)
		headers -- HTTPS headers (default: {})
		
		"""
		
		url = self.uri + urlpath

		if self.conn is None:
			self.conn = connection.Connection(self.api)

		ret = self.conn._request(url, req, headers)
		return json.loads(ret)
		
	def _public(self, method):
		urlpath = '/' + self.apiversion + '/public/' + method
		return self._query(urlpath,{})
		
	def getTime(self):
		return self._public('Time')
		
	def getAssets(self):
		return self._public('Assets')