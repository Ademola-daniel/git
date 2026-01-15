from tkinter import *
dictionary={'the': 'Theous',
            'king':'is',
            'is here':'here'}
def clear():
    entry.delete(0,END)




def here():
    output=' '
    data = entry.get()
    data2=data.split(' ')
    for i in data2:
        output+=dictionary.get(i,'!')+ ' '
        clear()
    entry.insert(0,output)


root=Tk()
root.title('My project')
root.resizable(width=False,height=False)
#Entry field
entry=Entry(root)
entry.pack()
label=Label(root,text='The one who will come',fg='Black')
label.pack()
button=Button(root,text='click',fg='black',command=here)
button.pack()
root.mainloop()
