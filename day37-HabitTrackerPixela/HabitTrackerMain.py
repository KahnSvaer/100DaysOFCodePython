import requests
import datetime as dt
import os

USERNAME = "kahnsvaer"
TOKEN = os.environ.get("Pixela_Token")
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

user_params2 = {
    "id": GRAPH_ID,
    "name": "Productivity Graph",
    "unit": "Hours",
    "type": "float",
    "color": "ajisai",
    "timezone": "Asia/Kolkata"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
# response = requests.post(url=graph_endpoint, json=user_params2, headers=headers)
# print(response.text)

# user_params3 = {
#     "date": (dt.datetime.now().date()-dt.timedelta(0)).strftime("%Y%m%d"),
#     "quantity": "15"
# }
#
# graph_posting_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
# response = requests.post(url=graph_posting_endpoint, headers=headers, json=user_params3)
# print(response.text)


# user_param4 = {
#     "quantity": "1"
# }
#
# graph_updating_endpoint = f"{graph_endpoint}/{GRAPH_ID}/{dt.datetime.now().strftime("%Y%m%d")}"
# response = requests.put(url=graph_updating_endpoint, headers=headers, json=user_param4)
# print(response.text)
#
# response = requests.delete(url=graph_updating_endpoint,headers=headers)
# print(response.text)
