"""Парсим ответ API в JSON формате"""
import json, requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
data_response = json.loads(response.text)

data_response_id = {}
for todo in data_response:
    try:
        if todo['completed']:
            data_response_id[todo['userId']]+=1
    except KeyError:
        data_response_id[todo['userId']] = 1
print(data_response_id)
