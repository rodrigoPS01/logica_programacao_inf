from tkinter import *

box = Tk()
box.title('Place')
box.geometry('500x500')

texto = Label(text='Digite seu nome: ')
texto.place(x=15, y=10)

nome_input = Entry()
nome_input.place(x=110, y=12 )

texto_idade = Label(text='Digite sua idade: ')
texto_idade.place(x=15, y=40)

idade_input = Entry()
idade_input.place(x=110, y=42 )

botao = Button(box, text='enviar', width=30)
botao.place(x=15, y=75)









box.mainloop()