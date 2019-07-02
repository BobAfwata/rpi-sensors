# use package
import requests
# login details
username = ''
password = ''
# application entry URL
url = 'http://ultrapisensor.caramacs.com/api/sensor_data/'
# create session
s = requests.Session()
# request entry URL to get the session cookie
r = s.get(url)
# debug output
print(r.status_code)
print(r.text)

# now imitate posting the filled in login form
#url = url + 'j_security_check'
#r = s.post(url, data = {'j_username':username, 'j_password':password})
# debug output
print(r.status_code)
# check if got through = what page did we get
print(r.json)
