"""Работа с файлами"""

"""Пример конструкции для Python2"""
FILE_OPEN = open('ex_text_1.txt', 'r', encoding='utf-8')
print(FILE_OPEN.read())
# for line in FILE_OPEN:
#     print(line)
FILE_OPEN.close()


FILE_WRITE = open('ex_text_write.txt', 'w', encoding='utf-8')
for i in range(100):
    FILE_WRITE.write('{} в квадрате {} ; \n'.format(i, i ** 2))
FILE_WRITE.close()
