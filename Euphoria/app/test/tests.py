# import requests
# import json

# url = "http://127.0.0.1:8000/Test/cov_name/"

# payload=json.dumps({
#     'name': 'ashutosha',
#     'number': 92392323232323,
#     'alert': 0,
#     'cov_data': []
 
# })
# files=[
#   ('name_image',('1e8c7460a52e3995e6f93ac38a46e41f.jpg',open('C://Users/Ashutosh Anand/Downloads/1e8c7460a52e3995e6f93ac38a46e41f.jpg','rb'),'image/jpeg'))
# ]
# headers = { 'Content-Type': 'application/json'}

# response = requests.request("POST", url, headers=headers, data=payload, files=files)

# print(response.text)

import requests
import json

url = "http://127.0.0.1:8000/Test/cov_name/"

payload = json.dumps({
  "name": "pranjali",
  "number": 8521571769963,
 
  "alert": 0,
  "cov_data": []
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
