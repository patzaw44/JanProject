import json

import requests
url = 'https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/honda?format=json'
response = requests.get(url)
data = response.json()
print(data)

# with open(url, "w", encoding="utf-8"):
#     json.dump(data)

