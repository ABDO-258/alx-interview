#!/usr/bin/python3
""" reads stdin line by line and computes metrics"""

import sys
import re


line_Num = 0
regex = r"^\d+\.\d+\.\d+\.\d+ .+ \"GET \/projects\/260 HTTP\/1.1\" \d+ \d+$"
total_size = 0

stat_dict = {"200": 0, "301": 0, "400": 0, "401": 0,
             "403": 0, "404": 0, "405": 0, "500": 0}


def printStats():
    """function to print stats """
    print("File size: {}".format(total_size))
    for key, value in stat_dict.items():
        if value > 0:
            print("{}: {}".format(key, value))


def get_filesize(xline):
    """get the file size from the line """
    line_list = xline.split(" ")
    return int(line_list[-1])


def get_status(xline):
    """get the status from the line """
    line_list = xline.split(" ")
    if (line_list[-2]) in stat_dict:
        stat_dict[line_list[-2]] += 1
    return int(line_list[-2])


try:
    for line in sys.stdin:
        line_Num += 1
        if re.search(regex, line):
            total_size += get_filesize(line)
            status = get_status(line)

        if line_Num % 10 == 0:
            printStats()
    printStats()

except KeyboardInterrupt:
    printStats()
    raise
