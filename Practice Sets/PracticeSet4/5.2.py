# install and import the requestts module (if available) and use it to fetch data from "https://api.github.com" .
import requests
result = requests.get("https://api.github.com")
print(result)
print(type(result))
print(dir(result))
dir(result)
