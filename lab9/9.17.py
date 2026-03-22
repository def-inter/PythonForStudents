"""
    source 9.17.py

    9.17 ( Гоночный автомобиль )
    Напишите программу, моделирующую автомобильные гонки. Автомобиль движется слева направо.
    Когда он достигает правого конца, он перезапускается слева и продолжает тот же процесс.
    Позвольте пользователю увеличивать и уменьшать скорость автомобиля, нажимая клавиши со стрелками вверх и вниз

    author Protasenya Yulian
    email nasamalashfreak@gmail.com
    version 2025.2.2(EAP) 18.09.2025
    group 10701325
"""

import tkinter as tk


class CarRace(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        # Program Data
        self.canvasWidth, self.canvasHeight = 400, 100
        self.rBorder, self.lBorder = 340, 9

        self.dx = 10
        self.acc = 0

        # Program Settings
        self.title("Racing Car")
        self.geometry(f"{self.canvasWidth}x{self.canvasHeight}+760+350")
        self.resizable(False, False)

        self.bind("<Up>", self.accIncrease)
        self.bind("<Down>", self.accDecrease)


        # Main Window
        self.raceContainer = tk.Canvas(self, bg="white", width=self.canvasWidth, height=self.canvasHeight)
        self.raceContainer.pack()

        self.createCarAt(x0=self.dx, y0=self.canvasHeight - 10)
        self.startMoveAnimation()

        self.mainloop()


    def accIncrease(self, event):
        self.acc += 1


    def accDecrease(self, event):
        self.acc -= 1


    def createCarAt(self, x0 = 0, y0 = 0):
        #Body
        self.raceContainer.create_rectangle(x0, y0 - 10, x0 + 50, y0 - 20, fill="black", tags="part")

        #Roof
        self.raceContainer.create_polygon(
            [
                x0 + 10, y0 - 20, x0 + 20, y0 - 30,
                x0 + 30, y0 - 30, x0 + 40, y0 - 20
            ], fill="gray", tags="part"
        )

        #Wheels
        self.raceContainer.create_oval(x0 + 10, y0, x0 + 20, y0 - 10, fill="gray", tags="part")
        self.raceContainer.create_oval(x0 + 30, y0, x0 + 40, y0 - 10, fill="gray", tags="part")


    def startMoveAnimation(self):
        if self.dx <= self.rBorder:
            self.dx += 1 * 0.1 * self.acc
        else:
            self.dx = 10

        if self.dx < self.lBorder:
            self.dx = self.rBorder

        self.raceContainer.delete("all")
        self.createCarAt(x0=self.dx, y0=self.canvasHeight - 10)
        self.after(10, self.startMoveAnimation)


CarRace()