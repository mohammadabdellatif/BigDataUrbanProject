#!/usr/bin/python

import sys


def map_line():
    readings = fields[4].split('-')
    return ','.join(fields[0:3]) + ',' + readings[0] + ',' + readings[1] + ',' + fields[5] + ',' + ','.join(
        fields[9:11])


# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    fields = line.split(",")
    # increase counters
    new_line = map_line()
    print(new_line)