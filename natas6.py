import requests
import re #regular expression

username = 'natas6'
password = 'aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1'

url = 'http://%s.natas.labs.overthewire.org' % username
#url = 'http://%s.natas.labs.overthewire.org/index-source.html' % username
#url = 'http://%s.natas.labs.overthewire.org/includes/secret.inc' % username

# HTTP POST request data = {'key' : 'value'}
data = {"secret": "FOEIUWGHFEEUHOFUOIU", "submit":"submit"}

# auth = (user,pass) HTTP Basic Auth

reponse = requests.post(url, auth = (username, password), data = data)

content = reponse.text

#print(content)

print(re.findall('The password for natas7 is (.*)', content)[0])
