import phonenumbers 
from phonenumbers import geocoder
from phonenumbers import timezone
from phonenumbers import carrier
import folium
from opencage.geocoder import OpenCageGeocode


key = '4ff5751ee1ce441295efa6990498850f'

numero = phonenumbers.parse('+34675332112')

zona = timezone.time_zones_for_number(numero)

geo = geocoder.description_for_number(numero, 'en')

carrier = carrier.name_for_number(numero, 'en')



geocoder = OpenCageGeocode(key)



query = str(geo)

results = geocoder.geocode(query)

lat = results[0]['geometry']['lat']

lng = results[0]['geometry']['lng']

myMap = folium.Map(location=[lat, lng], zoom_start = 9)

folium.Marker([lat, lng],popup= geo).add_to((myMap))
myMap.save("myLocation.html")


print(numero, zona, geo, carrier, lat, lng)
