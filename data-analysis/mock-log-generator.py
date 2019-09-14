import csv
import json
import random
from random_date_generator import gen_datetimes


ips = []
weights = []
with open('log-data/mock_ip_addresses.csv', newline='') as csvfile:
    ip_addr_with_name_reader = csv.reader(csvfile)
    next(ip_addr_with_name_reader, None)
    for row in ip_addr_with_name_reader:
        ips.append(row[0])
        weights.append(random.randint(1, 40))

# print(weights)
record_number_to_generate = 100

ip_random_choices = random.choices(ips, weights, k=record_number_to_generate)
date_random_choices = gen_datetimes(record_number_to_generate, min_year=2016, max_year=2019)

ip_to_data = None
with open('ip_to_data.json', 'r') as f:
    ip_to_data = json.load(f)

with open('log-data/mock_request_data.csv', 'w', newline='') as csvfile:
    logwriter = csv.writer(csvfile)
    chosen_fields = ['city', 'country', 'isp', 'lat', 'lon', 'org', 'reverse', 'zip']
    headers = ['ip', 'date']
    headers.extend(chosen_fields)
    logwriter.writerow(headers)
    for i in range(record_number_to_generate):
        chosen_ip = ip_random_choices[i]
        logwriter.writerow([
            chosen_ip,
            date_random_choices[i],
            ip_to_data[chosen_ip][chosen_fields[0]],
            ip_to_data[chosen_ip][chosen_fields[1]],
            ip_to_data[chosen_ip][chosen_fields[2]],
            ip_to_data[chosen_ip][chosen_fields[3]],
            ip_to_data[chosen_ip][chosen_fields[4]],
            ip_to_data[chosen_ip][chosen_fields[5]],
            ip_to_data[chosen_ip][chosen_fields[6]],
            ip_to_data[chosen_ip][chosen_fields[7]],
        ])
    # logwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
