from contextlib import contextmanager


@contextmanager
def file_open(path):
    try:
        f_obj = open(path, 'w', encoding='utf-8')
        yield f_obj
    except OSError:
        print("Такого файла не нашлось")
    finally:
        print("Получилось открыть файл и записать данные. Закрываем файл")
        f_obj.close()


if __name__ == '__main__':
    with file_open('test2.txt') as fobj:
        fobj.write('Тест контекстного менеджера')
