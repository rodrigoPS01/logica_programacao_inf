from tkinter import *

box = Tk()
box.title('Grid')
box.geometry('350x500')

visor = Entry(width=50)
visor.grid(row=0,column=0)

b1 = Button(box, text='C', width=40)
b1.grid(row=1,column=0, pady= 10 )

box.mainloop()