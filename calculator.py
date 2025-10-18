from tkinter import Tk
from tkinter.ttk import Button
from initiative import Initiative


class Calculator(Tk):
    def __init__(self):
        super().__init__()

        self.geometry('300x250')
        self.title('Main Window')
        
        initiative_btn = Button(self, text='Inicjatywa',
                                  command=self.initiative, width=15)
        initiative_btn.place(x=50, y=50)
        
    def initiative(self):
        window = Initiative(self)
        window.grab_set()
            