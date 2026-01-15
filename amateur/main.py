import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title('Hangman Game')


dictionary={'king':'The fairy harlequinn',
            'diane':'The Queen of giants',
            'meliodas':'The demonking son',
            'elizabeth':'The supreme deity daughter',
            'merlin':'The mage of infinty',
            'gowther':'The doll of self discovery',
            'escanor':'The human powered by the sun'

}

def compare():
    data = entry.get()
    data2= dictionary.get(data,'!') + ' '
    label.config(text=f'{data2.lower()}',font=('Times New Roman',11,'bold'))




style =ttk.Style()
style.theme_use('clam')
#Frame for buttons
frame = ttk.Frame(root)
frame.pack()
#Entry field
entry = ttk.Entry(frame)
entry.pack()
#Button
button=ttk.Button(frame,text='Click',command=lambda:compare())
button.pack()
#label
label=ttk.Label(frame,padding=10)
label.pack(side='bottom')
root.mainloop()
