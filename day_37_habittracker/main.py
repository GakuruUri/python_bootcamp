import requests


USERNAME = "uri"
TOKEN = "*DevOps@!!1209!!"
GRAPH_ID = "graph1"


pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}


# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixed_data = {
    "date": "20240711",
    "quantity": "15.5",
}
response = requests.post(url=pixel_creation_endpoint, json=pixed_data, headers=headers)
print(response.text)

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers, graph_pixel)
# print(response.text)


