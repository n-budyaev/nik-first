import sys
import os
import shutil
import psutil
#utf-8

print("Дароу")
name = input("Как тебя зовут?\n")
print("Добро пожаловать, ",name)
print("Кароче, это типо бот")
print("Готов поработать,",name)
agree = ''
while agree != 'n':
    agree = input("Если хочешь поработать, нажми y, если выйти - n\n")
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
        #while agree != 'n':
            # print("Еще раз!")
            # print()
            # print("1 - Вывести список файлов в данной директории")
            # print("2 - Вывести информацию о системе")
            # print("3 - Вывести список процессов")
            # print("4 - сделать дубликаты файлов в указанной папке")
            # print("5 - удалить дубликаты файлов в указанной папке")
            # print("9 - Для выхода")
            # print()
        do = int(input("твой выбор? "))
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
            print()
        elif do == 3:
            print(psutil.pids())
        elif do == 4:
            print()
            print("дублирование файлов в в указанной папке")
            dir_name = input("Введите имя папки для дублирования файлов \n")
            file_list = os.listdir(dir_name)
            i = 0
            j = 0
            while i < len(file_list):
    # Необходимо выполнить проверку isfile, т.к. при попытке копирования директории будет возникать ошибка                
                if os.path.isfile(file_list[i]):
                    newfile = file_list[i] + '.dupl'
                    shutil.copy(file_list[i], newfile)
                    print(newfile)
                    j +=1
                i += 1
            print("Создано ", j, " дубликатов")
        elif do == 5:
            print("Удаление файлов с расширением .dupl в указанной папке")
            dir_name = input("Введите имя папки для дублирования файлов\n")
            print()
            file_list = os.listdir(dir_name)
            i = 0
            j = 0
            while i < len(file_list):
                full_name = os.path.join(dir_name,file_list[i])
                if full_name.endswith('.dupl'):
                    print(file_list[i])
                    os.remove(full_name)
                    j +=1
                i += 1
            print("Удалено ", j, " файлов")
        elif do == 9:
            print("Покеда")
            sys.exit()
        else:
            print("Введи норм число")
print("Не хочешь, значит? Ну тогда пока!")
