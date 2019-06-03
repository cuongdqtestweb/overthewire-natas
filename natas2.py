import requests
import re #regular expression

username = 'natas2'
password = 'ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi'

#url = 'http://%s.natas.labs.overthewire.org' % username
#url = 'http://%s.natas.labs.overthewire.org/files/pixel.png' % username
#url = 'http://%s.natas.labs.overthewire.org/files/' % username
url = 'http://%s.natas.labs.overthewire.org/files/users.txt' % username

# auth = (user,pass) HTTP Basic Auth

reponse = requests.get(url, auth = (username, password))

content = reponse.text

#print(content)

print(re.findall('natas3:(.*)', content)[0])
