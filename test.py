import requests

# Use a valid API endpoint
url = "http://api.open-notify.org/astros.json"

# Send the request
response = requests.get(url)

# Print the status code (200 means success)
print("Status Code:", response.status_code)

# Print the raw response text (unformatted)
print("\nRaw Response:")
print(response.text)

# Print the formatted JSON response
print("\nFormatted Response:")
data = response.json()
print(data)

# Optionally loop through the astronauts
print("\nPeople currently in space:")
for person in data["people"]:
    print(f"- {person['name']} on {person['craft']}")
