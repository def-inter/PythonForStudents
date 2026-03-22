"""
    source 9.5.py

    9.5 ( Игра: отображение шахматной доски )
        Напишите программу, отображающую шахматную доску,
        в которой каждая белая и черная клетка представляет собой холст с черным или белым фоном

    author Protasenya Yulian
    email nasamalashfreak@gmail.com
    version 2025.2.2(EAP) 18.09.2025
    group 10701325
"""

import tkinter as tk


class ChessDesk(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        #Program Data
        self.canvasWidth = 400
        self.canvasHeight = 400

        #Program Settings
        self.title("Displaying a Checkerboard")
        self.geometry("400x400+760+350")
        # self.resizable(False, False)

        #Main Window
        self.drawingCanvas = tk.Canvas(self, bg="white", width=self.canvasWidth, height=self.canvasHeight)
        self.drawingCanvas.pack()
        self.creteDesk()

        self.mainloop()


    def creteDesk(self):
        row, column = 0, 0

        for i in range(1, 64 + 1):
            if (row + column) % 2 == 0:
                color = "white"
            else:
                color = "black"

            self.createDeskSquare(column * 50, row * 50, color)

            column += 1
            if i % 8 == 0:
                row += 1
                column = 0


    def createDeskSquare(self, x0: int, y0: int, color: str):
        segmentWidth = 400 // 8
        self.drawingCanvas.create_rectangle(x0, y0, x0+segmentWidth, y0+segmentWidth, fill=color)


ChessDesk()