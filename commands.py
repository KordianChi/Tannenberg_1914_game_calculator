from tkinter import Label, Toplevel, Radiobutton, IntVar
from tkinter import Entry
from tkinter import Button
from tkinter import END
from random import randint
from constants import commands_table

class Commands(Toplevel):
    def __init__(self, parent):

        super().__init__(parent)
        self.title('Dowodzenie')
        self.geometry("300x260+100+100")
        
        self.prev_command = IntVar()
        self.prev_command.set(-1)
        
        self.prev_side_command_lbl = Label(self, text='Poprzednia tura:')
        self.prev_march_rb = Radiobutton(self, text='MARSZ',
                                    variable=self.prev_command, value=-1)
        self.prev_stop_rb = Radiobutton(self, text='STOP',
                                   variable=self.prev_command, value=1)
        
        self.command_effective = IntVar()
        self.command_effective.set(2)
        
        self.effective_lbl = Label(self, text='Efektywnosc Dowodcy:')
        self.active_eff_rb = Radiobutton(self, text='A',
                                    variable=self.command_effective, value=1)
        self.normal_eff_rb = Radiobutton(self, text='N',
                                   variable=self.command_effective, value=2)
        self.passive_eff_rb = Radiobutton(self, text='B',
                                   variable=self.command_effective, value=3)
        
        self.command_btn = Button(self, text='Dowodzenie',
                                  command=self.commands_calculate)
        
        self.command_result_lbl = Label(self, text='Wynik inicjatywy:')
        self.command_result_ent = Entry(self, width=12)
        
        self.command_result_ent.insert(END, '0')
        self.prev_side_command_lbl.place(x=30, y=20)
        self.prev_march_rb.place(x=130, y=20)
        self.prev_stop_rb.place(x=210, y=20)
        self.effective_lbl.place(x=30, y=70)
        self.active_eff_rb.place(x=160, y=70)
        self.normal_eff_rb.place(x=200, y=70)
        self.passive_eff_rb.place(x=240, y=70)
        self.command_btn.place(x=90, y=130, width=120, height=30)
        self.command_result_lbl.place(x=30, y=180)
        self.command_result_ent.place(x=150, y=180)
                
    def commands_calculate(self):
        
        dice_result = randint(1, 6)
        dice_result = dice_result + self.prev_command.get()
        command_result = commands_table[self.command_effective.get()][dice_result]
        
        if command_result:
            commands = f"MARSZ {dice_result}"
        else:
            commands = f"STOP {dice_result}"
            
        self.command_result_ent.delete(0, END)
        self.command_result_ent.insert(0, commands)