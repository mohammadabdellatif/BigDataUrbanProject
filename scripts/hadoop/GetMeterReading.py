import requests

resp = requests.get("""https://gisservices.surrey.ca/arcgis/rest/services/Public/Water/MapServer/find?searchText=1002162276&contains=true&searchFields=FACILITYID&sr=&layers=1&f=pjson""")
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /tasks/ {}'.format(resp.status_code))
for todo_item in resp.json()['results']:
    print('{} {}'.format(todo_item['attributes']['LAST READ'],todo_item['attributes']['LAST READ DATE']))