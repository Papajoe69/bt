#!/usr/bin/python

import json

import kraken


	
def main():
	print 'bt'
	
	k = kraken.Kraken()
	j = k.getTime()
	print j

	j = k.getAssets()
	print j
	
	k.close()
	
 
if __name__ == "__main__":
	main()