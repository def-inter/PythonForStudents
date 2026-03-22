"""
    source 9.6.py

    9.6 ( Игра: покажите доску для крестиков-ноликов )
        Напишите программу, отображающую девять labels.
        На каждой метке может отображаться значок изображения для буквы X или значок изображения для буквы O

    author Protasenya Yulian
    email nasamalashfreak@gmail.com
    version 2025.2.2(EAP) 18.09.2025
    group 10701325
"""

import tkinter as tk
import random


class XNOGame(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        #Program Data
        self.redX = tk.PhotoImage(file="o.gif")
        self.greenMark = tk.PhotoImage(file="x.gif")

        #Program Settings
        self.title("XNO")
        self.geometry("310x305+760+350")
        self.resizable(False, False)

        #Main Window
        self.createGameDesk()
        self.mainloop()


    def createGameDesk(self):
        gameFrame = tk.Frame(self)
        gameFrame.pack()

        row, column = 0, 0
        for i in range(1, 9 + 1):
            game_choose = random.randint(0, 1)
            gameChooseLabel = tk.Label(gameFrame, borderwidth=0)

            if game_choose == 0:
                gameChooseLabel.configure(image=self.greenMark)
            else:
                gameChooseLabel.configure(image=self.redX)

            gameChooseLabel.grid(row=row, column=column)

            column += 1
            if i % 3 == 0:
                row += 1
                column = 0


XNOGame()