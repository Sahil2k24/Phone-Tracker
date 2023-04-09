#pip install phonenumbers

import phonenumbers
from test import number

#geopy is a python library. geopy makes it easy for Python
# developers to locate the coordinates of addresses, cities, countries, and landmarks across the globe
# using third-party geocoders and other data sources.


from phonenumbers import geocoder
country_no = phonenumbers.parse(number, "CH")
print("The country to which the number belongs : ")
print(geocoder.description_for_number(country_no, "en"))


from phonenumbers import carrier
service_provider=phonenumbers.parse(number, "RO")
print("The Service Provider of the particular number is : ")
print(carrier.name_for_number(service_provider, "en"))
