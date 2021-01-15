#!/usr/bin/python

import sys


def map_line(line_fields):
    readings = line_fields[4].split('-')
    return ','.join(line_fields[0:3]) + ',' + readings[0] + ',' + readings[1] + ','  + ','.join(
        line_fields[9:11])


# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    fields = line.split(",")
    # increase counters
    new_line = map_line(fields)
    print(new_line)