# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
import shutil

def create_dir():
    """"""""""""""""'Создаем папки"""""""""""""""""
    name = str(input("Введите имя директории: "))
    number_copy = int(input('Введите количество папок: '))
    import os
    i = 1
    while i <= number_copy:
        dir_name = os.path.join(os.getcwd(), name + str(i))
        try:
            os.mkdir(dir_name)
        except FileExistsError:
            print("Папки уже созданы")
        i += 1
        print("Папки успешно созданы", dir_name)

def delete_dir():
    '''''''''''''''''''Удаляем папки'''''''''''''''''''''''''
    name_del = str(input("Введите имя директории: "))
    number_copy_del = int(input('Введите количество папок: '))
    a = 1
    while a <= number_copy_del:
        dir_name_del = os.path.join(os.getcwd(), name_del + str(a))
        if os.path.isdir(dir_name_del):
            shutil.rmtree(dir_name_del)
        else:
            print("Такой папки нет", dir_name_del)
        a += 1
        print("Папки удалены: ", dir_name_del)

create_dir()
delete_dir()
# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def dir_name(a):
    """"""""'Отображение файлов директории'""""""
    a = os.listdir()
    print([z for z in enumerate(a, start=1)])
# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
a = os.path.basename(__file__)

if os.path.isfile(a):
    new_file = a + '.dupl.py'
    shutil.copy(a, new_file)
    print("Файл успешно создан")
