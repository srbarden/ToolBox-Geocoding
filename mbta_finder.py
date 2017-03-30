"""
Geocoding and Web APIs Project Toolbox exercise

Find the MBTA stops closest to a given location.

Full instructions are at:
https://sites.google.com/site/sd15spring/home/project-toolbox/geocoding-and-web-apis
"""

from urllib.request import urlopen
from urllib.parse import urlencode, quote
import json
from pprint import pprint


# Useful URLs (you need to add the appropriate parameters for your requests)
gmaps_base_url = "https://maps.googleapis.com/maps/api/geocode/json"
mbta_base_url = "http://realtime.mbta.com/developer/api/v2/stopsbylocation"
mbta_demo_api_key = "wX9NwuHnZU2ToO7GmGR9uw"


# A little bit of scaffolding if you want to use it

def name_to_url(user_input):
    formatted = quote(user_input)
    url = "'" + gmaps_base_url + "?" + formatted + "'"
    return url


def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urlopen(url)
    response_text = f.read()
    data = json.loads(str(response_text, "utf-8"))

    return data


def lat_long(data):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.

    See https://developers.google.com/maps/documentation/geocoding/
    for Google Maps Geocode API URL formatting requirements.
    """
    lat = data["results"][0]["geometry"]["location"]["lat"]
    lng = data["results"][0]["geometry"]["location"]["lng"]

    return (lat, lng)


def nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.

    See http://realtime.mbta.com/Portal/Home/Documents for URL
    formatting requirements for the 'stopsbylocation' API.
    """
    url = "http://realtime.mbta.com/developer/api/v2/stopsbylocation?api_key=wX9NwuHnZU2ToO7GmGR9uw&lat=42.3466764&lon=-71.0972178&format=json"
    f = urlopen(url)
    response_text = f.read()
    data = json.loads(str(response_text, "utf-8"))

    name = data['stop'][0]['stop_name']
    dist = data['stop'][0]['distance']

    return (name, dist)


def find_stop_near(place_name):
    """
    Given a place name or address, print the nearest MBTA stop and the
    distance from the given place to that stop.
    """
    url = name_to_url(place_name)
    data = get_json(url)
    ll = lat_long(data)
    nearest = nearest_station(ll)
    return nearest


if __name__ == '__main__':
    # url = "https://maps.googleapis.com/maps/api/geocode/json?address=Fenway%20Park"
    # url = name_to_url("Fenway Park")
    # print(url)
    # data = get_json(url)
    # print(lat_long(data))

    print(nearest_station(0, 0))
