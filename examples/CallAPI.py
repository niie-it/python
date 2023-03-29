import json, requests

url = 'http://dummyjson.com/products'

result = requests.get(url)
pythondict = result.json()
print(json.dumps(pythondict, indent=4))
print(list(pythondict.keys()))

