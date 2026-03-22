"""
    source 9.12-2.py

    9.13.2 ( Отображение положения мыши )
        Напишите программу, которая отображает положение мыши при нажатии кнопки мыши
        и перестает отображать ее при нажатии кнопки мыши

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

        self.bind("<ButtonPress>", self.onButtonPress)
        self.bind("<ButtonRelease>", self.onButtonRelease)
        self.bind("<B1-Motion>", self.onMotion)

        #Main Window
        self.messageFrame = tk.Frame(self)
        self.messageLabel = tk.Label(self.messageFrame)

        self.mainloop()

    def onMotion(self, event):
        x, y = event.x, event.y
        self.messageFrame.place_forget()
        self.messageLabel.pack_forget()

        self.messageLabel.configure(text=f"({x}, {y})")
        self.messageFrame.place(x=(x - 45), y=(y - 25))
        self.messageLabel.pack()


    def onButtonPress(self, event):
        if event.num != 1:
            return

        x, y = event.x, event.y
        self.messageLabel.configure(text=f"({x}, {y})")

        self.messageFrame.place(x=(x - 45), y=(y - 25))
        self.messageLabel.pack()


    def onButtonRelease(self, event):
        if event.num != 1:
            return

        self.messageFrame.place_forget()
        self.messageLabel.pack_forget()


MousePosition()