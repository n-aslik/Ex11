import tkinter as tk
from tkinter import *
from tkinter import ttk,messagebox
from math import factorial
import math
def add():
    try:
        v1=float(i1.get())
        v2=float(i2.get())
        v3=v1+v2
        i3.set(str(round(v3,1)))
        e3['bg']='green'
        e3['fg']='white'
        
    except ValueError:
        i3.set(str(round(v3,1)))
        e3['bg']='green'
        e3['fg']='white'
def sub():
    try:
        v1=float(i1.get())
        v2=float(i2.get())
        v3=v1-v2
        i3.set(str(round(v3,1)))
        e3['bg']='green'
        e3['fg']='white'
    except ValueError:
        i3.set(str(round(v3,1)))
        e3['bg']='green'
        e3['fg']='white'
def pro():
    try:
        v1=float(i1.get())
        v2=float(i2.get())
        v3=v1*v2
        i3.set(str(round(v3,1)))
        e3['bg']='green'
        e3['fg']='white'
    except ValueError:
        i3.set(str(round(v3,1)))
        e3['bg']='green'
        e3['fg']='white'
def div():
    try:
        v1=float(i1.get())
        v2=float(i2.get())
        v3=v1/v2
        i3.set(str(round(v3,2)))
        e3['bg']='green'
        e3['fg']='white'
        if  v1==0:
            i3.set(str(round(v3,2)))
    except ValueError and ZeroDivisionError:
        messagebox.showinfo("Ошибка","Деление на ноль невозможно")
        i3.set(str(round(v3,2)))
        e3['bg']='green'
        e3['fg']='white' 
def div1():
    try:
        v1=float(i1.get())
        #v2=float(i2.get())
        v3=1/v1
        i3.set(str(round(v3,3)))
        e3['bg']='green'
        e3['fg']='white'
        if  v1==0:
            i3.set(str(round(v3,3)))
    except ValueError and ZeroDivisionError:
        messagebox.showinfo("Ошибка","Деление на ноль невозможно")
        i3.set(str(round(v3,3)))
        e3['bg']='green'
        e3['fg']='white'  
def mod():
    try:
        v1=float(i1.get())
        v2=float(i2.get())
        v3=v1%v2
        i3.set(str(round(v3,1)))
        e3['bg']='green'
        e3['fg']='white'
    except ZeroDivisionError or ValueError:
        i3.set(str(round(v1,1)))
        e3['bg']='green'
        e3['fg']='white'
def stp():
    try:
        v1=float(i1.get())
        v2=float(i2.get())
        v3=v1**v2
        i3.set(str(round(v3,1)))
        e3['bg']='green'
        e3['fg']='white'
    except ValueError:
        i3.set(str(round(v3,1)))
        e3['bg']='green'
        e3['fg']='white'
def x_sqrt_y():
    try:
        v1=float(i1.get())
        v2=float(i2.get())
        v3=v1**((1/v2)*v2)
        i3.set(str(round(v3,1)))
        e3['bg']='green'
        e3['fg']='white'
    except ValueError:
        i3.set(str(round(v3,1)))
        e3['bg']='green'
        e3['fg']='white'
def fct():
    try:
        v1=int(i1.get())
        #v2=float(i2.get())
        i3.set(str(round(factorial(v1),1)))
        e3['bg']='green'
        e3['fg']='white'
    except ValueError and TypeError:
        i3.set(str(round(factorial(v1),1)))
        e3['bg']='green'
        e3['fg']='white'
def sin():
    try:
        v1=float(i1.get())
        #v2=float(i2.get())
        i3.set(str(round(math.sin(v1),1)))
        e3['bg']='green'
        e3['fg']='white'
    except ValueError and TypeError:
        i3.set(str(round(math.sin(v1),1)))
        e3['bg']='green'
        e3['fg']='white' 
def cos():
    try:
        v1=float(i1.get())
        #v2=float(i2.get())
        i3.set(str(round(math.cos(v1),1)))
        e3['bg']='green'
        e3['fg']='white'
    except ValueError and TypeError:
        i3.set(str(round(math.cos(v1),1)))
        e3['bg']='green'
        e3['fg']='white' 
def tg():
    try:
        v1=float(i1.get())
        #v2=float(i2.get())
        i3.set(str(round(math.tan(v1),1)))
        e3['bg']='green'
        e3['fg']='white'
    except ValueError and TypeError:
        i3.set(str(round(math.tan(v1),1)))
        e3['bg']='green'
        e3['fg']='white' 
def ctg():
    try:
        v1=float(i1.get())
        #v2=float(i2.get())
        i3.set(str(round(1/(math.tan(v1)),1)))
        e3['bg']='green'
        e3['fg']='white'
    except ValueError and TypeError:
        i3.set(str(round(1/(math.tan(v1)),1)))
        e3['bg']='green'
        e3['fg']='white' 
def sqt():
    try:
        v1=float(i1.get())
        #v2=float(i2.get())
        i3.set(str(round(math.sqrt(v1),2)))
        e3['bg']='green'
        e3['fg']='white'
    except ValueError and TypeError:
        i3.set(str(round(math.sqrt(v1),2)))
        e3['bg']='green'
        e3['fg']='white' 
def stp2():
    try:
        v1=float(i1.get())
        #v2=float(i2.get())
        v3=v1**2
        i3.set(str(round(v3,1)))
        e3['bg']='green'
        e3['fg']='white'
    except ValueError:
        i3.set(str(round(v3,1)))
        e3['bg']='green'
        e3['fg']='white'
def stp3():
    try:
        v1=float(i1.get())
        #v2=float(i2.get())
        v3=v1**3
        i3.set(str(round(v3,1)))
        e3['bg']='green'
        e3['fg']='white'
    except ValueError:
        i3.set(str(round(v3,1)))
        e3['bg']='green'
        e3['fg']='white'
def tenx():
    try:
        v1=float(i1.get())
        #v2=float(i2.get())
        v3=10**v1
        i3.set(str(round(v3,1)))
        e3['bg']='green'
        e3['fg']='white'
    except ValueError:
        i3.set(str(round(v3,1)))
        e3['bg']='green'
        e3['fg']='white'
def ecspx():
    try:
        v1=float(i1.get())
        #v2=float(i2.get())
        v3=math.exp(v1)
        i3.set(str(round(v3,1)))
        e3['bg']='green'
        e3['fg']='white'
    except ValueError:
        i3.set(str(round(v3,1)))
        e3['bg']='green'
        e3['fg']='white'
def log():
    try:
        v1=float(i1.get())
        #v2=float(i2.get())
        v3=math.log(v1)
        i3.set(str(round(v3,1)))
        e3['bg']='green'
        e3['fg']='white'
    except ValueError:
        i3.set(str(round(v3,1)))
        e3['bg']='green'
        e3['fg']='white'
def deg():
    try:
        v1=float(i1.get())
        #v2=float(i2.get())
        v3=math.degrees(v1)
        i3.set(str(round(v3,2)))
        e3['bg']='green'
        e3['fg']='white'
    except ValueError:
        i3.set(str(round(v3,2)))
        e3['bg']='green'
        e3['fg']='white'
def rad():
    try:
        v1=float(i1.get())
        #v2=float(i2.get())
        v3=math.radians(v1)
        i3.set(str(round(v3,2)))
        e3['bg']='green'
        e3['fg']='white'
    except ValueError:
        i3.set(str(round(v3,2)))
        e3['bg']='green'
        e3['fg']='white'        
#screen control        
def clear():
   e1.delete(0,END)
   e2.delete(0,END)
   e3.delete(0,END)
   e3['bg']='white'
   e3['fg']='black'
def default():
    w.geometry("218x195")
def engineer():
    w.geometry("337x195")
# def programmer():
#     global btn20,btn21,btn22,btn23,l1p,l2p,lp
#     def back():
#         win1.withdraw()
#     def addp():
#         bv1=int(b1.get())
#         bv2=int(b2.get())
#     def subp():
#         pass
#     def prop():
#         pass
#     def divp():
#         pass
    # win1=Tk()
    # win1.geometry("270x195")
    # win1.config(bg="green")
    # win1.title("Программист")
    # b1=tk.StringVar()
    # b2=tk.StringVar()
    # b3=tk.StringVar()
    # lp=Label(win1,text="Введите 1 число:").grid(row=0,column=0,stick="wens")
    # l1p=Label(win1,text="Введите 2 число:").grid(row=1,column=0,stick="wens")
    # l2p=Label(win1,text="Ответ:").grid(row=2,column=0,stick="wens")
    # en1=Entry(win1,textvariable=b1)
    # en1.grid(row=0,column=1,stick="wens")
    # en2=Entry(win1,textvariable=b2)
    # en2.grid(row=1,column=1,stick="wens")
    # en3=Entry(win1,textvariable=b3,bg='white')
    # en3.grid(row=2,column=1,stick="wens")
    # btn20=Button(win1,text="+",command=addp,activebackground="blue").grid(row=3,column=0,stick="wens")
    # btn21=Button(win1,text="-",command=subp,activebackground="blue").grid(row=3,column=1,stick="wens")
    # btn22=Button(win1,text="*",command=prop,activebackground="blue").grid(row=4,column=0,stick="wens")
    # btn23=Button(win1,text="/",command=divp,activebackground="blue").grid(row=4,column=1,stick="wens")
    # btn=Button(win1,text="Назад",command=back)
    # btn.grid(row=0,column=3)
    # win1.mainloop()
w=Tk()
calc_menu=Menu()
mode_menu=Menu(tearoff=0)
mode_menu.add_command(label="Обычный",command=default)
mode_menu.add_command(label="Инженерный",command=engineer)
#mode_menu.add_command(label="Программист",command="programmer")
calc_menu.add_cascade(label="Меню",menu=mode_menu)
w.config(bg="yellow",menu=calc_menu)
w.option_add("*tearoff",False)
w.title("Калькулятор")
w.geometry("218x195")
w.resizable(False,False)
i1=tk.StringVar()
i2=tk.StringVar()
i3=tk.StringVar()
l=Label(w,text="Введите 1 число:").grid(row=0,column=0,stick="wens")
l1=Label(w,text="Введите 2 число:").grid(row=1,column=0,stick="wens")
l2=Label(w,text="Ответ:").grid(row=2,column=0,stick="wens")
e1=Entry(w,textvariable=i1)
e1.grid(row=0,column=1,stick="wens")
e2=Entry(w,textvariable=i2)
e2.grid(row=1,column=1,stick="wens")
e3=Entry(w,textvariable=i3,bg='white')
e3.grid(row=2,column=1,stick="wens")
#Обычный
btn1=Button(w,text="+",command=add,activebackground="blue").grid(row=3,column=0,stick="wens")
btn2=Button(w,text="-",command=sub,activebackground="blue").grid(row=3,column=1,stick="wens")
btn3=Button(w,text="*",command=pro,activebackground="blue").grid(row=4,column=0,stick="wens")
btn4=Button(w,text="/",command=div,activebackground="blue").grid(row=4,column=1,stick="wens")
btn5=Button(w,text="%",command=mod,activebackground="blue").grid(row=5,column=0,stick="wens")
btn17=Button(w,text="x^1/2",command=sqt,activebackground="blue").grid(row=5,column=1,stick="wens")
btn18=Button(w,text="x^2",command=stp2,activebackground="blue").grid(row=6,column=0,stick="wens")
btn19=Button(w,text="x^3",command=stp3,activebackground="blue").grid(row=6,column=1,stick="wens")
btn13=Button(w,text="C",command=clear,activebackground="blue").grid(row=7,column=0,stick="wens")
btn16=Button(w,text="1/x",command=div1,activebackground="blue").grid(row=7,column=1,stick="wens")
# btn14=Button(w,text="["+" "+"]",command=size_large,activebackground="blue").grid(row=6,column=0,stick="wens")
# btn15=Button(w,text="[]",command=size_small,activebackground="blue").grid(row=6,column=0,stick="wens")
#Инженерный
btn7=Button(w,text="x^y",command=stp,activebackground="blue").grid(row=3,column=2,stick="wens")
btn8=Button(w,text="n!",command=fct,activebackground="blue").grid(row=4,column=2,stick="wens")
btn9=Button(w,text="sinx",command=sin,activebackground="blue").grid(row=5,column=2,stick="wens")
btn10=Button(w,text="cosx",command=cos,activebackground="blue").grid(row=6,column=2,stick="wens")
btn11=Button(w,text="tgx",command=tg,activebackground="blue").grid(row=7,column=2,stick="wens")
btn12=Button(w,text="ctgx",command=ctg,activebackground="blue").grid(row=3,column=3,stick="wens")
btn20=Button(w,text="x^1/x*y",command=x_sqrt_y,activebackground="blue").grid(row=4,column=3,stick="wens")
btn20=Button(w,text="10^x",command=tenx,activebackground="blue").grid(row=5,column=3,stick="wens")
btn21=Button(w,text="e^x",command=ecspx,activebackground="blue").grid(row=6,column=3,stick="wens")
btn22=Button(w,text="log",command=log,activebackground="blue").grid(row=7,column=3,stick="wens")
btn23=Button(w,text="deg",command=deg,activebackground="blue").grid(row=3,column=4,stick="wens",rowspan=3)
btn24=Button(w,text="rad",command=rad,activebackground="blue").grid(row=6,column=4,stick="wens",rowspan=2)
# w.bind('<Double-Button-1>',size_large)
# w.bind('<Double-Button-3>',size_small)#key Enrer and Tab
#w.bind('<Return>',size_small)#key Enrer and Tab
w.mainloop()