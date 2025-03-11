import sys
import requests
import json

if len(sys.argv) != 2:
    print("Missing command-line argument")
    sys.exit()
elif str(sys.argv[1]).isalpha():
    print("Command-line argument is not a number")
    sys.exit()

try:
    request = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
    # the damn link david malan gave me didnt work so i had to get ai to give me another and it works but its a little different
    # it has a rate limit 💔💔💔💔💔💔💔
    # im just gona say it works 
except requests.RequestException as e:
    print(f"Error: {e}")
    sys.exit()
#print(json.dumps(request.json(), indent=2))

data = request.json()
amount = float(data["bitcoin"]["usd"])
#print(amount)

print(f"${amount * float(sys.argv[1]):,.4f} USD")