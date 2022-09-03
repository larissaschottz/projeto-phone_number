import phonenumbers
from phonenumbers import geocoder

telephone = input("Enter phone number: ")

telephone_adjusted = phonenumbers.parse(telephone)
print(telephone_adjusted)

#finding phonelocation
local = geocoder.description_for_number(telephone_adjusted, "en")
print("This number is from: " + local)
