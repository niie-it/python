import requests, json

result = requests.get('https://dummyjson.com/products')
pythondict = result.json()

print(json.dumps(pythondict, indent=4))
