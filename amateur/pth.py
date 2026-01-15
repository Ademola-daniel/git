import tkinter as tk
from tkinter import ttk

dic={'king':'The one who will save you from yourself',
     'queen':'The one who will save the children from predators',
     'knight':'The one who has sworn allegiance to the kingdom'}


def Hil():

    data= entry.get()

    data2=dic.get(data,'something')
    label.config(text=f'{data2}')




root = tk.Tk()
root.config(bg='black')
root.title('A Game')
root.geometry()
#style
style=ttk.Style(root)
style.theme_use('clam')
#entry field
entry=ttk.Entry(root)
entry.pack()

#Button
button=ttk.Button(root,text='Click',command=lambda:Hil())
button.pack()
#label
label=ttk.Label(root,text='LABEL')
label.pack()


root.mainloop()
