import requests
import re #regular expression

username = 'natas11'
password = 'U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK'

url = 'http://%s.natas.labs.overthewire.org' % username

# HTTP POST request data = {'key' : 'value'}

cookies = { "data" : "ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK" }

# auth = (user,pass) HTTP Basic Auth

reponse = requests.get(url, auth = (username, password), cookies = cookies)

content = reponse.text

#print(content)

print(re.findall('\nThe password for natas12 is (.*)<br>', content)[0])
