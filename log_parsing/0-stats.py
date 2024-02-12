#!/usr/bin/python3
from sys import stdin


"""Script to get stats from a request"""

i = 0
my_dict = {}
status_available = ['200', '301', '400', '401', '403', '404', '405', '500']
total_size = 0


for line in stdin:
    line_split = line.split()
    status_code = line_split[7]
    file_size = line_split[8]
    if status_code in status_available:
        if status_code in my_dict:
            my_dict[status_code].extend([file_size])
        else:
            my_dict[status_code] = [file_size]
    else:
        break
    total_size += int(file_size)
    i += 1
    if i == 10:
        print(f'File size: {total_size}')
        my_dict = sorted(my_dict.items())
        my_dict = dict(my_dict)
        for key in my_dict:
            print(f'{key}: {len(my_dict[key])}')
        my_dict = {}
        i = 0

if i != 0:
    print(f'File size: {total_size}')
my_dict = sorted(my_dict.items())
my_dict = dict(my_dict)
for key in my_dict:
    print(f'{key}: {len(my_dict[key])}')
