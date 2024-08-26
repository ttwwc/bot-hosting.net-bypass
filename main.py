import requests
import random

url = "https://bot-hosting.net/api/freeCoins"
authorization_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjExODkwMzExNjEzNDc5ODE0MDMiLCJhdmF0YXIiOiJjZjYzNjM0OTU4OGE0ZTJlMmNmYzVjN2QyMjA1YzM2MSIsInVzZXJuYW1lIjoic290d2MjMCIsImp0aSI6IjYzNDZkNTBiLWNjOGQtNGUyOC1hYTU1LWE1YjI2N2IwOTliNyIsImlhdCI6MTcxMTc2MDc3MCwiZXhwIjoxNzEyOTcwNzcwfQ.jX11-t2IRVEFLXOwycv8L9_rvmsb8rVUZlj_1Sbh49I"
cookie_value = "_ga=GA1.1.411955593.1710557002; _ga_S0VHSF9NEZ=GS1.1.1710658411.6.1.1710658434.0.0.0" # find ur cookie by inspecting the request sent when claiming the first coin

headers = {
    "Authorization": authorization_token,
    "Cookie": cookie_value
}

response = requests.post(url, headers=headers)

print(response.status_code)
print(response.text)
