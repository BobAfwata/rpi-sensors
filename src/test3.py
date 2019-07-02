from urllib.parse import urlencode
from urllib.request import Request, urlopen

url = 'http://ultrapisensor.caramacs.com/api/sensor_data' # Set destination URL here
post_fields = {'value': 'sensor_id'}     # Set POST fields here

request = Request(url, urlencode(post_fields).encode())
json = urlopen(request).read().decode()
print(json)