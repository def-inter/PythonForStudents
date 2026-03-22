"""
    source 9.25.py

    9.25 ( Светофоры )
        Напишите программу, имитирующую светофор.
        Программа позволяет пользователю выбрать один из трех индикаторов: красный, желтый или зеленый

    author Protasenya Yulian
    email nasamalashfreak@gmail.com
    version 2025.2.2(EAP) 18.09.2025
    group 10701325
"""

import tkinter as tk


class TrafficLights(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        #Program Data
        self.colors = ["Red", "Yellow", "Green"]
        self.color = tk.IntVar()

        #Program Settings
        self.title("Traffic Lights")
        self.geometry("300x350+760+350")
        self.resizable(False, False)

        #Main Window
        self.sCanvas = tk.Canvas(self, bg="white", width=300, height=300)
        self.sCanvas.pack()

        self.createTrafficLighter()

        pickColorFrame = tk.Frame(self)
        pickColorFrame.pack()

        for index in range(1, 3 + 1):
            btn = tk.Radiobutton(
                pickColorFrame,
                text=self.getColorById(index),
                value=index,
                variable=self.color,
                command=self.lightPartOfTrafficLighter
            )
            btn.grid(row=0, column=index)



        self.mainloop()

    def createTrafficLighter(self):
        sRadius = 45
        x0 = 150

        self.sCanvas.create_rectangle(x0 - sRadius, 290, x0 + sRadius, 10)

        for i in range(3):
            dy = 2 * sRadius + 5
            self.sCanvas.create_oval(
                x0 - sRadius, 290 - i * dy,
                x0 + sRadius, 290 - 2 * sRadius - i * dy,
                tags=self.getColorById(i + 1)
            )

    def lightPartOfTrafficLighter(self):
        for color in self.colors:
            self.sCanvas.itemconfig(color, fill="white")

        color = self.getColorById(self.color.get())
        self.sCanvas.itemconfig(color, fill=color)


    def getColorById(self, colorId: int):
        if colorId <= 0:
            return None

        return self.colors[colorId - 1]



TrafficLights()