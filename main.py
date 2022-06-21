from tkinter import *
from tkinter import Tk
from turtle import color

# cores

cor1 = "#1e1f1e" # preto
cor2 = "#ffffff" # branco
cor3 = "#38576b" # azul
cor4 = "#404040" # cinza
cor5 = "#FFAB40" # laranja

janela = Tk()
janela.title('Calculadora')
janela.geometry("235x310")
janela.config(bg=cor1)

# frames
frame_tela = Frame(janela, width=235, height=50, bg=cor1)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268, bg=cor3)
frame_corpo.grid(row=1, column=0)


# variavel todos valores

todos_valores = ''
valor_texto = StringVar()

#criando funcao

def digita_valor(event):
    
    global todos_valores
    
    todos_valores =todos_valores + str(event)

    #mostra o valor na tela
    
    valor_texto.set(todos_valores)

# funcao para calcular

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    
    valor_texto.set(str(resultado))

# funcao limpa tela

def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")

# criando label

app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=cor1, fg=cor2)
app_label.place(x=0,y=0)

#botoes

b_1 = Button(frame_corpo, command=limpar_tela, text="C", width=11, height=2, bg=cor2, font=('Ivy 13 bold'), relief=GROOVE, overrelief=FLAT)
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo, command= lambda: digita_valor('%'),text="%", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=GROOVE, overrelief=FLAT)
b_2.place(x=120, y=0)
b_3 = Button(frame_corpo, command=lambda: digita_valor('/'), text="/", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=GROOVE, overrelief=FLAT)
b_3.place(x=180, y=0)

b_4 = Button(frame_corpo, command= lambda: digita_valor('7'), text="7",width=5, height=2, bg=cor2, font='Ivy 13 bold', relief=GROOVE, overrelief=FLAT)
b_4.place(x=0, y=52)
b_5 = Button(frame_corpo, command= lambda: digita_valor('8'), text="8",width=5, height=2, bg=cor2, font='Ivy 13 bold', relief=GROOVE, overrelief=FLAT)
b_5.place(x=60, y=52)
b_6 = Button(frame_corpo, command= lambda: digita_valor('9'), text="9",width=5, height=2, bg=cor2, font='Ivy 13 bold', relief=GROOVE, overrelief=FLAT)
b_6.place(x=120, y=52)
b_7 = Button(frame_corpo, command= lambda: digita_valor('*'), text="*",width=5, height=2, bg=cor5, fg=cor2, font='Ivy 13 bold', relief=GROOVE, overrelief=FLAT)
b_7.place(x=180, y=52)

b_8 = Button(frame_corpo, command= lambda: digita_valor('4'), text="4",width=5, height=2, bg=cor2, font='Ivy 13 bold', relief=GROOVE, overrelief=FLAT)
b_8.place(x=0, y=104)
b_9 = Button(frame_corpo, command= lambda: digita_valor('5'),text="5",width=5, height=2, bg=cor2, font='Ivy 13 bold', relief=GROOVE, overrelief=FLAT)
b_9.place(x=60, y=104)
b_10 = Button(frame_corpo, command= lambda: digita_valor('6'),text="6",width=5, height=2, bg=cor2, font='Ivy 13 bold', relief=GROOVE, overrelief=FLAT)
b_10.place(x=120, y=104)
b_11 = Button(frame_corpo, command= lambda: digita_valor('-'), text="-",width=5, height=2, bg=cor5, fg=cor2, font='Ivy 13 bold', relief=GROOVE, overrelief=FLAT)
b_11.place(x=180, y=104)

b_12 = Button(frame_corpo, command= lambda: digita_valor('1'), text="1",width=5, height=2, bg=cor2, font='Ivy 13 bold', relief=GROOVE, overrelief=FLAT)
b_12.place(x=0, y=156)
b_13 = Button(frame_corpo, command= lambda: digita_valor('2'), text="2",width=5, height=2, bg=cor2, font='Ivy 13 bold', relief=GROOVE, overrelief=FLAT)
b_13.place(x=60, y=156)
b_14 = Button(frame_corpo, command= lambda: digita_valor('3'), text="3",width=5, height=2, bg=cor2, font='Ivy 13 bold', relief=GROOVE, overrelief=FLAT)
b_14.place(x=120, y=156)
b_15 = Button(frame_corpo, command= lambda: digita_valor('+'), text="+",width=5, height=2, bg=cor5, fg=cor2, font='Ivy 13 bold', relief=GROOVE, overrelief=FLAT)
b_15.place(x=180, y=156)

b_16 = Button(frame_corpo, command= lambda: digita_valor('0'), text="0",width=11, height=2, bg=cor2, font='Ivy 13 bold', relief=GROOVE, overrelief=FLAT)
b_16.place(x=0, y=208)
b_17 = Button(frame_corpo, command= lambda: digita_valor('.'), text=".",width=5, height=2, bg=cor2, font='Ivy 13 bold', relief=GROOVE, overrelief=FLAT)
b_17.place(x=120, y=208)
b_18 = Button(frame_corpo, command= calcular, text="=",width=5, height=2, bg=cor5, fg=cor2, font='Ivy 13 bold', relief=GROOVE, overrelief=FLAT)
b_18.place(x=180, y=208)


janela.mainloop()
