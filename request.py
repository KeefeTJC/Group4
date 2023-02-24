# Use the Request library
import requests

# Set the target webpage
url = 'http://172.18.58.80/varsity'
webpage = requests.get(url)
# This will get the full webpage in text
print(webpage.text)
# Get and print the status code
print("Status code:")
print("\t *", webpage.status_code)
# Get the headers
h = requests.head(url)
print("Header:")
print("**********")
# To print line by line
for x in h.headers:
    print("\t ", x, ":", h.headers[x])
    print("**********")

# Modify the headers user-agent
headers = {'User-Agent': 'Mobile'}

# Test it on an external site
url2 = 'http://httpbin.org/headers'
request_header = requests.get(url2, headers=headers)
print(request_header.text)
