"""
    source 9.23.py

    9.23 ( Кнопки и переключатели )
        Напишите программу, которая использует переключатели для выбора цвета фона текста

    author Protasenya Yulian
    email nasamalashfreak@gmail.com
    version 2025.2.2(EAP) 18.09.2025
    group 10701325
"""

import tkinter as tk


class RBNB(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        #Program Data
        self.color = tk.IntVar()
        dx = 10

        #Program Settings
        self.title("Radio buttons and button")
        self.geometry("400x180+760+350")
        self.resizable(False, False)

        #Main Window
        pickColorFrame = tk.Frame(self)
        pickColorFrame.pack()

        for index in range(1, 5 + 1):
            btn = tk.Radiobutton(
                pickColorFrame,
                text=self.getColorById(index),
                value=index,
                variable=self.color,
                command=self.changeMsgColor
            )
            btn.grid(row=0, column=index)

        self.msgCanvas = tk.Canvas(self, bg="white", width=400, height=100)
        self.msgCanvas.create_text(200, 50, text="Welcome", tags="msg")
        self.msgCanvas.pack()

        btnFrame = tk.Frame(self)
        btnFrame.pack()

        btnLeft = tk.Button(btnFrame, text="<=", command=lambda: self.moveMsg(-dx, 0))
        btnRight = tk.Button(btnFrame, text="=>", command=lambda: self.moveMsg(dx, 0))

        btnLeft.grid(row=0, column=0)
        btnRight.grid(row=0, column=1)

        self.mainloop()

    def moveMsg(self, x, y):
        self.msgCanvas.move("msg", x, y)

    def getColorById(self, colorId: int):
        if colorId <= 0:
            return None

        colors = ["Red", "Yellow", "White", "Gray", "Green"]
        return colors[colorId - 1]

    def changeMsgColor(self):
        msg = self.msgCanvas.find_withtag("msg")[0]
        self.msgCanvas.itemconfig(msg, fill=self.getColorById(self.color.get()))


RBNB()