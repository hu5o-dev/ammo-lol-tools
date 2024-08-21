import requests
import json
import time
import os

url = "https://ammo.lol/api/v1/public/user"
headers = {
    "Content-Type": "application/json",
    "API-Key": "2ffb1a72d594ecf09d0972e1ff7602af1e5c6b00"
}

uid = 1

if not os.path.exists('users'):
    os.makedirs('users')

while True:
    params = {
        "uid": uid
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        user_info = response.json()
        filename = f'users/user_info_{uid}.json'

        with open(filename, 'w') as file:
            json.dump(user_info, file, indent=4)

        print(f"User information for UID {uid} saved to '{filename}'.")
        uid += 1
        time.sleep(1)
    else:
        print(f"Failed to retrieve user info for UID {uid}. Status code: {response.status_code}")
        break
