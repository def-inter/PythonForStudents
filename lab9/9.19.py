"""
    source 9.19.py

    9.19 ( Перемещение круга с помощью клавиш )
        Напишите программу, которая перемещает круг вверх, вниз, влево или вправо с помощью клавиш со стрелками

    author Protasenya Yulian
    email nasamalashfreak@gmail.com
    version 2025.2.2(EAP) 18.09.2025
    group 10701325
"""

import tkinter as tk
import tkinter.messagebox as msgbox

class CircleMover(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        #Program Data
        self.currentPos = (100, 100)
        self.radius = 20

        dx, dy = 10, 10
        self.directions = {
            "Left": (-dx, 0), "Right": (dx, 0),
            "Up": (0, -dy), "Down": (0, dy)
        }

        #Program Settings
        self.title("Moving Circle")
        self.geometry("500x250+760+350")
        self.resizable(False, False)

        self.bind("<Up>", self.moveTo)
        self.bind("<Down>", self.moveTo)
        self.bind("<Left>", self.moveTo)
        self.bind("<Right>", self.moveTo)

        #Main Window
        self.ballFieldCanvas = tk.Canvas(self, bg="white", width=500, height=200)
        self.ballFieldCanvas.pack()
        self.ball = self.createBall(100, 100, self.radius)

        self.mainloop()


    def canMoveTo(self, offsetX: int, offsetY: int) -> bool:
        newPos = (self.currentPos[0] + offsetX, self.currentPos[1] + offsetY)
        moveX, moveY = newPos

        if offsetX != 0:
            moveX += (offsetX / abs(offsetX)) * self.radius

        if offsetY != 0:
            moveY += (offsetY / abs(offsetY)) * self.radius

        condition = (0 <= moveX <= 500) and (0 <= moveY <= 200)
        if condition:
            self.currentPos = newPos

        return condition


    def moveTo(self, event) -> None:
        direction = event.keysym
        offsetX, offsetY = self.directions[direction]

        if not self.canMoveTo(offsetX, offsetY):
            msgbox.showwarning("Restriction", f"You cant move {direction.lower()}")
            return

        self.ballFieldCanvas.move(self.ball, offsetX, offsetY)
        self.ballFieldCanvas.update()


    def createBall(self, x: int, y: int, r: int) -> int:
        ball = self.ballFieldCanvas.create_oval(
            x - r, y - r, x + r, y + r,
            outline="gray"
        )

        return ball


CircleMover()