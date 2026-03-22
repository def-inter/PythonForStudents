"""
    source 9.13-1.py

    9.13.1 ( Отображение положения мыши )
        Напишите программу, которая отображает положение мыши при нажатии кнопки мыши

    author Protasenya Yulian
    email nasamalashfreak@gmail.com
    version 2025.2.2(EAP) 18.09.2025
    group 10701325
"""

import tkinter as tk


class MousePosition(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        #Program Data
        self.appearDelay = 1000

        #Program Settings
        self.title("Mouse Position")
        self.geometry("200x200+760+350")
        self.resizable(False, False)

        self.bind("<Button-1>", self.onButtonClick)

        #Main Window
        self.messageFrame = tk.Frame(self)
        self.messageLabel = tk.Label(self.messageFrame)

        self.mainloop()


    def onButtonClick(self, event):
        x, y = event.x, event.y
        self.messageLabel.configure(text=f"({x}, {y})")

        self.messageFrame.place(x=(x - 45), y=(y - 25))
        self.messageLabel.pack()

        self.after(self.appearDelay, self.messageLabel.pack_forget)
        self.after(self.appearDelay, self.messageFrame.place_forget)


MousePosition()