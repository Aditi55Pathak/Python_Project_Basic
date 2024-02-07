#  42301c39fa3142ffa29c7218d7959322 -ApiKey

import requests

# Set the API endpoint and parameters
api_key = "42301c39fa3142ffa29c7218d7959322"
api_endpoint = "https://newsapi.org/v2/top-headlines"
parameters = {
    "country": "us",  # Retrieve news from the United States
    "category": "business",  # Retrieve business news
}

# Send the GET request to the API
response = requests.get(
    api_endpoint, params=parameters, headers={"Authorization": api_key}
)

# Parse the response
data = response.json()

# Process the response
if response.status_code == 200:  # Successful response
    articles = data["articles"]
    for article in articles:
        title = article["title"]
        source = article["source"]["name"]
        print(f"Title: {title}\nSource: {source}\n")
else:
    print(f"Error: {data['message']}")
