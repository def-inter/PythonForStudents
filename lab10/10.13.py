"""
    source 10.13.py

    10.13 ( Устранение дубликатов )
    Напишите функцию, которая возвращает новый
    список, удаляя повторяющиеся значения в списке.

    author Protasenya Yulian
    email nasamalashfreak@gmail.com
    version 2025.2.2(EAP) 18.09.2025
    group 10701325
"""

from math import *
from random import *
numbers = [int(i) for i in input("Enter numbers: ").split(' ')]
print(numbers[0],end = ' ')
def eliminateDublicates(numbers):
    new_numbers = [numbers[0]]
    for i in range(len(numbers)):
        count = 0
        for j in range(len(new_numbers)):
            if numbers[i] == new_numbers[j]:
                count+=1
            if count == 1:
                break
        if count == 0 :
            print(numbers[i],end = ' ')
            new_numbers.append(numbers[i])
eliminateDublicates(numbers)

