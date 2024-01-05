from tkinter import *

def media():
    n1 = float(nota1.get())
    n2 = float(nota2.get())
    n3 = float(nota3.get())
    s = (n1 + n2 + n3)/3
    if s < 7:
        resposta.configure(text=f'Você foi Reprovado, com media {s}', bg='red')
    elif s > 7 and s <10:
        resposta.configure(text=f'Você foi Aprovado, com media {s}', bg='green')
    elif s == 10:
        resposta.configure(text=f'Você foi Aprovado com distinção, com media {s}', bg='blue', fg='white')


box = Tk()
box.title('Notas')
box.geometry('500x500')

Texto = Label(text='Digite as sua 1° nota no espaço abaixo: ', bg='#F9E4B7', fg='black')
Texto.pack()

nota1 = Entry()
nota1.pack()

Texto2 = Label(text='Digite as sua 2° nota no espaço abaixo: ', bg='#F9E4B7', fg='black')
Texto2.pack()

nota2 = Entry()
nota2.pack()

Texto3 = Label(text='Digite as sua 3° nota no espaço abaixo: ', bg='#F9E4B7', fg='black')
Texto3.pack()

nota3 = Entry()
nota3.pack()

button = Button(box, text='Enter', command=media)
button.pack()

resposta = Label(text= '')
resposta.pack()

box.mainloop()