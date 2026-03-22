"""
    source 10.5.py

    **10.5 ( Вывести отдельные числа )
    Напишите программу, которая считывает
    числа, разделенные пробелом, в одной строке и отображает отдельные числа

    author Protasenya Yulian
    email nasamalashfreak@gmail.com
    version 2025.2.2(EAP) 18.09.2025
    group 10701325
"""

from math import *
numbers =[int(i) for i in input("Enter numbers: ").split(' ')]
new_numbers = [numbers[0]]
# new_numbers.append(numbers[0])
for i in range(len(numbers)):
    count = 0
    for j in range(len(new_numbers)):
        if numbers[i] == new_numbers[j]:
            count+=1
        if count == 1:
            break
    if count == 0 :
        new_numbers.append(numbers[i])


print("The distinct numbers are:" ,*new_numbers)
