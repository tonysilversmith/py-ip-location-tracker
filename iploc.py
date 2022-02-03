#Copyright tonysilversmith, all right reserved.

import requests, json
import os
import json
fields = '?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query'
API = 'https://www.ip-api.com/json/'
def __main__():
	try:
		print('Hey tony here!')
		print("lets get into it")
		ip_address = input('Enter victim\'s ip :')
		getData = requests.get(API+ip_address+fields).json()
		jsonOutput = json.dumps(getData, indent=2)
		print(jsonOutput)
	except (requests.exceptions.ConnectionError) as e:
        	print (red+"[~]"+" check your internet connection!"+clear)
if __name__ == '__main__':
	__main__()
