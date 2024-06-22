import geocoder
import geopy
import geopy.geocoders
import os

class Owner:
    def __init__(self, name: str, language: str) -> None:
        Owner.name = name
        Owner.language = language

        # get user location by using ip
        self.geo = geocoder.ip('me')
        self.geo = self.geo.latlng
        geolocator = geopy.geocoders.Nominatim()
        Owner.location = geolocator.reverse(str(self.geo[0]) + ', ' + str(self.geo[1]))

        # get environment variables
        Owner.SpotifyClientID = os.getenv('SpotifyClientID')
        Owner.SpotifyClientSecret = os.getenv('SpotifyClientSecret')
        Owner.SpotifyRedirectUri = os.getenv('SpotifyRedirectUri')

    def change_owner_name(self, new_owner_name: str):
        Owner.name = new_owner_name

    def change_owner_language(self, new_owner_language: str):
        Owner.language = new_owner_language
    