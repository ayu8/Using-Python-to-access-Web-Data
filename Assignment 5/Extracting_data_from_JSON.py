import urllib.request, urllib.parse, urllib.error
import ssl
import json

url = input("Enter location: ")
print("Retrieving", url)

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

data = urllib.request.urlopen(url).read()
print("Retrieved", len(data), "characters")

js = json.loads(data)
cmnts = total = 0

for i in js["comments"]:
	total += i["count"]
	cmnts += 1

print("Count:", cmnts)
print("Sum:", total)
