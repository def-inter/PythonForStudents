"""
    source 10.23.py

    10.23 ( Алгебра: решение квадратных уравнений )
    Напишите функцию для
    решения квадратного уравнения

    author Protasenya Yulian
    email nasamalashfreak@gmail.com
    version 2025.2.2(EAP) 18.09.2025
    group 10701325
"""
from math import *

eqp = [int(i) for i in input("Coefficients: ").split(' ')]
roots = []
if eqp[1] ** 2 - 4 * eqp[0] * eqp[2] >= 0:
    roots.append(((-1) * eqp[1] - (sqrt(eqp[1] ** 2 - 4 * eqp[0] * eqp[2])) )/(2 * eqp[0]))
    roots.append(((-1) * eqp[1] + (sqrt(eqp[1] ** 2 - 4 * eqp[0] * eqp[2]))) / (2 * eqp[0]))
    print("Количество всех корней: 3")
    print("Количество некомплексных корней: 2")
    print("Корень 1:",roots[0])
    print("Корень 2:", roots[1])
else:
    print("Количество всех корней: 3")
    print("Количество некомплексных корней: 0")
