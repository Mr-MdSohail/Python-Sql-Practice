import requests 
data=requests.get("https://api.open-meteo.com/v1/forecast?latitude=17.38405&longitude=78.45636&current=temperature_2m")
print(data.json())
current = data.json().get("current")
print(current.get('temperature_2m'),"°C",sep="")
print(current.get('temperature_2m'),"C")
