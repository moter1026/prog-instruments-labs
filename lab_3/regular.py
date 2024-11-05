import csv
import re

import consts


def match_check(string: str, regular: str) -> bool:
    """
    проверяет строку регулярным выражением при помощи re.match

    :param string: строка, которую необходимо проверить
    :param string: регулярное выражение для этой строки
    :return: True - если значение валидное, False - иначе
    """
    result = re.match(regular, string)
    if not result:
        return False
    return True


def check_csv(file_name: str) -> list[int]:
    """
    Функция ищет в строках .csv файла с именем file_name невалидные значения.
    Возвращает целочисленный список с кол-вом невалидных значений в каждой строке файла

    :param file_name: имя или путь до файла
    :return: целочисленный список с кол-вом невалидных значений в каждой строке
    """
    try:
        err_list = []
        with open(file_name,"r", encoding="utf-16") as read_file:
            csv_file = csv.reader(read_file, delimiter=";")
            first = True
            names = []
            index_err = 0
            for row in csv_file:
                if first:
                    names = row
                    first = False
                    continue
                err_list.append(0)
                index_names = 0
                for val in row:
                    if not match_check(str(val),str(consts.REGULAR_DICT[names[index_names]])):
                        err_list[index_err] += 1
                    index_names += 1
                index_err += 1
        return err_list
    except Exception as e:
        print(e)