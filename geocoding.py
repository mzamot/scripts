import json, requests, sys

def getLatLong(address, api=""):
  url = r"https://maps.googleapis.com/maps/api/geocode/json"
  print address
  try:
    response = requests.get(url, params={ 'address' : address, 'key' : api } )
 
    if response.status_code == 200:
      jsonBody = json.loads(response.text)
    else:
      raise Exception("Received HTTP code: %d" % response.status_code ) 
  except Exception as error:
    print error
    sys.exit(1)

  location = jsonBody['results'][0]['geometry']['location']
  return { 'latitude' : location['lat'], 'longitude' : location['lng'] }


# Execution from command line
# python geocoding.py address
print getLatLong(address=" ".join(sys.argv[1:]) )