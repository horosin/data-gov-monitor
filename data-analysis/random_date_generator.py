# import random
# import time

# def str_time_prop(start, end, format, prop):
#     """Get a time at a proportion of a range of two formatted times.

#     start and end should be strings specifying times formated in the
#     given format (strftime-style), giving an interval [start, end].
#     prop specifies how a proportion of the interval to be taken after
#     start.  The returned time will be in the specified format.
#     """

#     stime = time.mktime(time.strptime(start, format))
#     etime = time.mktime(time.strptime(end, format))

#     ptime = stime + prop * (etime - stime)

#     return time.strftime(format, time.localtime(ptime))


# def random_date(start, end, prop):
#     return str_time_prop(start, end, '%mm/%dd/%YY %I:%M %p', prop)

# print(random_date("01/01/2017 1:30 PM", "14/9/2019 4:50 PM", random.random()))

import random
from datetime import datetime, timedelta

# min_year=2017
# max_year=datetime.now().year

# start = datetime(min_year, 1, 1, 00, 00, 00)
# years = max_year - min_year+1
# end = start + timedelta(days=365 * years)

# for i in range(10):
#     random_date = start + (end - start) * random.random()
#     print(random_date)

#done

def gen_datetime(min_year=2017, max_year=datetime.now().year):
    # generate a datetime in format yyyy-mm-dd hh:mm:ss.000000
    start = datetime(min_year, 1, 1, 00, 00, 00)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    return start + (end - start) * random.random()

def gen_datetimes(record_number, min_year=2017, max_year=datetime.now().year):
    # generate a datetime in format yyyy-mm-dd hh:mm:ss.000000
    start = datetime(min_year, 1, 1, 00, 00, 00)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    records = []
    for i in range(record_number):
        records.append(start + (end - start) * random.random())
    return records
