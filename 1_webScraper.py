import requests
from bs4 import BeautifulSoup
import json

url = "https://food.grab.com/sg/en/restaurants"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
}

# Create a session
session = requests.Session()

# Make the request using the session
response = session.get(url, headers=headers)

# Check status code and proceed with parsing if successful
if response.status_code == 200:
    # Parse the content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the script tag with id="__NEXT_DATA__"
    script_tag = soup.find('script', id='__NEXT_DATA__')

    if script_tag:
        # Extract the content within the script tag
        script_content = script_tag.string.strip()

        # Save the content to a JSON file
        with open('resultJson.json', 'w', encoding='utf-8') as json_file:
            json_file.write(script_content)

        print("Data saved to resultJson.json")
    else:
        print("Error: Script tag with id='__NEXT_DATA__' not found.")
else:
    print(f"Error: Unable to fetch content. Status code: {response.status_code}")
