#!/usr/bin/python3.4
# coding: utf-8

'''
Есть функция input, позволяет подождать, пока пользователь что-то введет и нажмет Enter,
и получить его ввод в виде строки. Как-то так: x = input("Задай число x:")

Сделать простой калькулятор: вводим 2 числа и действие. Он считает и выводит на экран.

Действий реализовать столько, на сколько хватит энтузиазма и времени.
'''


def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    if y != 0:
        return x / y
    else:
        print('Ошибка: На ноль делить нельзя!')

x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))
result = str(input('Выберете одну из операций над числами: +, -, *, /\n'))

if result == '+':
    print('Результат: ',addition(x, y))
elif result == '-':
    print('Результат: ',subtraction(x, y))
elif result == '*':
    print('Результат: ',multiplication(x, y))
elif result == '/':
    print('Результат: ',division(x, y))
else:
    print('Ошибка: неправильная операция!')