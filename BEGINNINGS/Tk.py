from tkinter import *
import tkinter.messagebox

root =Tk()
tkinter.messagebox.showinfo('Warning','Please make sure you are 18 years old')

askdata=tkinter.messagebox.askquestion('Askdata','Are you human')
if askdata=='yes':
    print('welcome')
else:
    print('You are not permitted by the organisation guidelines to have access to this site')
