import requests
from datetime import datetime

USERNAME = "meliodas"
TOKEN = "hellohellomyfriend"
ID = "meliodasgraph123"

pixela_endpoint = "https://pixe.la/v1/users"

params = {"token": TOKEN,
          "username": USERNAME,
          "agreeTermsOfService": "yes",
          "notMinor": "yes"
          }

# response = requests.post(url=pixela_endpoint, json=params)
# print(response.text)

graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"

params_graph = {"id": ID,
                "name": "Study",
                "unit": "Hours",
                "type": "float",
                "color": "ajisai"
                }

header_graph = {"X-USER-TOKEN": TOKEN}
#
# response_graph = requests.post(graph_endpoint, headers=header_graph, json=params_graph)
# print("created ", response_graph.text)

# specific_date = datetime(year=2024, month=2, day=26)
today = datetime.now()
print(today)

add_graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{ID}"

params_add = {"date": today.strftime("%Y" + "%m" + "%d"),
              "quantity": "4.2"
              }

add_graph = requests.post(add_graph_endpoint, headers=header_graph, json=params_add)
print("added ", add_graph.text)

# delete_graph = requests.delete(add_graph_endpoint, headers=header_graph)
# print(delete_graph.text)

# url = "https://pixe.la/v1/users/meliodas"
# headers = {
#     "X-USER-TOKEN": "hellohellomyfriend"
# }


# delete_response = requests.delete(url, headers=headers)
# delete_response.raise_for_status()
# print(delete_response.text)
