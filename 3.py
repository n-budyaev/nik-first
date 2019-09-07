import sys
import os
import shutil
import psutil
#utf-8

print("Дароу")
name = input("Как тебя зовут?")
print("Добро пожаловать, ",name, " (я знаю я даун)")
print("Кароче, это типо бот")
print("Готов поработать,",name)
agree = input("Y/N ")
if agree == "Y" or 'y':
    print("Начнем!")
    print("Кароче, это супер пупер навороченный бот")
    print("Я тип могу:")
    print()
    print("1 - Вывести список файлов в данной директории")
    print("2 - Вывести информацию о системе")
    print("3 - Вывести список процессов")
    print("4 - сделать дубликаты файлов в указанной папке")
    print("5 - удалить дубликаты файлов в указанной папке")
    print("9 - Для выхода")
    print()
    do = int(input("1/2/3/4/5/9"))
    print()
    if do == 1:
        print()
        print(os.listdir())
        print()
    elif do == 2:
        print()
        print('кол-во CPU:', psutil.cpu_count())
        print('логин пользователя:', os.getlogin())
        print('код-ка файловой системы:', sys.getfilesystemencoding())
        print('платформа ОС:', sys.platform)
        print('имя текущей директории:', os.getcwd())
    elif do == 3:
        print(psutil.pids())
    elif do == 4:
        print()
        print("дублирование файлов в в указанной папке")
        dir_name = input("Введите имя папки для дублирования файлов  ")
        file_list = os.listdir(dir_name)
        i = 0
        while i < len(file_list):
# Необходимо выполнить проверку isfile, т.к. при попытке копирования директории будет возникать ошибка                
            if os.path.isfile(file_list[i]):
                newfile = file_list[i] + '.dupl'
                shutil.copy(file_list[i], newfile)
                print(newfile)
            i += 1
        print("Создано ", len(file_list), " дубликатов")
    elif do == 5:
        print("Удаление файлов с расширением .dupl в указанной папке")
        dir_name = input("Введите имя папки для дублирования файлов")
        print()
        file_list = os.listdir(dir_name)
        i = 0
        while i < len(file_list):
            full_name = os.path.join(dir_name,file_list[i])
            if full_name.endswith('.dupl'):
                print(file_list[i])
                os.remove(full_name)
            i += 1
        print("Удалено ", len(file_list), " файлов")
    elif do == 9:
        print("Покеда")
    else:
        print("Введи норм число")
elif agree == "N" or 'n':
    print("Ну тогда пока!")
    sys.exit
else:
    print("Как я понял, ты хочешь выйти")
    print("Ну пока")
    sys.exit