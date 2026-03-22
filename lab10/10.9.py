"""
    source 10.9.py

    *10.9 ( Статистика: вычисление отклонения )
    Напишите тестовую программу, которая предлагает пользователю ввести список
    чисел и отображает среднее и стандартное отклонение,

    author Protasenya Yulian
    email nasamalashfreak@gmail.com
    version 2025.2.2(EAP) 18.09.2025
    group 10701325
"""

from math import *
from random import *
numbers = [float(i) for i in input("Enter numbers: ").split(' ')]
def mean(numbers):
    sum = 0
    for i in range(len(numbers)):
        sum += numbers[i]
    return sum / len(numbers)
def deviation(numbers,mean):
    deviation = 0
    for i in range(len(numbers)):
        deviation += ((numbers[i] - mean) ** 2)
    return (deviation / (len(numbers) - 1))  ** 0.5
mean = mean(numbers)
print("The mean is",mean)
print("The standard deviation is",deviation(numbers,mean))