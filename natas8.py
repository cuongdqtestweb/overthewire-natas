import requests
import re #regular expression

username = 'natas8'
password = 'DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe'

url = 'http://%s.natas.labs.overthewire.org' % username

# HTTP POST request data = {'key' : 'value'}

data = {"secret": "oubWYf2kBq", "submit":"submit" }

# auth = (user,pass) HTTP Basic Auth

reponse = requests.post(url, auth = (username, password), data = data)

content = reponse.text

#print(content)

print(re.findall('natas9 is (.*)', content)[0])
