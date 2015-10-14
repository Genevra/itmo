#!/usr/bin/python3.4
#coding: utf-8

'''
Даны 3 круга диаметрами:
- 45
- 338
- 19
Посчитать площади кругов и вычесть 2 площади из 3-ьей.
'''

import math

diameter_0 = 45
diameter_1 = 338
diameter_2 = 19

sq_0 = math.pi * ((diameter_0 / 2) ** 2)
sq_1 = math.pi * ((diameter_1 / 2) ** 2)
sq_2 = math.pi * ((diameter_2 / 2) ** 2)

print(sq_2 - sq_1 - sq_0)


