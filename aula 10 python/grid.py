from tkinter import *

box = Tk()
box.title('Grid')
box.geometry('500x500')

texto = Label(text='Digite seu nome : ', padx= 10, pady= 10)
texto.grid(row=0,column=0)

nome_input = Entry()
nome_input.grid(row=0, column=1)

texto_idade = Label(text='Digite sua idade : ')
texto_idade.grid(row=1,column=0)

idade_input = Entry()
idade_input.grid(row=1, column=1)

botao = Button(box,text='enviar' )
botao.grid(row=2,column=0, columnspan=2, pady=10)













box.mainloop()