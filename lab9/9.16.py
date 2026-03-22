"""
    source 9.16.py

    9.16 ( Отображение работающего вентилятора )
        Напишите программу, которая отображает работающий вентилятор

    author Protasenya Yulian
    email nasamalashfreak@gmail.com
    version 2025.2.2(EAP) 18.09.2025
    group 10701325
"""

import tkinter as tk
import math


class FanProgram(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        # Program Data
        canvasWidth, canvasHeight = 400, 400
        self.center = (canvasWidth // 2, canvasHeight // 2)

        # Program Settings
        self.title("Fan")
        self.geometry("400x400+760+350")
        self.resizable(False, False)

        # Main Window
        self.fanCanvas = tk.Canvas(self, bg="white", width=canvasWidth, height=canvasHeight)
        self.fanCanvas.pack()

        self.fan = self.createFan()
        self.startFanAnimation(speed=30)

        self.mainloop()


    def startFanAnimation(self, speed: int = 50, frequency: float = 0.1):
        for blade in self.fan:
            coords = self.fanCanvas.coords(blade)

            newCoords = []
            for i in range(0, len(coords), 2):
                x = coords[i]
                y = coords[i + 1]

                xRel = x - self.center[0]
                yRel = y - self.center[1]

                xRot = xRel * math.cos(frequency) - yRel * math.sin(frequency)
                yRot = xRel * math.sin(frequency) + yRel * math.cos(frequency)

                xNew = xRot + self.center[0]
                yNew = yRot + self.center[1]

                newCoords.extend([xNew, yNew])

                self.fanCanvas.coords(blade, *newCoords)

        self.after(speed, self.startFanAnimation, speed, frequency)


    def createFan(self):
        x0, y0 = self.center
        fanBladeIds = list()

        fanBladesSettings = {
            "topWing": [(x0, y0), (x0 - 40, y0 - 110), (x0 + 40, y0 - 110)],
            "botWing": [(x0, y0), (x0 - 40, y0 + 110), (x0 + 40, y0 + 110)],
            "leftWing": [(x0, y0), (x0 - 110, y0 + 40), (x0 - 110, y0 - 40)],
            "rightWing": [(x0, y0), (x0 + 110, y0 + 40), (x0 + 110, y0 - 40)],
        }

        for wingCoords in fanBladesSettings.values():
            fanBladeIds.append(self.createWing(wingCoords))

        return fanBladeIds


    def createWing(self, wingCoords: list):
        return self.fanCanvas.create_polygon(wingCoords, fill="gray", outline="black", tags="fanBlade")


FanProgram()