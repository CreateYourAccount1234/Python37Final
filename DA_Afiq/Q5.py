#use the request lib
import requests
#set the target webpage
url = 'http://172.17.50.43/snow'
r = requests.get(url)
# This will get the full page
print(r.text)

#This will get the status code
print("Status code:")
print("\t *", r.status_code)

#This will get just the headers
h = requests.head(url)
print("Header:")
print("******")
# To print line by line
for x in h.headers:
    print("\t", x, ":", h.headers[x])
    print("*****")
#this will modify the headers user-agent
headers = {'User-Agent': 'mobile'}
# Test it on an external site
url2 = 'http://httpbin.org/headers'
rh = requests.get(url2, headers=headers)
print(rh.text)