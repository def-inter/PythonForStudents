"""
    source 10.12.py

    10.12 ( Вычисление НОД )
    Напишите функцию, которая возвращает наибольший
    общий делитель (НОД) целых чисел в списке.

    author Protasenya Yulian
    email nasamalashfreak@gmail.com
    version 2025.2.2(EAP) 18.09.2025
    group 10701325
"""

from math import *
from random import *
numbers = [int(i) for i in input("Enter numbers: ").split(' ')]
gsd_el = numbers[0]
def gsdEl(number,gsd_el):
    while gsd_el * number != 0:
        if number > gsd_el:
            number = number % gsd_el
        else:
            gsd_el = gsd_el % number
    return gsd_el + number
for i in range(len(numbers)):
    gsd_el = gsdEl(numbers[i],gsd_el)
print("GSD of this numbers is",gsd_el)