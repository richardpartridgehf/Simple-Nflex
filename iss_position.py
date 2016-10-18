import requests
import json
import datetime

def get(event, context):
    url = "http://api.open-notify.org/iss-now.json"
    limit = 2
    count = 0

    r = requests.get(url)
    data = r.json()
  
    lon = data['iss_position']['longitude']
    lat = data['iss_position']['latitude']
    timestamp = data['timestamp']
    country = 'Perhaps the Ocean'
    
    currenttime = datetime.datetime.fromtimestamp(
        int(timestamp)
    ).strftime('%Y-%m-%d %H:%M:%S')
    
    placeurl = "http://maps.googleapis.com/maps/api/geocode/json?latlng=" + str(lat) + "," + str (lon) + "&sensor=true"

    r2 = requests.get(placeurl)
    pldata = r2.json()
    
    if pldata['status']=='OK':
        place = pldata['results'][0]
        country = place['formatted_address']

    return {
        'version': 0.1,
        'type': 'table',
        'optionalContent': {
            'text': 'ISS Position'
        },
        'columns': [
            {
                'text': 'Time'
            },
            {
                'text': 'Long'
            },
            {
                'text': 'Lat'
            },
            {
                'text': 'Place'
            }
        ],
        'rows': [
        {
           "data": [
	         	{
	                'text': currenttime
	            },
	            {
	                'text': lat
	            },
	            {
	                'text': lon
	            },
	            {
	            	'text': country
	            }
        	]
        }
        ]
    }