"""
    source 9.2.py

    9.2 ( Создание калькулятора стоимости инвестиций )
        Напишите программу, которая рассчитывает будущую стоимость инвестиций
        при заданной процентной ставке

    author Protasenya Yulian
    email nasamalashfreak@gmail.com
    version 2025.2.2(EAP) 18.09.2025
    group 10701325
"""

import tkinter as tk
import tkinter.messagebox as msgbox


class EntryLabel(tk.Frame):
    def __init__(self, master: tk.Misc | None, labelText: str) -> None:
        super().__init__(master)

        self.label = tk.Label(self, text=labelText)
        self.__entry = tk.Entry(self, justify="right")

        self.label.pack(side="left")
        self.__entry.pack(side="right")


    def get(self) -> str:
        return self.__entry.get()


    def set(self, info: str) -> None:
        self.__entry.delete(0, tk.END)
        self.__entry.insert(0, info)


class InvestmentCalc(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        #Program Data

        #Program Settings
        self.title("Investment Calculator")
        self.geometry("315x150+760+350")
        self.resizable(False, False)

        #Main Window
        #Entered Data Frame
        infoFrame = tk.Frame(self)
        infoFrame.pack(anchor="nw")

        self.investmentAmountEntry = EntryLabel(infoFrame, "Investment Amount")
        self.yearsEntry = EntryLabel(infoFrame, "Years")
        self.interestRateEntry = EntryLabel(infoFrame, "Annual Interest Rate")

        self.investmentAmountEntry.pack(fill="x")
        self.yearsEntry.pack(fill="x")
        self.interestRateEntry.pack(fill="x")

        #Result Info Frame
        resultFrame = tk.Frame(infoFrame)
        resultFrame.pack(anchor="nw", fill="x")

        self.result = tk.DoubleVar(None)
        resultInfoLabel = tk.Label(resultFrame, text="Future Value")
        self.resultLabel = tk.Label(resultFrame, textvariable=self.result)

        resultInfoLabel.pack(side="left")
        self.resultLabel.pack(side="right")

        calculateBtn = tk.Button(infoFrame, text="Calculate", command=self.calculateFutureValue)
        calculateBtn.pack(side="right")

        self.mainloop()


    def calculateFutureValue(self):
        investmentAmount = self.investmentAmountEntry.get()
        years = self.yearsEntry.get()
        interestRate = self.interestRateEntry.get()

        for dataChunk in (investmentAmount, years, interestRate):
            newDataChunk = dataChunk.replace(".", "")

            if not (newDataChunk.isnumeric() or newDataChunk.isdigit()):
                msgbox.showwarning("Warning", f"The value \"{dataChunk}\" is invalid")
                return

        investmentAmount = float(investmentAmount)
        years = float(years)
        interestRate = float(interestRate)

        futureValue = round(investmentAmount * pow((1 + (interestRate / 12)), (years * 12)), 2)
        self.result.set(futureValue)
        self.resultLabel.configure(textvariable=self.result)


InvestmentCalc()