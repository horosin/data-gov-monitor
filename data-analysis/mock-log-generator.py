import csv
import json
import random
from random_date_generator import gen_datetimes
from get_mock_metadata_from_dane_gov import get_mock_data


ips = []
weights = []
with open('log-data/mock_ip_addresses.csv', newline='') as csvfile:
    ip_addr_with_name_reader = csv.reader(csvfile)
    next(ip_addr_with_name_reader, None)
    for row in ip_addr_with_name_reader:
        ips.append(row[0])
        weights.append(random.randint(1, 40))

record_number_to_generate = 10000

ip_random_choices = random.choices(ips, weights, k=record_number_to_generate)
date_random_choices = gen_datetimes(record_number_to_generate, min_year=2016, max_year=2019)

ip_to_data = None
with open('ip_to_data.json', 'r') as f:
    ip_to_data = json.load(f)

mock_data_gov_records_number = 100
data_gov_records = get_mock_data(mock_data_gov_records_number)

with open('log-data/mock_request_data.csv', 'w', newline='') as csvfile:
    logwriter = csv.writer(csvfile)
    data_gov_headers = ['uri', 'title', 'category_name', 'category_id']
    request_headers = ['ip', 'date']
    chosen_fields = ['city', 'country', 'isp', 'lat', 'lon', 'org', 'reverse', 'zip']
    data_gov_headers.extend(request_headers)
    data_gov_headers.extend(chosen_fields)

    logwriter.writerow(data_gov_headers)
    for i in range(record_number_to_generate):
        data_gov_random_record = data_gov_records[random.randint(0, mock_data_gov_records_number-1)]

        chosen_ip = ip_random_choices[i]
        logwriter.writerow([
            data_gov_random_record[0],
            data_gov_random_record[1],
            data_gov_random_record[2],
            data_gov_random_record[3],
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
