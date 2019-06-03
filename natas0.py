import requests
import re #regular expression

username = 'natas0'
password = username

url = 'http://%s.natas.labs.overthewire.org' % username

# auth = (user,pass) HTTP Basic Auth

reponse = requests.get(url, auth = (username, password))

content = reponse.text

#print(content)

print(re.findall('<!--The password for natas1 is (.*) -->', content)[0])
