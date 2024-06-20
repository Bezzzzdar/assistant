import geocoder
import geopy
import geopy.geocoders

class Owner:
    def __init__(self, name: str, language: str) -> None:
        Owner.name = name
        Owner.language = language

        self.geo = geocoder.ip('me')
        self.geo = self.geo.latlng
        geolocator = geopy.geocoders.Nominatim()
        Owner.location = geolocator.reverse(str(self.geo[0]) + ', ' + str(self.geo[1]))

    def change_owner_name(self, new_owner_name: str):
        Owner.name = new_owner_name

    def change_owner_language(self, new_owner_language: str):
        Owner.language = new_owner_language
    