import csv
import json
from ip_reverse_scanner import get_data_from_ip

ips = []
weights = []
with open('log-data/mock_ip_addresses.csv', newline='') as csvfile:
    ip_addr_with_name_reader = csv.reader(csvfile)
    next(ip_addr_with_name_reader, None)
    ip_to_data = {}
    for row in ip_addr_with_name_reader:
        ip = row[0]
        ip_to_data[ip] = get_data_from_ip(ip)


with open('ip_to_data.json', 'w') as fp:
    json.dump(ip_to_data, fp)
