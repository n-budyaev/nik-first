# Использование функций
# Функция удаления дубликатов
# Вывод количества удаленных дубликатов
# Удаление файлов с расширением окончанием dupl
# coding: utf-8
import time
import sys
import winsound
import os
import psutil
import shutil

FREQUENCY = 2500  # Set Frequency To 2500 Hertz
DURATION = 500  # Set Duration To 1000 ms == 1 second

def stroka():
    i = 0
    ii = 0
    mas = []
    while i < 66:
        i +=1
        mas.append(i)
    for ii in mas[:]:
        print('-', end='')
        sys.stdout.flush()
        time.sleep(0.01)

#stroka()

def duplicate_file(filename):
    if os.path.isfile(filename):
        newfile: object =  filename + '.dupl'
        #do copy
        shutil.copy(filename, newfile)
        if os.path.exists(newfile):
            print("Файл ", newfile, " был успешно создан")
        else:
            print("Что-то пошло не так...")

def delete_files(filename):
    j: int = 0
    dirname = os.getcwd()
    for f in filename:
        fullname = os.path.join(dirname, f)
        if fullname.endwith('.dupl'):
            os.remove(fullname)
            if not os.path.exists(fullname):
                j +=1
    print('Удалено ', j, ' файлов')

# Удалить все .dupl в папке
def delete_all_files():
    # if not dirname and dirname.strip():
    dirname = os.getcwd()
    file_list = os.listdir(dirname)
    j = 0
    for f in file_list:
        fullname = os.path.join(dirname, f)
        if fullname.endswith('.dupl') == True:
            os.remove(fullname)
            if not os.path.isfile(fullname):
                print("Файл ", fullname, " успешно удален")
                j +=1
            else:
                print("Что-то пошло не так...")
    return print("Удалено ", j, " файлов")

def sys_info():
    print("Вот что я знаю о системе:")
    print("Количество процессоров: ", psutil.cpu_count())
    print("Платформа: ", sys.platform)
    print("Кодировка файловой системы: ", sys.getfilesystemencoding())
    print("Текущая директория: \n ", os.getcwd())
    print("Текущий пользователь: ", os.getlogin())

def main():
    stroka()
    winsound.Beep(FREQUENCY, DURATION)
    print("\nДобро пожаловать в процесс hacker 2!")
    stroka()
    winsound.Beep(FREQUENCY, DURATION)
    answer = ''
    while answer != 'Q':
        answer = input("\nБудем работать? (Y/N/Q) Q - выход \n")
        if answer == 'Y':
            stroka()
            winsound.Beep(FREQUENCY, DURATION)
            print("\nСписок доступной информации")
            stroka()
            print("\n")
            winsound.Beep(FREQUENCY, DURATION)
            print(" [1]  - вывод списка файлов в директории")
            print(" [2]  - вывод системной информации функцией")
            print(" [3]  - продублировать файлы в текущей директории")
            # remove из модуля os
            print(" [4]  - функция удалить файлы с окончанием dupl")
            print(" [5]  - продублировать выбранный файл функцией")
            print("с помощью функции и вывести количество созданных файлов")
            print(" [Для выхода нажмите любую другую клавишу]")
            try:
                do = int(input("\nВведите число: "))
            except ValueError:
                break
            finally:
                if do == 1:
                    print(os.listdir())
                elif do == 2:
                    sys_info()
                elif do == 3:
                    file_list = os.listdir()
                    i = 0
                    while i < len(File_list):
                        # проферка файл или нет
                        if os.path.issfile(file_list[i]):
                            newfile = file_list[i] + '.dupl'
                            # do copy
                            shutil.copy(file_list[i], newfile)
                            if os.path.exists(newfile):
                                print("Файл ", newfile, " был успешно создан")
                        i += 1
                elif do == 4:
                    print(os.listdir())
                    # dirname = input("\nУкажите имя папки, или пропустите, если нужна корневая папка программыH:\n")
                    delete_all_files()
                    print(os.listdir())
                elif do == 5:
                    print(os.listdir())
                    file_name = input("\nУкажите имя файла:\n")
                    duplicate_file(file_name)
                    print(os.listdir())
                print("Для выхода из программы введите букву Q")
                winsound.Beep(FREQUENCY, DURATION)

if __name__ == "__main__":
    main()

