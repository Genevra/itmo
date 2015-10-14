#!/usr/bin/python3.4
#coding: utf-8

'''
Задание.
Создать файл со списком чисел
Прочитать файл
Первых два числа сложить
Третье, четвёртое перемножить и взять корень от числа
Всё вывести на экран
Взять максимальное от двух получившихся и вывести на экран
От пятого числа в файле взять косинус
'''

import math

#Создаём файл с данными
myfile = open('Numbers.txt', 'w')
myfile.writelines(['234\n',
                   '98\n',
                   '567\n',
                   '33\n',
                   '16\n'])
myfile.close()

f = open('Numbers.txt', 'r')
lines = f.readlines()
f.close()

addition = int(lines[0]) + int(lines[1])
multiplication_and_sqrt = round(math.sqrt(int(lines[2]) * int(lines[3])))

print('Результат сложения первых двух чисел:', addition)
print('-' * 79)
print('Умножение третьего и четвёртого числа, корень числа:', multiplication_and_sqrt)
print('-' * 79)
print('Максимальное число из двух:', max(addition, multiplication_and_sqrt))
print('-' * 79)
print('Косинус пятого числа', int(lines[4]), ':', round(math.cos(int(lines[4]))))

