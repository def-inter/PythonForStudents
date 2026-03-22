"""
    source 9.15.py

    9.15 ( Отображение вентилятора )
        Напишите программу, которая отображает вентилятор

    author Protasenya Yulian
    email nasamalashfreak@gmail.com
    version 2025.2.2(EAP) 18.09.2025
    group 10701325
"""

import tkinter as tk


class FanProgram(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        #Program Data
        canvasWidth, canvasHeight = 400, 400
        self.center = (canvasWidth // 2, canvasHeight // 2)

        #Program Settings
        self.title("Fan")
        self.geometry("400x400+760+350")
        # self.resizable(False, False)

        #Main Window
        self.fanCanvas = tk.Canvas(self, bg="white", width=canvasWidth, height=canvasHeight)
        self.fanCanvas.pack()
        self.createFan()

        self.mainloop()


    def createFan(self):
        x0, y0 = self.center
        wings = {
            "topWing": [(x0, y0), (x0 - 40, y0 - 110), (x0 + 40, y0 - 110)],
            "botWing": [(x0, y0), (x0 - 40, y0 + 110), (x0 + 40, y0 + 110)],
            "leftWing": [(x0, y0), (x0 - 110, y0 + 40), (x0 - 110, y0 - 40)],
            "rightWing": [(x0, y0), (x0 + 110, y0 + 40), (x0 + 110, y0 - 40)],
        }

        for wingCoords in wings.values():
            self.createWing(wingCoords)


    def createWing(self, wingCoords: list[tuple]):
        self.fanCanvas.create_polygon(wingCoords, fill="gray", outline="black")


    def sumVectors(self, vec1: tuple, vec2: tuple) -> tuple:
        resVec = list()

        count = 0
        for coord1, coord2 in zip(vec1, vec2):
            resVec.append(coord1 + coord2)
            count += 1

        return tuple(resVec)


FanProgram()