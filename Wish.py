from tkinter import *
from tkinter import ttk
from tkinter import messagebox



win = Tk()
win.title("The New price")
win.geometry("300x500+550+200")
win.configure(background="#7f8fa6")
style = ttk.Style()
style.theme_use('classic')
style.configure('TButton', background="#7f8fa6")


def Reset():
    Var.set("")
    ProductPrice.set("0")
    DiscountPercentage.set("0")
    ProductPrice.set("0")
    NewPrice.set("0")
    priceOfReduction.set("0")

def Total():
    n = Var.get()
    print(n)


def iExit():
    exit = messagebox.askyesno("The New price", "Confirm id you want exit")
    if exit > 0:
        win.destroy()

def Total():
    if (Var.get() == "Increase" ):
        Step1 = ProductPrice.get() *  DiscountPercentage.get()
        Step2 = Step1 / 100
        Step3 = priceOfReduction.set(Step2)
        Step3 = ProductPrice.get() + Step2
        Step4 = NewPrice.set(Step3)

    elif (Var.get() == "Decrease" ):
        Step1 = ProductPrice.get() *  DiscountPercentage.get()
        Step2 = Step1 / 100
        Step3 = priceOfReduction.set(Step2)
        Step3 = ProductPrice.get() - Step2
        Step4 = NewPrice.set(Step3)

def About():
    root =Tk()
    root.title("About Me")
    root.configure(background = "#2f3640")
    root.geometry("250x200+570+240")
    style = ttk.Style()
    style.theme_use('classic')
    style.configure('TButton', background="#7f8fa6")
    def iiExit():
        root.destroy()

    inf = Label(root, text="""
u"Copyright © 2018,
Youssef Boubli,
All Rights Reserved
    """, font=("arial", 15, 'bold'), bg='#2f3640', fg="white")
    inf.pack()

    btn = ttk.Button(root, text="Exit", command=iiExit)
    btn.pack(pady=40)

    root.mainloop()

txtIncreaseOrDecrease = Label(win, text="Increase or decrease", font=('arial', 13, 'bold'), bg="#7f8fa6", fg="white")
txtIncreaseOrDecrease.pack()

Var = StringVar()
IncreaseOrDecrease = ttk.Combobox(win,  state='readonly', width=20, font=('arial', 13, 'bold'), textvariable=Var,)
IncreaseOrDecrease['value'] = (" ", 'Increase', 'Decrease')
IncreaseOrDecrease.current(0)
IncreaseOrDecrease.pack()

ProductPrice = IntVar()
txtProductPrice = Label(win, text="Product price", width=20, font=('arial', 13, 'bold'), bg="#7f8fa6", fg="white")
txtProductPrice.pack()
lblProductPrice = Entry(win, width=30, bd=5, justify='left', textvariable=ProductPrice)
lblProductPrice.pack()

DiscountPercentage = IntVar()
txtDiscountPercentage = Label(win, text="discount percentage", width=30, font=('arial', 13, 'bold'), bg="#7f8fa6", fg="white")
txtDiscountPercentage.pack()
lblDiscountPercentage = Entry(win, width=30, bd=5, justify='left', textvariable=DiscountPercentage)
lblDiscountPercentage.pack()

priceOfReduction = IntVar()
txtpriceOfReduction = Label(win, text="The price of reduction", width=30, font=('arial', 13, 'bold'), bg="#7f8fa6", fg="white")
txtpriceOfReduction.pack()
lblpriceOfReduction = Entry(win, width=30, bd=5, justify='left', textvariable=priceOfReduction, state='readonly')
lblpriceOfReduction.pack()

NewPrice = IntVar()
txtNewPrice = Label(win, text="The new price", width=30, font=('arial', 13, 'bold'), bg="#7f8fa6", fg="white")
txtNewPrice.pack()
lblNewPrice = Entry(win, width=30, bd=5, justify='left', textvariable=NewPrice, state='readonly')
lblNewPrice.pack()

btnTotal = ttk.Button(win, width=10, text="Total", command=Total)
btnTotal.pack(pady=6)
btnReset = ttk.Button(win, width=10, text="Reset",command=Reset)
btnReset.pack(pady=6)
btnExit = ttk.Button(win, width=10, text="Exit",command=iExit)
btnExit.pack(pady=6)

btnAbout = ttk.Button(win, width=10, text="About",command=About)
btnAbout.pack(pady=6)


win.mainloop()