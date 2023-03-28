import os
import shutil

PATH_DIR_REPORT = os.getcwd() + '\inputFiles'
COUNT_DIR = 5


def create_dir_with_report(PATH_DIR_REPORT, COUNT_DIR):
    """
    Функция создает определенное кол-во репозиториев и файлов по переданному пути

    :param PATH_DIR_REPORT: Путь до репозитория
    :param COUNT_DIR: Кол-во репозирориев и документов
    :return:
    """

    for i in range(COUNT_DIR):
        os.makedirs(f'{PATH_DIR_REPORT}\\Directory{i}')
        open(f'testfile{i}.txt', 'w')
        shutil.move(f'testfile{i}.txt', f'inputFiles\Directory{i}')

    os.makedirs(f'{PATH_DIR_REPORT}\\DirectoryEmply')
    os.makedirs(f'{PATH_DIR_REPORT}\\Directory5Report')
    for i in range(5):
        open(f'testfile5Report{i}.txt', 'w')
        shutil.move(f'testfile5Report{i}.txt', f'{PATH_DIR_REPORT}\\Directory5Report')

    count_files = 0  # Кол-во файлов
    list_files = []
    count_dir = 0  # Кол-во папок
    list_dirs = []

    for rootdir, dirs, files, in os.walk(PATH_DIR_REPORT):
        for file in files:
            count_files += 1
            list_files.append(file)
        for dir in dirs:
            count_dir += 1
            list_dirs.append(dir)

    print(f'Созданы {count_files} файлов:')
    for i in list_files:
        print(i)
    print(f'Созданы {count_dir} директорий:')
    for i in list_dirs:
        print(i)




