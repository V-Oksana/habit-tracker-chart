import os
import requests
from datetime import datetime

USERNAME = "oksana-learns-python"
TOKEN = os.environ.get("ACCESS_TOKEN")
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Create a new user (this part only needs to be run once in the beginning of the project)
# response1 = requests.post(url=pixela_endpoint, json=user_params)
# print(response1.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "My Python Learning Graph",
    "unit": "hours",
    "type": "float",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# Create a new graph (this part only needs to be run once in the beginning of the project)
# response2 = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response2.text)
# The graph can be viewed at https://pixe.la/v1/users/oksana-learns-python/graphs/graph1.html)

pixel_value_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# Pick a date
date = datetime(year=2025, month=12, day=13)
# date = datetime.now()
date_formatted = date.strftime("%Y%m%d") # https://www.w3schools.com/python/python_datetime.asp

pixel_value_params = {
    "date": date_formatted,
    "quantity": "2.0",
}

# Uncomment and run one of the 3 options below to Create, Update or Delete a pixel:
# Create a pixel
# response3 = requests.post(url=pixel_value_endpoint, json=pixel_value_params, headers=headers)
# print(response3.text)

# Update a pixel
# update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_formatted}"
# response4 = requests.put(url=update_pixel_endpoint, json=pixel_value_params, headers=headers)
# print(response4.text)

# Delete a pixel
# delete_pixel_url = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_formatted}"
# response5 = requests.delete(url=delete_pixel_url, headers=headers)
# print(response5.text)
