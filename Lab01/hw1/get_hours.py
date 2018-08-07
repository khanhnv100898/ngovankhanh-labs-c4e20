# import time
# strings = time.strftime("%Y,%m,%d,%H,%M,%S")
# t = strings.split(',')
# numbers = [ int(x) for x in t ]
# print (numbers)

# import datetime
# datetime.datetime.now()
# print(datetime.datetime.now())
import datetime
# print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

# print(datetime.datetime.now().strftime('%H'))

time_send = datetime.datetime.now().strftime('%H')
print(time_send)