import googlemaps
from datetime import datetime

# Replace 'YOUR_API_KEY' with your actual Google Maps API key
gmaps = googlemaps.Client(key='AIzaSyB2XoyuzNvz2YeE3FIo4O3PUbO3v8XAEWI')

# Set the city you want to scrape
city = 'New York'

# Search for places in the specified city
places_result = gmaps.places(query='Abha resturants', location=city)

# Iterate over the results and extract information about each place
for place in places_result['results']:
    # Extract the name of the place
    name = place['name']

    # Extract the address of the place
    address = place['formatted_address']

    # Extract the latitude and longitude of the place
    lat = place['geometry']['location']['lat']
    lng = place['geometry']['location']['lng']

    # Extract the rating of the place (if available)
    if 'rating' in place:
        rating = place['rating']
    else:
        rating = None

    # Extract the types of the place
    types = place['types']

    # Print the extracted information for each place
    print(f'Name: {name}\nAddress: {address}\nLatitude: {lat}\nLongitude: {lng}\nRating: {rating}\nTypes: {types}\n')
