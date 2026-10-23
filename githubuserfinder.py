import requests

username = input("Enter your GitHub username: ")

url = f"https://github.com{username}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print("Username:",data["login"])
    print("followers:",data["followers"])
    print("following:",data["following"])
    print("Repositories:",data["public_repos"])

elif response.status_code == 404:
    print("User not found")
else:
    print(f"something went wrong (Status code: {response.status_code})")
    
