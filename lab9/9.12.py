"""
    source 9.12.py

    9.12 ( Чередовать два сообщения )
        Напишите программу, которая будет переключаться щелчком левой кнопки мыши между двумя сообщениями,
        отображаемыми на canvas: «Programming is fun» и «It is fun to program»

    author Protasenya Yulian
    email nasamalashfreak@gmail.com
    version 2025.2.2(EAP) 18.09.2025
    group 10701325
"""

import tkinter as tk


class RotatingMessage(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        #Program Data
        self.messages = ("Programming is fun", "It is fun to program")
        self.choice = 0

        #Program Settings
        self.title("Rotating Message")
        self.geometry("200x200+760+350")
        self.resizable(False, False)

        self.bind("<Button-1>", self.onButtonClick)

        #Main Window
        textFrame = tk.Frame(self)
        textFrame.pack(expand=True)

        self.messageLabel = tk.Label(textFrame, text=self.messages[self.choice])
        self.messageLabel.pack()

        self.mainloop()


    def onButtonClick(self, event):
        self.choice = 1 if self.choice == 0 else 0
        self.messageLabel.configure(text=self.messages[self.choice])


RotatingMessage()