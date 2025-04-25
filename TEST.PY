import openpyxl
import math


def read_xlsx():
    work_book = openpyxl.load_workbook('gradebook.xlsx')

    sheet_obj = work_book.active
    for row in sheet_obj.iter_rows(min_row=1, values_only=True):
        name = row[0]
        grades = list(filter(lambda x: isinstance(x, (int, float)), row[1:]))
        sorted_grades = sorted(grades, reverse=True)
        five_grades = sorted_grades[:5]
        while len(five_grades) < 5:
            five_grades.append(0)

        average_grade = math.ceil(sum(five_grades)/5)
        print(f'{name}: {average_grade}')


read_xlsx()
