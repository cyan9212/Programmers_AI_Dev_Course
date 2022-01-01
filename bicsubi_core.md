![](Aspose.Words.83e78e49-5834-420f-a5b6-65bd840c7008.001.png)

Public 

`	`Documentation Settings![](Aspose.Words.83e78e49-5834-420f-a5b6-65bd840c7008.001.png)

Environment

No Environment

Layout

Double Column

Language

Python - Requests
# **bicsubi\_core**
- [Introduction ](https://documenter.getpostman.com/view/7440345/UVRHi3gs#intro)

GET[](https://documenter.getpostman.com/view/7440345/UVRHi3gs#8354ac61-c1d1-41d6-864a-009931e69f62 "whoami")

[whoami](https://documenter.getpostman.com/view/7440345/UVRHi3gs#8354ac61-c1d1-41d6-864a-009931e69f62 "whoami")

GET[](https://documenter.getpostman.com/view/7440345/UVRHi3gs#aee13486-61a6-47c2-a815-51c9d24d46de "echo?string=")

[echo?string="string"](https://documenter.getpostman.com/view/7440345/UVRHi3gs#aee13486-61a6-47c2-a815-51c9d24d46de "echo?string=")

GET[](https://documenter.getpostman.com/view/7440345/UVRHi3gs#44654948-5fc5-4c08-96c0-320c4ce16f1f "weapon")

[weapon](https://documenter.getpostman.com/view/7440345/UVRHi3gs#44654948-5fc5-4c08-96c0-320c4ce16f1f "weapon")

POST[](https://documenter.getpostman.com/view/7440345/UVRHi3gs#2201596b-1ea3-4a0a-976b-73958e8d0e95 "weapon")

[weapon](https://documenter.getpostman.com/view/7440345/UVRHi3gs#2201596b-1ea3-4a0a-976b-73958e8d0e95 "weapon")

DEL[](https://documenter.getpostman.com/view/7440345/UVRHi3gs#8261ccae-5798-4b19-86d9-92bb68d2ccf6 "weapon/id")

[weapon/id](https://documenter.getpostman.com/view/7440345/UVRHi3gs#8261ccae-5798-4b19-86d9-92bb68d2ccf6 "weapon/id")

PUT[](https://documenter.getpostman.com/view/7440345/UVRHi3gs#6a7c765f-1c78-434e-81a1-1569a21f415f "weapon/id")

[weapon/id](https://documenter.getpostman.com/view/7440345/UVRHi3gs#6a7c765f-1c78-434e-81a1-1569a21f415f "weapon/id")

bicsubi\_core

GET

whoami

http://127.0.0.1:5000/whoami




Example Request

whoami

View More

import requests

url = "http://127.0.0.1:5000/whoami"

payload={}

headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

![](Aspose.Words.83e78e49-5834-420f-a5b6-65bd840c7008.001.png)

Example Response

200 OK

Body 

Header(4)

{

`  `"name": "cyan9212"

}

GET

echo?string="string"

No request URL found. It will show up here once added.




Example Request

echo?string="string"

View More

import requests

url = "http://127.0.0.1:5000/echo?string=apple"

payload={}

headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

![](Aspose.Words.83e78e49-5834-420f-a5b6-65bd840c7008.001.png)

Example Response

200 OK

Body 

Header(4)

"apple"

GET

weapon

http://127.0.0.1:5000/weapon




Example Request

weapon

View More

import requests

url = "http://127.0.0.1:5000/weapon"

payload={}

headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

![](Aspose.Words.83e78e49-5834-420f-a5b6-65bd840c7008.001.png)

Example Response

200 OK

Body 

Header(4)

View More

[

`  `{

`    `"id": 1,

`    `"name": "Arrow",

`    `"stock": 2

`  `},

`  `{

`    `"id": 2,

`    `"name": "Lance",

`    `"stock": 3

`  `},

POST

weapon

http://127.0.0.1:5000/weapon

BODYraw

{

`    `"name": "Spear",

`    `"stock": 1

}




Example Request

weapon

View More

import requests

url = "http://127.0.0.1:5000/weapon"

payload = "{\r\n    \"name\": \"Spear\",\r\n    \"stock\": 1\r\n}"

headers = {}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

![](Aspose.Words.83e78e49-5834-420f-a5b6-65bd840c7008.001.png)

Example Response

200 OK

Body 

Header(4)

{

`  `"id": 7,

`  `"name": "Spear",

`  `"stock": 1

}

DEL

weapon/id

weapon/id




Example Request

weapon/id

View More

import requests

url = "http://127.0.0.1:5000/weapon/4"

payload={}

headers = {}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)

![](Aspose.Words.83e78e49-5834-420f-a5b6-65bd840c7008.001.png)

Example Response

200 OK

Body 

Header(4)

{

`  `"id": 4,

`  `"name": "Spear",

`  `"stock": 1

}

PUT

weapon/id

http://127.0.0.1:5000/weapon/4




Example Request

weapon/id

View More

import requests

url = "http://127.0.0.1:5000/weapon/2"

payload = "{\r\n    \"name\": \"Lance\",\r\n    \"stock\": 3\r\n}"

headers = {}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)

![](Aspose.Words.83e78e49-5834-420f-a5b6-65bd840c7008.001.png)

Example Response

200 OK

Body 

Header(4)

[

`  `{

`    `"id": 2,

`    `"name": "Lance",

`    `"stock": 3

`  `}

]
