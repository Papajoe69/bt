import httplib
import urllib

class Connection:
	
	def __init__(self, uri, timeout = 30):
		self.headers = {
            'User-Agent': 'krakenex/0.0.5 (+https://github.com/veox/python2-krakenex)'
        }
		self.conn = httplib.HTTPSConnection(uri, timeout = timeout)
		
	def close(self):
		self.conn.close()

	def _request(self, url, req = {}, headers = {}):
		data = urllib.urlencode(req)
		headers.update(self.headers)
		self.conn.request("POST", url, data, headers)
		response = self.conn.getresponse()

		return response.read()
