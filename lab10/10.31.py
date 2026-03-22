"""
    source 10.31.py

    10.31 ( Вхождения каждой цифры в строке )
    Напишите функцию, которая
    подсчитывает вхождения каждой цифры в строке

    author Protasenya Yulian
    email nasamalashfreak@gmail.com
    version 2025.2.2(EAP) 18.09.2025
    group 10701325
"""
s = input("Enter the string:")
lists = list(s)
list_s = set(lists)
for el in list_s:
    if ord(el) >= 48 and ord(el) <= 57:
        if(lists.count(el) > 1):
            print(f"{el} occurs {lists.count(el)} times")
        else:
            print(f"{el} occurs {lists.count(el)} time")