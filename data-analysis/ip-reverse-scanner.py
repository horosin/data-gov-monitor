import requests
import json

ip_api_url = 'http://ip-api.com/json/'
ip_to_find = '149.156.96.52'
# fields=status,message,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,reverse,quer
custom_fields = '?fields=65535'

response = requests.get(ip_api_url + ip_to_find + custom_fields)
content_dict = json.loads(response.content)
print(content_dict)
