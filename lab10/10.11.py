"""
    source 10.11.py

    *10.11 ( Выбор случайного числа )
    Напишите тестовую программу, которая предлагает пользователю ввести список
    чисел, вызывает функцию для перетасовки чисел и отображает числа.

    author Protasenya Yulian
    email nasamalashfreak@gmail.com
    version 2025.2.2(EAP) 18.09.2025
    group 10701325
"""

from math import *
from random import *
numbers = [int(i) for i in input("Enter numbers: ").split(' ')]
def s_shuffle(numbers):
    for i in range(len(numbers) - 1,0,-1):
        j = randint(0,i)
        numbers[i],numbers[j] = numbers[j],numbers[i];
    return numbers
print("Before",*numbers)
s_shuffle(numbers)
print("After",*numbers)