"""
    source 10.1.py

    10.1 ( Назначение оценок )
    Напишите программу, которая считывает список
    оценок и затем выставляет оценки

    author Protasenya Yulian
    email nasamalashfreak@gmail.com
    version 2025.2.2(EAP) 18.09.2025
    group 10701325
"""
from math import *
grades = [int(i) for i in input("Enter scores: ").split(' ')]
best_mark = max(grades)
for i in range(len(grades)):
    if(best_mark - 10 <= grades[i] ):
        print(f"Student {i} score is {grades[i]} and grade is A")
    elif (best_mark - 20 <= grades[i]):
        print(f"Student {i} score is {grades[i]} and grade is B")
    elif (best_mark - 30 <= grades[i]):
        print(f"Student {i} score is {grades[i]} and grade is C")
    elif (best_mark - 40 <= grades[i]):
        print(f"Student {i} score is {grades[i]} and grade is D")
    else:
        print(f"Student {i} score is {grades[i]} and grade is F")