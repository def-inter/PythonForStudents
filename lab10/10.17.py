"""
    source 10.17.py

    **10.17 ( Анаграммы )
    Напишите функцию, которая проверяет, являются ли два
    слова анаграммами.

    author Protasenya Yulian
    email nasamalashfreak@gmail.com
    version 2025.2.2(EAP) 18.09.2025
    group 10701325
"""
s1 = input("Enter the first word: ")
s2 = input("Enter the second word: ")
lists1 = list(s1)
lists2 = list(s2)

list_s1 = [word.lower() for word in lists1]
list_s2 = [word.lower() for word in lists2]

def sort_string(list_s):
    count = 0
    while count != len(list_s) - 1:
        count = 0
        for i in range(len(list_s) - 1):
            if list_s[i] < list_s[i + 1]:
                list_s[i], list_s[i + 1] = list_s[i + 1], list_s[i];
            else:
                count += 1
sort_string(list_s1)
sort_string(list_s2)
if(list_s1 == list_s2):
    print(f"{s1} and {s2} are anagrams")
else:
    print(f"{s1} and {s2} aren't anagrams")
