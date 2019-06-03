import requests
import re #regular expression

username = 'natas1'
password = 'gtVrDuiDfck831PqWsLEZy5gyDz1clto'

url = 'http://%s.natas.labs.overthewire.org' % username

# auth = (user,pass) HTTP Basic Auth

reponse = requests.get(url, auth = (username, password))

content = reponse.text

#print(content)

print(re.findall('<!--The password for natas2 is (.*) -->', content)[0])
