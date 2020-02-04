"""Работа с файлами"""

FILE_OPEN = open('ex_text_1.txt', 'r', encoding='utf-8')
print(FILE_OPEN.read())


FILE_WRITE = open('ex_text_write.txt', 'w', encoding='utf-8')
for i in range(100):
    FILE_WRITE.write('{} в квадрате {} ; \n'.format(i, i ** 2))
FILE_WRITE.close()
