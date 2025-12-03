#"http://api.openweathermap.org/geo/1.0/direct?q=Tehran&appid=13d798c7224407de20e5d1090b475085"
# #https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid=13d798c7224407de20e5d1090b475085
import requests
city = input("Enter a city name: ")
request = (f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid=13d798c7224407de20e5d1090b475085")
response = requests.get(request).json()
for a in response:
   lat = (a["lat"])
   lon = (a["lon"])

ap = "13d798c7224407de20e5d1090b475085"
request = (f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={ap}")
response2 = requests.get(request).json()

print(response2["weather"][0]["description"])
temp = (response2["main"]["temp"] - 273.15)
print(f"The temperature is {temp} celsius")