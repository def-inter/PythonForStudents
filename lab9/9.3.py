"""
    source 9.3.py

    9.3 ( Выбор геометрических фигур )
        Напишите программу, рисующую прямоугольник или овал. Пользователь выбирает
        цифру с помощью переключателя и указывает, заполнена ли она, нажав кнопку проверки.

    author Protasenya Yulian
    email nasamalashfreak@gmail.com
    version 2025.2.2(EAP) 18.09.2025
    group 10701325
"""

import tkinter as tk


class RadNCheckButtons(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        #Program Data
        self.canvasWidth = 500
        self.canvasHeight = 100

        #Program Settings
        self.title("Radio and Check buttons")
        self.geometry("600x150+760+350")
        self.resizable(False, False)

        #Main Window
        self.drawingCanvas = tk.Canvas(self, bg="white", width=self.canvasWidth, height=self.canvasHeight)
        self.canvasObject = 0
        self.drawingCanvas.pack()

        btnsFrame = tk.Frame(self)
        btnsFrame.pack()

        self.figureType = tk.IntVar()
        rbDrawOval = tk.Radiobutton(btnsFrame, text="Oval", value=1, variable=self.figureType, command=self.processRBtn)
        rbDrawRectangle = tk.Radiobutton(btnsFrame, text="Rectangle", value=2, variable=self.figureType, command=self.processRBtn)

        self.isFilled = tk.BooleanVar()
        cbFillFigure = tk.Checkbutton(btnsFrame, text="Filled",variable=self.isFilled, command=self.processCBtn)

        rbDrawRectangle.grid(row=0, column=0)
        rbDrawOval.grid(row=0, column=1)
        cbFillFigure.grid(row=0, column=2)

        self.mainloop()


    def processRBtn(self):
        self.drawingCanvas.delete("all")

        match self.figureType.get():
            case 1:
                self.canvasObject = self.drawingCanvas.create_oval(2, 3, self.canvasWidth - 3, self.canvasHeight - 1)
            case 2:
                self.canvasObject = self.drawingCanvas.create_rectangle(2, 3, self.canvasWidth - 3, self.canvasHeight - 1)

        self.fillColor()


    def fillColor(self):
        if self.canvasObject == 0:
            return

        if self.isFilled.get():
            self.drawingCanvas.itemconfig(self.canvasObject, fill="gray")
        else:
            self.drawingCanvas.itemconfig(self.canvasObject, fill="white")


    def processCBtn(self):
        self.fillColor()


RadNCheckButtons()