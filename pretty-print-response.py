import requests
import json

url = "{YOUR-MORPHEUS/APPLIANCE-URL-HERE}/api/users"       # replace with your appliance URL i.e. the URL on which you reach Morpheus 

payload = {"user": {
        "roles": [{"id": 1}],
        "receiveNotifications": True,
        "firstName": "Test-User-Pretty-Print",             # edit the user's firstName here
        "username": "test-pretty",                         # edit the user's username here
        "email": "{USER-EMAIL-HERE}",                      # edit the user's email 
        "password": "{NEW-PASSWORD-HERE}"                  # replace with a suitable password for the user 
    }}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Bearer {YOUR-API-TOKEN-HERE}"
}
response = requests.post(url, json=payload, headers=headers, verify=False)
string = response.json()
print(json.dumps(string, indent=2))
