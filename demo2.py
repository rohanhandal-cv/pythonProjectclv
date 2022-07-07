#1. Connecting to a public Web Service using REST APIs and extract data in JSON format
import requests
# step 2 send a get request, get a response object
result = requests.get("https://randomuser.me/api")

# step 3: Get the status code..returns an integer on success
print(result.status_code)

# step 4:get the data

result.text
# step 5: get data in a more readable json format
print(result.json())

