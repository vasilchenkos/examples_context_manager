"""Пример работы с файлами json"""
import json

with open('users.json', 'r') as file_open:
    data = json.load(file_open)

with open('output.json', 'w') as file_output:
    json.dump(data, file_output, indent=4)

str = json.dumps(data, indent=4)
print(str)
