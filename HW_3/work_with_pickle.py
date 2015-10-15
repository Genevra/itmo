#!/usr/bin/python3.4
#coding: utf-8

'''
»> import pickle
»> data = {
... 'a': [1, 2.0, 3, 4+6j],
... 'b': ("character string", b"byte string"),
... 'c': {None, True, False}
... }
»>
»> f = open('c:/temp/data.pickle', 'wb')
... pickle.dump(data, f)
...
»> with open('data.pickle', 'rb') as f:
... data_new = pickle.load(f)

1. Сделайте простую базу данных:

Пользователь вводит команду: ввести, вывести
- Ввести - пользователь вводит марку автомобиля и его мощность. Необходимо проверить, что марка состоит только из букв
латинского или русского алфавитов. Мощность только из цифр.

- Вывести - выводятся все автомобили - по алфавиту. Сортировку сделать сначала стандартным методом.
Затем написать свою версию сортировки циклами.

2. Реализовать поиск/фильтрацию в базе данных - то есть вывод по условию.

- По мощности - конкретное число, больше, меньше, в промежутке.
- По вхождению слова в название.
- По полному соответствию слова.
'''

import pickle
data = {
    'Auto': {
        'opel': 95,
        'mazda': 110,
        'mersedes': 120
    }
}

f = open('Auto.pickle', 'wb')
pickle.dump(data, f)
f.close()

answer = str(input('input / output: '))
if answer == 'input':
    print('yo')
elif answer == 'output':
    print('hoy')
else:
    print('no')