'''
This program tests for the confirm-to-delete message.
- button to delete (delete button function leads to message box)
- prompts message

notes:
- selecting "No" prompts nothing (which is intended)
- "Yes" should prompt delete function
- could likely be more refined, but it does its function
'''

from tkinter import *
from tkinter import ttk
from tkinter import messagebox  # yep

mono = Tk()  # switching it up slightly


# functions
def messagebox1():  # first parameter will be title then txt
    mbox = messagebox.askquestion("Confirm Deletion", "Do you wish to delete this row?")
    if mbox == 'yes':
        print('[ insert function name ] ')  # realistically, you'd execute the delete function here

# delete button
delete = Button(mono, text="Delete Row", command=messagebox1).grid(row=0, column=0)


mono.geometry("163x153")  # tiny
mono.mainloop()