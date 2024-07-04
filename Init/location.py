"""Contains the user's location on start of the app"""
import geocoder

#Format: latitude,longitude
CITY = f"{(location := geocoder.ip('me').latlng)[0]},{location[1]}"