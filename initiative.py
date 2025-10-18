from tkinter import Label, Toplevel, Radiobutton, BooleanVar
from tkinter import Entry
from tkinter import Button
from tkinter import END
from tkinter.ttk import Checkbutton
from random import randint


class Initiative(Toplevel):
    def __init__(self, parent):

        super().__init__(parent)
        self.title('Inicjatywa')
        self.geometry("300x260+100+100")
        
        self.prev_side_init = BooleanVar()
        self.prev_side_init.set(True)
        
        self.prev_side_init_lbl = Label(self, text='Poprzednia tura:')
        self.russians = Radiobutton(self, text='Rosjanie',
                                    variable=self.prev_side_init, value=False)
        self.germans = Radiobutton(self, text='Niemcy',
                                   variable=self.prev_side_init, value=True)

        self.russians_retreat_lbl = Label(self, text='Ucieczki rosyjskie:')
        self.russians_retreat_ent = Entry(self, width=7)
        self.russians_retreat_ent.insert(END, '0')
        
        self.russians_losses_lbl = Label(self, text='Straty rosyjskie:')
        self.russians_losses_ent = Entry(self, width=7)
        self.russians_losses_ent.insert(END, '0')

        self.germans_retreat_lbl = Label(self, text='Ucieczki niemieckie:')
        self.germans_retreat_ent = Entry(self, width=7)
        self.germans_retreat_ent.insert(END, '0')

        self.germans_losses_lbl = Label(self, text='Straty niemieckie:')
        self.germans_losses_ent = Entry(self, width=7)
        self.germans_losses_ent.insert(END, '0')

        self.hindenburg = BooleanVar()
        self.hindenburg.set(False)
        self.hindenburg_chk = Checkbutton(self, text='Hindenburg',
                                          variable=self.hindenburg)

        self.initiative_btn = Button(self, text='Inicjatywa',
                                  command=self.calculate_initiative)
        
        self.initiatve_result_lbl = Label(self, text='Wynik inicjatywy:')
        self.initiatve_result_ent = Entry(self, width=12)
        self.initiatve_result_ent.insert(END, '0')
        
        self.russians.place(x=120, y=10)
        self.germans.place(x=200, y=10)
        self.prev_side_init_lbl.place(x=30, y=10)
        
        self.russians_retreat_lbl.place(x=30, y=40)
        self.russians_retreat_ent.place(x=180, y=40)

        self.russians_losses_lbl.place(x=30, y=70)
        self.russians_losses_ent.place(x=180, y=70)

        self.germans_retreat_lbl.place(x=30, y=100)
        self.germans_retreat_ent.place(x=180, y=100)

        self.germans_losses_lbl.place(x=30, y=130)
        self.germans_losses_ent.place(x=180, y=130)

        self.hindenburg_chk.place(x=30, y=160)

        self.initiative_btn.place(x=30, y=190)
        
        self.initiatve_result_lbl.place(x=30, y=220)
        self.initiatve_result_ent.place(x=180, y=220)
        
    def calculate_initiative(self):
    
        while(True):
        
            germans_result = randint(1, 6)
            if self.hindenburg.get():
                germans_result = germans_result + randint(1, 6)
            germans_result = germans_result + int(self.russians_retreat_ent.get())
            germans_result = germans_result + int(self.russians_losses_ent.get())
            
            russians_result = randint(1, 6)
            russians_result = russians_result + int(self.germans_retreat_ent.get())
            russians_result = russians_result + int(self.germans_losses_ent.get())
            
            if(self.prev_side_init.get()):
                germans_result = germans_result + 1
            else:
                russians_result = russians_result + 1
            
            if germans_result > russians_result:
                winner = f"Niemcy ({germans_result}:{russians_result})"
                break
            elif russians_result > germans_result:
                winner = f"Rosjanie ({russians_result}:{germans_result})"
                break
    
        self.initiatve_result_ent.delete(0, END)
        self.initiatve_result_ent.insert(0, winner)
                
            
                
            
