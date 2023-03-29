import urllib3 

http = urllib3.PoolManager()

response = http.request("GET", "https://dummyjson.com/products")
print(response.status) # Prints 200