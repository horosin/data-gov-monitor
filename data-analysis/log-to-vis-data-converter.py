import csv


with open('log-data/mock_logs_template.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        print(row[0])

print()
        # print(', '.join(row))
