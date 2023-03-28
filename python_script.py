import os
import shutil

COUNT_DIR = 5
COUNT_DIR_MOVE = 5
PATH_DIR_REPORT = os.getcwd() + '\inputFiles'
PATH_MOVE_DIR = os.getcwd() + '\outputFiles'

def create_dir_with_report(PATH_DIR_REPORT, COUNT_DIR):
    """
    Функция создает определенное кол-во репозиториев и файлов по переданному пути
    и печатает кол-во созданых файлов и папок

    :param PATH_DIR_REPORT: Путь до репозитория
    :param COUNT_DIR: Кол-во репозирориев и документов
    :return:
    """

    print('Создание отчетов и папок')

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
        print()

    print(f'Созданы {count_dir} директорий:')
    for i in list_dirs:
        print(i)
        print()


def create_move_dir(PATH_MOVE_DIR, COUNT_DIR_MOVE):
    """
    Создает директории для перемещения туда отчетов
    и печатает кол-во созданых файлов и папок

    :param PATH_MOVE_DIR: Путь до репозитория
    :param COUNT_DIR_MOVE: Кол-во репозиториев
    :return:
    """

    print('Создание директории для перемещения туда отчетов')

    for i in range(COUNT_DIR_MOVE):
        os.makedirs(f'{PATH_MOVE_DIR}\\Directory{i}')

    count_files_move = 0  # Кол-во файлов
    list_files_move = []
    count_dir_move = 0  # Кол-во папок
    list_dirs_move = []

    for rootdir, dirs, files, in os.walk(PATH_MOVE_DIR):
        for file in files:
            count_files_move += 1
            list_files_move.append(file)
        for dir in dirs:
            count_dir_move += 1
            list_dirs_move.append(dir)

    print(f'Созданы {count_files_move} файлов:')
    for i in list_files_move:
        print(i)
        print()
    print(f'Созданы {count_dir_move} директорий:')
    for i in list_dirs_move:
        print(i)
        print()


def move_report(PATH_DIR_REPORT, PATH_MOVE_DIR):
    """
    Функция перемещает все файлы из первой директории в
    в подпапки второй директории
    :param PATH_DIR_REPORT: путь, откуда копируем файлы (первая директория)
    :param PATH_MOVE_DIR:   путь, куда копируем файлы (вторая директория)
    :return:
    """

    for rootdirO, dirsO, filesO, in os.walk(PATH_MOVE_DIR):
        for dir in dirsO:
            for rootdir, dirs, files, in os.walk(PATH_DIR_REPORT):
                for file in files:
                    if file in next(os.walk(rootdirO + '\\' + dir))[2]:
                        pass
                    else:
                        shutil.copy(rootdir + '\\' + file, rootdirO + '\\' + dir)
                        print(f'Копирование файла {file} в каталог {rootdirO}\\{dir}')
                        assert os.path.exists(rootdirO + '\\' + dir + '\\' + file), 'Файл не скопирован'
                        print(f'Копирование ушпешно')


def test_script_files_move(PATH_MOVE_DIR, PATH_DIR_REPORT):
    """
    Проверка
    Сравнение файлов в исходном каталоге и куда скопировали файлы

    :param PATH_MOVE_DIR: Каталог, куда копировали файлы
    :param PATH_DIR_REPORT: Каталог, откуда брали файлы
    :return:
    """
    assert os.path.exists(PATH_DIR_REPORT), 'Не наден исходный каталог'
    assert os.path.exists(PATH_MOVE_DIR), 'Не найден каталог для копирования'

    list_input_files = []
    for rootdir, dirs, files, in os.walk(PATH_DIR_REPORT):
        for file in files:
            if file != None and not (file in list_input_files):
                list_input_files.append(file)

    assert len(list_input_files) != 0, 'Исходный каталог пуст'

    list_output_files = []
    for rootdir, dirs, files, in os.walk(PATH_MOVE_DIR):
        for dir in dirs:

            for rootdirD, dirsD, filesD, in os.walk(PATH_MOVE_DIR + '\\' + dir):
                for file in filesD:
                    if file != None:
                        list_output_files.append(file)

            list_output_files.sort()
            list_input_files.sort()
            for i in range(len(list_input_files)):
                assert list_input_files[i] == list_output_files[i], f'Файл {list_input_files[i]} не скопирован \n' \
                                                                    f' в каталог {PATH_MOVE_DIR}\\{dir}'

            list_output_files = []

    print('Скрипт выполнен успешно')


if __name__ == '__main__':
    """
    Это не обязательно, для теста создает директории
    указать
    PATH_DIR_REPORT = os.getcwd() + '\inputFiles'
    PATH_MOVE_DIR = os.getcwd() + '\outputFiles'
    """
    # create_dir_with_report(PATH_DIR_REPORT, COUNT_DIR)
    # create_move_dir(PATH_MOVE_DIR, COUNT_DIR_MOVE

    move_report(PATH_DIR_REPORT, PATH_MOVE_DIR)
    test_script_files_move(PATH_MOVE_DIR, PATH_DIR_REPORT)
