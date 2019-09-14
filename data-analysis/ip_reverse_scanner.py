import requests
import json

ip_api_url = 'http://ip-api.com/json/'
ip_to_find = '149.156.96.52'
# fields to retrieve = status,message,country,countryCode,region,regionName,city,
# zip,lat,lon,timezone,isp,org,as,reverse,query
custom_fields = '?fields=65535'
response = requests.get(ip_api_url + ip_to_find + custom_fields)
content_dict = json.loads(response.content)

def get_data_from_ip(ip_to_find):
    response = requests.get(ip_api_url + ip_to_find + custom_fields)
    content_dict = json.loads(response.content)
    chosen_fields = ['city', 'country', 'isp', 'lat', 'lon', 'org', 'reverse', 'zip']
    chosen_data = {key:content_dict[key] for key in chosen_fields}
    return(chosen_data)
# print(get_data_from_ip('5.134.213.82'))
