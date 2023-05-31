from tkinter import *
from functools import partial

master = Tk()
master.title("Calculadora")

#Funções

def click_igual():
    segundo_numero = visor.get()
    visor.delete(0, END)
    if matematica == "soma":
        visor.insert(0, p_numero + float(segundo_numero))
    if matematica == "subtracao":
        visor.insert(0, p_numero - float(segundo_numero))
    if matematica == "divisao":
        visor.insert(0, p_numero / float(segundo_numero))
    if matematica == "multiplicacao":
        visor.insert(0, p_numero * float(segundo_numero))


def click_soma():
    primeiro_numero = visor.get()
    global p_numero
    global matematica
    matematica = "soma"
    p_numero = float(primeiro_numero)
    visor.delete(0, END)

def click_sub():
    primeiro_numero = visor.get()
    global p_numero
    global matematica
    matematica = "subtracao"
    p_numero = float(primeiro_numero)
    visor.delete(0, END)

def click_div():
    primeiro_numero = visor.get()
    global p_numero
    global matematica
    matematica = "divisao"
    p_numero = float(primeiro_numero)
    visor.delete(0, END)

def click_mult():
    primeiro_numero = visor.get()
    global p_numero
    global matematica
    matematica = "multiplicacao"
    p_numero = float(primeiro_numero)
    visor.delete(0, END)


def click_ponto():
    visor.insert(END, ".")

def deletar():
    visor.delete(0, END)

def click_button(numero):
    atual = visor.get()
    visor.delete(0, END)
    visor.insert(END, str(atual)+ str(numero))

lb1 = Label(master, text="CALCULADORA", font=("verdana", 20, "bold"), pady=10)
lb1.pack()

visor = Entry(master, width= 80, bg="lightblue", bd=2)
visor.pack()

lb2 = Label(master, text="   by Dev.pedromatos@gmail.com", font=("verdana", 10, "bold"), pady=10)
lb2.place(x=2, y=320)

#Coluna 1:

bt7 = Button(master, text="7", bg="lightblue",pady=14, padx=14, bd=4, command= lambda: click_button(7))
bt7.place(x=10, y=100)

bt4 = Button(master, text="4", bg="lightblue",pady=14, padx=14, bd=4, command= lambda: click_button(4))
bt4.place(x=10, y=155)

bt1 = Button(master, text="1", bg="lightblue",pady=14, padx=14, bd=4, command= lambda: click_button(1))
bt1.place(x=10, y=210)

bt0 = Button(master, text="0", bg="lightblue",pady=14, padx=14, bd=4, command= lambda: click_button(0))
bt0.place(x=10, y=265)

#Coluna 2:

bt8 = Button(master, text="8", bg="lightblue",pady=14, padx=14, bd=4, command= lambda: click_button(8))
bt8.place(x=60, y=100)

bt5 = Button(master, text="5", bg="lightblue",pady=14, padx=14, bd=4, command= lambda: click_button(5))
bt5.place(x=60, y=155)

bt2 = Button(master, text="2", bg="lightblue",pady=14, padx=14, bd=4, command= lambda: click_button(2))
bt2.place(x=60, y=210)

bt_ponto = Button(master, text=".", bg="lightblue",pady=14, padx=15, bd=4, command=click_ponto)
bt_ponto.place(x=60, y=265)


#Coluna 3:

bt9 = Button(master, text="9", bg="lightblue",pady=14, padx=14, bd=4, command= lambda: click_button(9))
bt9.place(x=110, y=100)

bt6 = Button(master, text="6", bg="lightblue",pady=14, padx=14, bd=4, command= lambda: click_button(6))
bt6.place(x=110, y=155)

bt3 = Button(master, text="3", bg="lightblue",pady=14, padx=14, bd=4, command= lambda: click_button(3))
bt3.place(x=110, y=210)

bt_exp = Button(master, text="EXP", bg="silver",pady=14, padx=7, bd=4)
bt_exp.place(x=110, y=265)


#Coluna 4:

bt_ce = Button(master, text="CE", bg="silver",pady=14, padx=10, bd=4, command=deletar)
bt_ce.place(x=160, y=100)

bt_multiplicar = Button(master, text="*", bg="silver",pady=14, padx=14, bd=4, command= click_mult)
bt_multiplicar.place(x=160, y=155)

bt_somar = Button(master, text="+", bg="silver",pady=14, padx=13, bd=4, command=click_soma)
bt_somar.place(x=160, y=210)

bt_ans = Button(master, text="ANS", bg="silver",pady=14, padx=5, bd=4)
bt_ans.place(x=160, y=265)

#Coluna 5:

bt_del = Button(master, text="DEL", bg="silver",pady=14, padx=7, bd=4)
bt_del.place(x=210, y=100)

bt_dividir = Button(master, text="/", bg="silver",pady=14, padx=14, bd=4, command=click_div)
bt_dividir.place(x=210, y=155)

bt_subtrair = Button(master, text="-", bg="silver",pady=14, padx=14, bd=4, command=click_sub)
bt_subtrair.place(x=210, y=210)

bt_igual = Button(master, text="=", bg="green",pady=14, padx=12, bd=4, command=click_igual)
bt_igual.place(x=210, y=265)

master.resizable(False, False)
master.geometry("280x380")
master.mainloop()