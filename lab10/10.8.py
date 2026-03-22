"""
    source 10.8.py

    10.8 (Find the index of the smallest element)
        Write a function that returns the index of
    the smallest element in a list of integers. If the number of such elements is greater than
    1, return the smallest index.
        Write a test program that prompts the user to enter a list of numbers, invokes this
    function to return the index of the smallest element, and displays the index.

    author Protasenya Yulian
    email nasamalashfreak@gmail.com
    version 2025.2.2(EAP) 18.09.2025
    group 10701325
"""

from math import *
from random import *

def indexOfSmallestElement():
    numbers = [int(i) for i in input("Enter numbers: ").split(' ')]
    index = 0
    el = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] < el:
            el = numbers[i]
            index = i
    print("The smallest element is",el)
    print("Index of smallest element is",index)
indexOfSmallestElement()


