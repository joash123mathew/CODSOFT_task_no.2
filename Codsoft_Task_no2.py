from tkinter import *

window = Tk()
window.title('Calculator')
window.geometry('700x400')
window.configure(bg='grey')
#Integer containers
Num1 = IntVar()
Num2 = IntVar()

def Sum():
    summ = Num1.get() + Num2.get()
    result1.config(text=f"Sum is {summ}",fg='green')

def Diff():
    diff = Num1.get() - Num2.get()
    result1.config(text=f"Difference is {diff}",fg='green')

def Prod():
    prod = Num1.get() * Num2.get()
    result1.config(text=f"Product is {prod}",fg='green')

def Quo():
    if Num2.get()==0:
        result1.config(text="ERROR!!!, denominator is 0",fg='red')
    else:
        quo = Num1.get() / Num2.get()
        result1.config(text=f"Quotient is {quo}",fg='green')

def Mod():
    if Num2.get()==0:
        result1.config(text="ERROR!!!, denominator is 0",fg='red')
    else:
        mod = Num1.get() % Num2.get()
        result1.config(text=f"Modulus is {mod}",fg='green')

title=Label(window,text="Calculator",font=('Arial',40),fg='red')
title.grid(padx=2,row=0,column=2,pady=(10,50))

l1=Label(window,text='Number1:',font=('Arial',30))
l1.grid(row=1,column=0,padx=(100,10))

tb1=Entry(window,textvariable=Num1,font=('Arial',30))
tb1.grid(row=1,column=1)

l2=Label(window,text='Number2:',font=('Arial',30))
l2.grid(row=2,column=0,padx=(100,10),pady=(50))

tb2=Entry(window,textvariable=Num2,font=('Arial',30))
tb2.grid(row=2,column=1)

plus = Button(window,text="+",command=Sum,font=("arial",20))
plus.grid(row=3,column=1,pady=(30),padx=(0,400))

minus = Button(window,text="-",command=Diff,font=("arial",20))
minus.grid(row=3,column=1,pady=(30),padx=(0,300))

mult = Button(window,text="*",command=Prod,font=("arial",20))
mult.grid(row=3,column=1,pady=(30),padx=(0,200))

div = Button(window,text="/",command=Quo,font=("arial",20))
div.grid(row=3,column=1,pady=(30),padx=(0,100))

mod = Button(window,text="%",command=Mod,font=("arial",20))
mod.grid(row=3,column=1,pady=(30),padx=(0,0))

result1 = Label(window,text= ' ',font=('arial',30,'bold'))
result1.grid(row=4,column=2,pady=30)

window.mainloop()