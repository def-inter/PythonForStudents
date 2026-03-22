"""
    source 10.16.py

    **10.16 ( Пузырьковая сортировка )
    Напишите функцию сортировки,
    использующую алгоритм пузырьковой сортировки.

    author Protasenya Yulian
    email nasamalashfreak@gmail.com
    version 2025.2.2(EAP) 18.09.2025
    group 10701325
"""

from math import *
from random import *

numbers = [int(i) for i in input("Enter numbers: ").split(' ')]
count = 0
while count != len(numbers) - 1:
    count = 0
    for i in range(len(numbers) - 1):
        if numbers[i] < numbers[i + 1]:
            numbers[i],numbers[i + 1] = numbers[i + 1],numbers[i];
        else:
            count +=1
print("Sorted list:",*numbers)