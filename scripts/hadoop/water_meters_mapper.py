#!/usr/local/bin/python
import math
import sys

import requests

FACILITYID, HOUSE_NO, STREET_NO, ACCOUNT_NO, FOLIO, STATUS, GPS, IMAGE, LOTLINK, LATITUDE, LONGITUDE = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

DOWNLOAD_URL = 'https://gisservices.surrey.ca/arcgis/rest/services/Public/Water/MapServer/find?searchText=DISPLACEMENT&contains=true&searchFields=TYPE_A&sr=&layers=1&returnGeometry=true&returnZ=false&returnM=falsereturnUnformattedValues=true&returnFieldName=true&f=pjson'

def get_reading():
    readings = {}
    resp = requests.get(DOWNLOAD_URL)
    if resp.status_code != 200:
        raise RuntimeError('GET {} {}'.format(DOWNLOAD_URL, resp.status_code))
    for result in resp.json()['results']:
        a = result['attributes']
        readings[a['FACILITYID']] = [a['LAST_READING_A'], a['LAST_READING_DATE_A']]
    return readings

readings_dic = get_reading()

def map_line(line_fields):
    readings = readings_dic[line_fields[FACILITYID]]
    if readings is None:
        return None
    mapped = ["-".join([line_fields[FACILITYID], readings[1]])]
    mapped.extend(line_fields[FACILITYID:FOLIO])
    mapped.extend(readings)
    mapped.extend(line_fields[LATITUDE:])
    return ','.join(mapped)


# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    if line.startswith('FACILITYID'):
        continue
    # split the line into words
    fields = line.split(",")
    if fields[STATUS] != 'In Service':
        continue
    # increase counters
    try:
        new_line = map_line(fields)
        if map_line != None:
            print(new_line)
    except:
        continue
