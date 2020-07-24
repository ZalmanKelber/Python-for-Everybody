import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter url: ")
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read().decode()
print(data)
try:
    js = json.loads(data)
except:
    print("Error: couldn't parse JSON data")
    quit()

total = 0

for comment in js["comments"]:
    total += int(comment["count"])

print(total)
