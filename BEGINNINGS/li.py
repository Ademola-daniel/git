from tkinter import *
class First:
    def __init__(self,rootone):
        frame = Frame(rootone)
        frame.pack()

        button = Button(frame,text = 'Click',command=self.printmessage)
        button.pack()

        button2 = Button(frame,text ='click',fg='Blue',command=frame.quit)
        button2.pack(side=LEFT)


    def printmessage(self):
        print('who the hell do you think you are')

root = Tk()
def printmessage():
    print('who the hell do you think you are')


menu = Menu(root)
root.config(menu=menu)

submenu=Menu(menu)
submenu2=Menu(menu)

menu.add_cascade(label='File',menu =submenu)
submenu.add_command(label='intro',command=printmessage)
submenu.add_separator()
submenu.add_command(label='progress',command=printmessage)
menu.add_cascade(label='Home',menu=submenu2)
submenu2.add_command(label='Story',command=printmessage)

toolbar = Frame(root,bg ='Black')
firstbutton = Button(toolbar,text='Save',command=printmessage)
secondbutton=Button(toolbar,text='Print', command= printmessage)

firstbutton.pack(side = LEFT,padx=2,pady=3)
secondbutton.pack(side = LEFT,padx=2,pady=3)
toolbar.pack(side=TOP, fill =X)

status= Label(root,text='Status bar',bd=1,relief =SUNKEN)
status.pack(side=BOTTOM,fill=X)
root.mainloop()
