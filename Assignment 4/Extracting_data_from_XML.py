import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
import ssl

url = input("Enter location: ")
print("Retrieving", url)

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

data = urllib.request.urlopen(url).read()
print("Retrieved", len(data), "characters")

tree = ET.fromstring(data)
lst = tree.findall("comments/comment")

cmnts = 0
total = 0

for i in lst:
	total += int(i.find("count").text)
	cmnts += 1
print("Count:", cmnts)
print("Sum:", total)
