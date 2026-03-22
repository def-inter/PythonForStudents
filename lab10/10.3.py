"""
    source 10.3.py

    **10.3 ( Подсчет вхождений чисел )
    Напишите программу, которая считывает
    несколько целых чисел от 1 до 100 и подсчитывает вхождения каждого из них.

    author Protasenya Yulian
    email nasamalashfreak@gmail.com
    version 2025.2.2(EAP) 18.09.2025
    group 10701325
"""

from math import *
integers =[int(i) for i in input("Enter integers between 1 and 200: ").split(' ')]
set_integers = set(integers)
for el in set_integers:
    if(integers.count(el) > 1):
        print(f"{el} occurs {integers.count(el)} times")
    else:
        print(f"{el} occurs {integers.count(el)} time")