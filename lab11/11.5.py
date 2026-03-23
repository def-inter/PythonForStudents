import math
from tkinter import *
class Cell:
    def __int__(self):
        pass

class Game:
    def __init__(self):
        window = Tk()
        window.title("Tic-Tac-Toe")
        window.geometry("400x400+550+280")

        self.oImage = PhotoImage(file='o.gif')
        self.xImage = PhotoImage(file='x.gif')
        self.emptyImage = PhotoImage(file='empty.gif')

        self.frame = Frame(window, height=400, width=400)
        self.frame.pack()

        self.canvases = []
        self.current_player = "X"
        self.list = [[0,0,0],[0,0,0],[0,0,0]]
        self.count = 0
        for i in range(3):
            for j in range(3):
                cell = Frame(self.frame)
                cell.grid(row=i, column=j, padx=4, pady=4)

                canvas = Canvas(cell, width=104, height=104, bg='white')
                canvas.pack()

                canvas.create_image(52, 52, image=self.emptyImage, tags=f"img_{i}_{j}")
                canvas.image = self.emptyImage

                # Привязываем клик
                canvas.bind("<Button-1>", lambda e, r=i, c=j: self.on_click(r, c))

                self.canvases.append((canvas, i, j))

        self.status_label = Label(window, text='Ход X', font=('Arial', 14))
        self.status_label.pack()

        window.mainloop()

    def on_click(self, row, col):
        for canvas, i, j in self.canvases:
            if i == row and j == col:
                current_image = canvas.image


                if current_image == self.emptyImage:
                    if self.current_player == "X":
                        canvas.itemconfig(f"img_{i}_{j}", image=self.xImage)
                        canvas.image = self.xImage
                        self.current_player = "O"
                        self.status_label.config(text='Ход O')
                        self.list[i][j] = 10
                    else:
                        canvas.itemconfig(f"img_{i}_{j}", image=self.oImage)
                        canvas.image = self.oImage
                        self.current_player = "X"
                        self.status_label.config(text='Ход X')
                        self.list[i][j] = 1
        self.count += 1
        for i in range(3):
            if self.list[i][0] + self.list[i][1] +self.list[i][2] == 3 :
                self.status_label.config(text='Выйграли O')
            if self.list[i][0] + self.list[i][1] +self.list[i][2]== 30 :
                self.status_label.config(text='Выйграли X')
        for i in range(3):
            if self.list[0][i] + self.list[1][i] +self.list[2][i] == 3 :
                self.status_label.config(text='Выйграли O')
            if self.list[0][i] + self.list[1][i] +self.list[2][i] == 30 :
                self.status_label.config(text='Выйграли X')
        if self.list[0][0] + self.list[1][1] + self.list[2][2] == 3 :
            self.status_label.config(text='Выйграли O')
        elif self.list[0][0] + self.list[1][1] + self.list[2][2] == 30 :
            self.status_label.config(text='Выйграли X')
        if self.list[2][0] + self.list[1][1] + self.list[0][2] == 3 :
            self.status_label.config(text='Выйграли O')
        elif self.list[2][0] + self.list[1][1] + self.list[0][2] == 30 :
            self.status_label.config(text='Выйграли X')

Game()