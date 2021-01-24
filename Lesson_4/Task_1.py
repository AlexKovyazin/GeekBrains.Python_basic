from sys import argv

file_name, hours, rate_per_hour, premium = argv
try:
    print(int(hours) * int(rate_per_hour) + int(premium))
except ValueError:
    print('Value Error')
