import urllib.request, urllib.parse, urllib.error
import json

serviceurl = "http://maps.googleapis.com/maps/api/geocode/json?"

while True:
    address = input("Enter location: ")
    if len(address) < 1:    # if there is no text entered
        break               # end the program

    # takes the key and the value and does the "+" and "comma" and turns it into a url
    url = serviceurl + urllib.parse.urlencode(
        {"address": address}) 

    # pass the url here
    print("Retrieving", url)
    uh = urllib.request.urlopen(url) # open
    data = uh.read().decode()        # decode it
    print("Retrieved", len(data), "characters")

    try:
        js = json.loads(data)        # parse it with json
    except:
        js = None
    
    # all this is if it blows up
    if not js or "status" not in js or js["status"] != 'OK':
        print("=== Failure to Retrieve ===")
        print(data)
        continue
    
    # these are keys within keys; dict within dict
    # goes to results, 0 is for the first key(which is geometry)
    # inside the geometry is location
    # from there we grab lat (latitude)
    lat = js["results"][0]["geometry"]["location"]["lat"]
    # from there we grab lng (longitude)
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print("lat", lat, "lng", lng)
    location = js["results"][0]["formatted_address"]
    print(location)