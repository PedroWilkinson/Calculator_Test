from tkinter import *
from functools import partial

master = Tk()
master.title("Calculadora")



#Coluna 1:

bt7 = Button(master, text="7", bg="lightblue",pady=14, padx=14, bd=4)
bt7.place(x=10, y=100)

bt4 = Button(master, text="4", bg="lightblue",pady=14, padx=14, bd=4)
bt4.place(x=10, y=155)

bt1 = Button(master, text="1", bg="lightblue",pady=14, padx=14, bd=4)
bt1.place(x=10, y=210)

#Coluna 2:

bt8 = Button(master, text="8", bg="lightblue",pady=14, padx=14, bd=4)
bt8.place(x=60, y=100)

bt5 = Button(master, text="5", bg="lightblue",pady=14, padx=14, bd=4)
bt5.place(x=60, y=155)

bt2 = Button(master, text="2", bg="lightblue",pady=14, padx=14, bd=4)
bt2.place(x=60, y=210)

bt0 = Button(master, text="0", bg="lightblue",pady=14, padx=14, bd=4)
bt0.place(x=60, y=265)

#Coluna 3:

bt9 = Button(master, text="9", bg="lightblue",pady=14, padx=14, bd=4)
bt9.place(x=110, y=100)

bt6 = Button(master, text="6", bg="lightblue",pady=14, padx=14, bd=4)
bt6.place(x=110, y=155)

bt3 = Button(master, text="3", bg="lightblue",pady=14, padx=14, bd=4)
bt3.place(x=110, y=210)

bt_ponto = Button(master, text=".", bg="green",pady=14, padx=15, bd=4)
bt_ponto.place(x=110, y=265)

#Coluna 4:

bt_dividir = Button(master, text="/", bg="lightblue",pady=14, padx=14, bd=4)
bt_dividir.place(x=160, y=100)

bt_multiplicar = Button(master, text="*", bg="lightblue",pady=14, padx=14, bd=4)
bt_multiplicar.place(x=160, y=155)

bt_subtrair = Button(master, text="-", bg="lightblue",pady=14, padx=14, bd=4)
bt_subtrair.place(x=160, y=210)

bt_somar = Button(master, text="+", bg="lightblue",pady=14, padx=14, bd=4)
bt_somar.place(x=160, y=265)

master.resizable(False, False)
master.geometry("280x380")
master.mainloop()