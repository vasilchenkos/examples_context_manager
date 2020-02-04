"""Пример работы контекстного менеджера"""

with open('text.txt', 'r') as open_text:
    for i in open_text.read().split():
        print('test case is ' + i + ' ')
