#!/usr/local/bin/python
import sys
import requests
import uuid

READING_URL = 'https://gisservices.surrey.ca/arcgis/rest/services/Public/Water/MapServer/find?searchText={id}&contains=true&searchFields=FACILITYID&sr=&layers=1&f=pjson'

FACILITYID, HOUSE_NO, STREET_NO, ACCOUNT_NO, FOLIO, STATUS, GPS, IMAGE, LOTLINK, LATITUDE, LONGITUDE = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10


def get_reading(facility_id):
    url = READING_URL.format(id=facility_id)
    resp = requests.get(url)
    if resp.status_code != 200:
        raise RuntimeError('GET {} {}'.format(url, resp.status_code))
    meter_attributes = resp.json()['results'][0]['attributes']
    return [meter_attributes['LAST READ'], meter_attributes['LAST READ DATE']]


def map_line(line_fields):
    readings = get_reading(line_fields[FACILITYID])
    mapped = [str(uuid.uuid1())]
    mapped.extend(line_fields[FACILITYID:FOLIO])
    mapped.extend(readings)
    mapped.extend(line_fields[LATITUDE:])
    return ','.join(mapped)


# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    fields = line.split(",")
    # increase counters
    new_line = map_line(fields)
    print(new_line)
