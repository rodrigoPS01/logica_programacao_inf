from tkinter import *

def saudacao():
    nome_digitado = texto_input.get()
    resposta.configure(text=f'Seja bem vindo, {nome_digitado}!')

box = Tk()
box.title('Revisão')
box.geometry('500x500')

texto = Label(text='Digite seu nome: ', bg= 'black', fg= 'white')
texto.pack()

texto_input = Entry()
texto_input.pack()

button = Button(box, text= 'Enter', command=saudacao)
button.pack()

resposta = Label(text= ''  )
resposta.pack()






box.mainloop()