import urllib.request, urllib.parse, urllib.error
import json
import ssl

# api_key = False   #Keyless access to Google Maps Platform is deprecated
api_key = input("Enter your API: ")
# You need to enter your Google Places API key here
# https://developers.google.com/maps/documentation/geocoding/intro

serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input("Enter address location: ")
    if address == "done": break
    if len(address) < 1: break

    parms = dict()
    parms["address"] = address
    if api_key is not False:
        parms["api_key"] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)    #use rules to parse string into HTTP request URL

    print("Retrieving", url)
    uh = urllib.request.urlopen(url, context = ctx)     #remember we get a handle back
    data = uh.read().decode()                           #let's pull all the document from that page in one string
    print("Retrieved", len(data), "characters")

    try:
        js = json.loads(data)                           #deserialize the data
    except:
        js = None

    if not js or 'status' not in js or js["status"] != "OK":
        print("==== Failure To Retrieve ====")
        print(data)
        continue

    print(json.dumps(js, indent = 4))                 #serialize back to json (opposite of .loads())

    lat = js["result"][0]["geometry"]["location"]["lat"]
    long = js["result"][0]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)
