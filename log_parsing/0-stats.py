#!/usr/bin/python3
import sys


"""Script to get stats from a request"""

i = 0
my_dict = {}
status_available = ['200', '301', '400', '401', '403', '404', '405', '500']
total_size = 0


try:
    for line in sys.stdin:
        line_split = line.split()

        try:
            status_code = line_split[7]
        except IndexError:
            pass
        
        try:
            file_size = line_split[8]
            if status_code in status_available:
                if status_code in my_dict:
                    my_dict[status_code].extend([file_size])
                else:
                    my_dict[status_code] = [file_size]
            else:
                break
        except IndexError:
            pass

        total_size += int(file_size)
        i += 1
        if i == 10:
            print('File size: {}'.format(total_size))
            my_dict = sorted(my_dict.items())
            my_dict = dict(my_dict)
            for key in my_dict:
                print('{}: {}'.format(key, len(my_dict[key])))   
            i = 0

    print('File size: {}'.format(total_size))
    my_dict = sorted(my_dict.items())
    my_dict = dict(my_dict)
    for key in my_dict:
        print('{}: {}'.format(key, len(my_dict[key])))
        i = 0

except KeyboardInterrupt:
    print('File size: {}'.format(total_size))
    my_dict = sorted(my_dict.items())
    my_dict = dict(my_dict)
    for key in my_dict:
        print('{}: {}'.format(key, len(my_dict[key])))
    raise
