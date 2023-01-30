import Func as fn
import re
import os

stack = []

OPERATOR = ['+', '-', '*', '/', '^']


# я не знаю как правильно вывести ошибки тут. Вылетает много технической информации
class MyError(Exception):
    def __init__(self, text):
        os.system('cls')
        self.txt = text

# наверняка можно сделать без регулярок просто через поиск символа


def Calc(valid_string):
    for element_of_expr in re.split(r"\s+", valid_string):
        try:
            # пробуем сделать числом если ошибка то опрератор
            element_of_expr = float(element_of_expr)
            stack.append(element_of_expr)
        except ValueError:
            for oper in element_of_expr:
                if oper not in OPERATOR:
                    continue
                try:
                    oper2 = stack.pop()
                    oper1 = stack.pop()
                except IndexError:
                    raise MyError("мало операндов")
                try:
                    if (oper == OPERATOR[0]):  # не слишком элегантно но работает
                        oper = fn.summ(oper1, oper2)
                    elif (oper == OPERATOR[1]):
                        oper = fn.difference(oper1, oper2)
                    elif (oper == OPERATOR[2]):
                        oper = fn.mult(oper1, oper2)
                    elif (oper == OPERATOR[3]):
                        oper = fn.div(oper1, oper2)
                    elif (oper == OPERATOR[4]):
                        oper = fn.exp(oper1, oper2)
                except ZeroDivisionError:
                    raise MyError("деление на 0")
                stack.append(oper)
    if len(stack) != 1:
        raise MyError("много операндов последовательно")
    return stack.pop()


# print(Calc('2 3 5 / *'))
