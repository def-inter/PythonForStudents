"""
    source 10.7.py

    *10.7 (Count single digits)
    Write a program that generates 1000 random integers
    between 0 and 9 and displays the count for each number.

    author Protasenya Yulian
    email nasamalashfreak@gmail.com
    version 2025.2.2(EAP) 18.09.2025
    group 10701325
"""

from math import *
from random import *

integers =[]
for i in range(1000):
    integers.append(randint(0,9))
set_integers = set(integers)
for el in set_integers:
    if(integers.count(el) > 1):
        print(f"{el} occurs {integers.count(el)} times")
    else:
        print(f"{el} occurs {integers.count(el)} time")


