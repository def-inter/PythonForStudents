"""
    source 10.2.py

    10.2 ( Поменяйте местами введенные числа )
    Напишите программу, которая
    считывает список целых чисел и отображает их в порядке, обратном тому, в
    котором они были прочитаны.

    author Protasenya Yulian
    email nasamalashfreak@gmail.com
    version 2025.2.2(EAP) 18.09.2025
    group 10701325
"""

from math import *
numbers =[int(i) for i in input("Enter numbers: ").split(' ')]
numbers.reverse()
print(*numbers)