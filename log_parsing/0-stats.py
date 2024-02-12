#!/usr/bin/python3
from sys import stdin
"""
comments
"""

i = 0
my_dict = {}
total_size = 0


for line in stdin:
    line_split = line.split()
    status_code = line_split[7]
    file_size = line_split[8]
    if status_code in my_dict:
        my_dict[status_code].extend([file_size])
    else:
        my_dict[status_code] = [file_size]
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

print(f'File size: {total_size}')
my_dict = sorted(my_dict.items())
my_dict = dict(my_dict)
for key in my_dict:
    print(f'{key}: {len(my_dict[key])}')
   
