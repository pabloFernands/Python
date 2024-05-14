import requests
from datetime import datetime

USERNAME = "pablauto"
TOKEN = "asht7asdt27948"

pixela_endpoint = "https://pixe.la/v1/users"

pixela_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

#pixela_response = requests.post(url = pixela_endpoint, json=pixela_parameters)
#print(pixela_response.text)

GRAPH_ID = "graph1"

graph_config = {
    "id": GRAPH_ID,
    "name": "Jump rope",
    "unit": "Jumps",
    "type": "int",
    "color": "shibafu",
}

graph_header = {
    "X-USER-TOKEN": "asht7asdt27948"
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

#graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=graph_header)
#print(graph_response.text)

today = datetime.now()
date = today.strftime("%Y%m%d")
ask_quantity = input("O quanto você pulou hoje?")

graph_update = {
    "date": date,
    "quantity": ask_quantity
}

graph_post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
#graph_requests = requests.post(url=graph_post_endpoint, json=graph_update, headers=graph_header)

graph_put = {
    "quantity": ask_quantity
}

graph_put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"
graph_put_requests = requests.put(url=graph_put_endpoint, json=graph_put, headers=graph_header)
print(graph_put_requests.text)

graph_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"
#graph_delete_requests = requests.delete(url=graph_delete_endpoint, headers=graph_header)
#print(graph_delete_requests.text)