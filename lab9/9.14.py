"""
    source 9.14.py

    9.14 ( Рисование линий с помощью клавиш со стрелками )
        Напишите программу, которая рисует сегменты линий с помощью клавиш со стрелками

    author Protasenya Yulian
    email nasamalashfreak@gmail.com
    version 2025.2.2(EAP) 18.09.2025
    group 10701325
"""

import tkinter as tk


class ArrowKeys(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        #Program Data
        self.directions = {
            "Left": (-1, 0), "Right": (1, 0),
            "Up": (0, -1), "Down": (0, 1)
        }

        self.startPoint = (100, 100)
        self.currentPoint = self.startPoint

        #Program Settings
        self.title("Arrow Keys")
        self.geometry("200x200+760+350")
        self.resizable(False, False)

        self.bind("<Up>", self.moveTo)
        self.bind("<Down>", self.moveTo)
        self.bind("<Left>", self.moveTo)
        self.bind("<Right>", self.moveTo)

        #Main Window
        self.moveSpace = tk.Canvas(self, bg="white", width=200, height=200)
        self.moveSpace.pack()

        self.mainloop()


    def moveTo(self, event):
        direction = self.directions[event.keysym]
        moveMultiplier = 10

        x, y = direction
        x *= moveMultiplier
        y *= moveMultiplier

        x0, y0 = self.currentPoint
        newX, newY = self.sumVectors(self.currentPoint, (x, y))
        self.moveSpace.create_line(x0, y0, newX, newY)

        self.currentPoint = (newX, newY)


    def sumVectors(self, vec1: tuple, vec2: tuple) -> tuple:
        resVec = list()

        count = 0
        for coord1, coord2 in zip(vec1, vec2):
            resVec.append(coord1 + coord2)
            count += 1

        return tuple(resVec)


ArrowKeys()