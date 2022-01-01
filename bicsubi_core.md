![](Aspose.Words.bd9b4f77-a958-46dd-b036-52721913b0a3.001.png)

Public 

`	`Documentation Settings![](Aspose.Words.bd9b4f77-a958-46dd-b036-52721913b0a3.001.png)

Environment

No Environment

Layout

Double Column

Language

cURL
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

curl --location --request GET 'http://127.0.0.1:5000/whoami'

![](Aspose.Words.bd9b4f77-a958-46dd-b036-52721913b0a3.001.png)

GET

echo?string="string"

No request URL found. It will show up here once added.




Example Request

echo?string="string"

curl --location --request GET ''

![](Aspose.Words.bd9b4f77-a958-46dd-b036-52721913b0a3.001.png)

GET

weapon

http://127.0.0.1:5000/weapon




Example Request

weapon

curl --location --request GET 'http://127.0.0.1:5000/weapon'

![](Aspose.Words.bd9b4f77-a958-46dd-b036-52721913b0a3.001.png)

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

curl --location --request POST 'http://127.0.0.1:5000/weapon' \

--data-raw '{

`    `"name": "Spear",

`    `"stock": 1

}'

![](Aspose.Words.bd9b4f77-a958-46dd-b036-52721913b0a3.001.png)

DEL

weapon/id

weapon/id




Example Request

weapon/id

curl --location --request DELETE 'weapon/id'

![](Aspose.Words.bd9b4f77-a958-46dd-b036-52721913b0a3.001.png)

PUT

weapon/id

http://127.0.0.1:5000/weapon/4




Example Request

weapon/id

curl --location --request PUT 'http://127.0.0.1:5000/weapon/4'

![](Aspose.Words.bd9b4f77-a958-46dd-b036-52721913b0a3.001.png)
