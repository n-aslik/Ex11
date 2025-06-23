import sqlite3
import tkinter as tk
from tkinter import ttk,messagebox
from tkinter import*
from currency_converter import CurrencyConverter
import datetime
 
def updbalans():
    def chng1():
        conn = sqlite3.connect('my_wallet.db')
        curs = conn.cursor()
        upd = e6.get()
        user_id=e7.get()
        try:
            curs.execute('''UPDATE wallet SET balance=balance+ ? WHERE id= ?''',(upd,user_id,))
            conn.commit()
            messagebox.showinfo("Сообщение","Добавление прошло успешно!")
        except Exception as e:
            messagebox.showerror("Ошибка","Добавление прошло неудачно")
            print(e)
            conn.rollback()
            conn.close()

    def chng2():
        try:
            conn = sqlite3.connect('my_wallet.db')
            curs = conn.cursor()
            upd = e6.get()
            user_id=e7.get()
            curs.execute('''UPDATE wallet SET balance=balance-? WHERE id=?''',(upd,user_id,))
            conn.commit()
            messagebox.showinfo("Сообщение","Вычисление прошло успешно!")
        except Exception as e:
            messagebox.showerror("Ошибка","Вычисление прошло неудачно")
            print(e)
            conn.rollback()
            conn.close()
        
        

    u=Tk()
    u.title('Добавление/Вычисление')
    u.resizable(False,False)
    ch1=ttk.Button(u,text='Добавление',command=chng1)
    ch1.grid(row=1,column=0)
    ch2=ttk.Button(u,text='Вычисление',command=chng2)
    ch2.grid(row=1,column=1)
    ls=tk.Label(u,text='Введите число')
    ls.grid(row=0,column=0,sticky='wens')
    e6=tk.Entry(u)
    e6.grid(row=0,column=1,sticky='wens')
    u.mainloop()



def find_user():
    conn=sqlite3.connect('my_wallet.db')
    curs=conn.cursor()
    find_u=e1.get()
    curs.execute('''SELECT id, user, balance FROM wallet WHERE id=?''',(find_u))
    info=curs.fetchone()
    if info:
        e2.delete(0,"end")
        e3.delete(0,"end")
        e7.delete(0,"end")

        e2.insert(0,info[1])
        e3.insert(0,info[2])
        e7.insert(0,info[0])
        messagebox.showinfo("Сообщение","Поиск прошёл успешно")
    else:
        messagebox.showerror("Ошибка","Поиск неудался!")
    e1.delete(0,"end")


def notice():
    conn=sqlite3.connect('my_wallet.db')
    curs=conn.cursor()
    user_id=e7.get()
    curs.execute('''SELECT balance FROM wallet WHERE id=?''',(user_id))
    info=curs.fetchone()
    if info[0]<=5:
        messagebox.showinfo("Сообщение",f"На вашем балансе {info[0]} сомони,пожалуйста пополните баланс")
    else:    
        messagebox.showinfo("Сообщение",f"На вашем балансе {info[0]} сомони")
    conn.close()





def newuser():
    def add():
        a_u=e4.get()
        a_c=e5.get()
        a_cd=e11.get()
        conn=sqlite3.connect('my_wallet.db')
        curs=conn.cursor()
        try:
            curs.execute('''Insert into wallet(user,balance,card) values(?,?,?)''',(a_u,a_c,a_cd,))
            messagebox.showinfo("Сообщение","Добавление прошёл успешно!")
            conn.commit()
        except Exception as e:
            print(e)
            conn.rollback()
            conn.close()


            

    w=Tk()
    w.title('Создать пользователя')
    w.resizable(False,False)
    #Добавление пользователя
    global e4,e5,e11
    lu=tk.Label(w,text='Имя').grid(row=0,column=0,sticky='wens')
    lc=tk.Label(w,text='Баланс').grid(row=1,column=0,sticky='wens')
    lcd=tk.Label(w,text='Карта').grid(row=2,column=0,sticky='wens')
    e4=tk.Entry(w)
    e4.grid(row=0,column=1,sticky='wens')
    e5=tk.Entry(w)
    e5.grid(row=1,column=1,sticky='wens')
    e11=tk.Entry(w)
    e11.grid(row=2,column=1,sticky='wens')
    newu_btn=tk.Button(w,text='Добавить',command=add)
    newu_btn.grid(row=3,column=0,columnspan=2,sticky='wens')
    
    w.mainloop()



    


            


def my_cards():
    mc=Tk()
    mc.geometry('400x100')
    mc.title('Мои карты')
    mc.config(bg='yellow')
    mc.resizable(False,False)
    conn=sqlite3.connect('my_wallet.db')
    curs=conn.cursor()
    user_id=e7.get()
    curs.execute('''SELECT card FROM wallet WHERE id=?''',(user_id,))
    info=curs.fetchone()
    for i in info:
        msg_l=tk.Label(mc,text=f'Ваши карты:{i}\t',fg='blue',bg='yellow',font=('Arial',12,'bold')).grid(row=0,column=0,sticky='wens')
    conn.close()
    mc.mainloop()

def money_transfer():
    def transfer():
        conn=sqlite3.connect('my_wallet.db')
        curs=conn.cursor()
        user_name1=e2.get()
        user_name2=e9.get()
        bal=e10.get()
        try:
            curs.execute('UPDATE wallet SET balance=balance+? WHERE user=?',(user_name1,user_name2,bal))
            messagebox.showinfo("Сообщение","Перевод выполнился успешно!")
        except Exception as e:
            messagebox.showerror("Ошибка","Произошла ошибка")
            print(e)
            conn.rollback()
            conn.close()
    

    mt=Tk()

    mt.title('Перевод денег')

    intolabel=tk.Label(mt,text='От кого:',width=12,bd=2,relief=tk.SUNKEN)

    intolabel.config(font=('Calibri',12))

    intolabel.grid(row=0,column=0,sticky='wens')
    

    fromlabel=tk.Label(mt,text='Кому:',width=12,bd=2,relief=tk.SUNKEN)

    fromlabel.config(font=('Calibri',12))

    fromlabel.grid(row=1,column=0,sticky='wens')

    e8=tk.Entry(mt)

    e8.grid(row=0,column=1)

    e9=tk.Entry(mt)

    e9.grid(row=1,column=1)

    e10=tk.Entry(mt)

    e10.grid(row=0,column=2)

    transf_btn=tk.Button(mt,text='Переводить',bg='red',width=8,height=1,bd=2,relief=tk.SUNKEN,command=transfer)

    transf_btn.config(font=('Calibri',12))

    transf_btn.grid(row=1,column=2,sticky='wens',columnspan=2)

    mt.quit()


    


def toexit():

    win.withdraw()




win=Tk()

wall_menu=Menu()

mode_menu=Menu(tearoff=0)

mode_menu.add_command(label='Создать',command=newuser)


mode_menu.add_command(label='Выйти',command=toexit)

wall_menu.add_cascade(label='Меню',menu=mode_menu)

win.title('Мой_кошелёк')

win.config(bg='pink',menu=wall_menu)

win.geometry('520x800')

win.option_add("*tearoff",False)

win.resizable(False,False)


global e1,e2,e3,e7

#Поиск

finduser=tk.Label(win,text='Поиск',bd=2,relief=tk.SUNKEN)

finduser.config(font=('Calibri',12))

finduser.grid(row=0,column=0,sticky='wens')


e1=tk.Entry(win)

e1.config(font=('Calibri',12))

e1.grid(row=0,column=1,sticky='wens')


find_btn=tk.Button(win,text='Найти',bg='red',width=8,height=1,bd=2,relief=tk.SUNKEN,command=find_user)

find_btn.config(font=('Calibri',12))

find_btn.grid(row=0,column=2,sticky='wens',columnspan=2)

#


#Баланс

bal_label=tk.Label(win,text='Баланс',width=12,bd=2,relief=tk.SUNKEN)

bal_label.config(font=('Calibri',12))

bal_label.grid(row=2,column=0,sticky='wens')


e2=tk.Entry(win)

e2.config(font=('Calibri',12))

e2.grid(row=1,column=1,sticky='wens')

#

#Пользователь

user_label=tk.Label(win,text='Пользователь',width=12,bd=2,relief=tk.SUNKEN)

user_label.config(font=('Calibri',12))

user_label.grid(row=1,column=0,sticky='wens')

id_label=tk.Label(win,text='ID',width=5,bd=2,relief=tk.SUNKEN)

id_label.config(font=('Calibri',12))

id_label.grid(row=1,column=2,sticky='wns')


e3=tk.Entry(win)

e3.config(font=('Calibri',12))

e3.grid(row=2,column=1,sticky='wens')

e7=tk.Entry(win,width=5)

e7.config(font=('Calibri',12))

e7.grid(row=1,column=2,sticky='ens')

#


#Курс денег

c=CurrencyConverter()

curren=1

res=c.convert(curren,'USD','EUR')


usd_n=IntVar()

usd_n.set(curren)

eur_n=IntVar()

eur_n.set(round(res,6))


img=PhotoImage(file='C:\Users\Администратор\Documents\Ex11\Wallet\conv.png')

Empty=tk.Label(win,bd=2,height=400,bg='orange',image=img,relief=tk.RAISED)

Empty.grid(row=6,column=0,sticky='wens',columnspan=4)

img1=PhotoImage(file='C:\Users\Администратор\Documents\Ex11\Wallet\usd.png')

usdlab=tk.Label(win,image=img1,bg='lightgray',fg='blue',relief=tk.RAISED)

usdlab.grid(row=7,column=0,sticky='wens')

usdlab1=tk.Label(win,textvariable=usd_n,bg='lightgray',fg='blue',relief=tk.RAISED)

usdlab1.grid(row=7,column=1,sticky='wens')


img2=PhotoImage(file='C:\Users\Администратор\Documents\Ex11\Wallet\eur.png')

eurlab=tk.Label(win,image=img2,bg='lightgray',fg='blue',relief=tk.RAISED)

eurlab.grid(row=7,column=2,sticky='wens')

eurlab1=tk.Label(win,textvariable=eur_n,bg='lightgray',fg='blue',relief=tk.RAISED)

eurlab1.grid(row=7,column=3,sticky='wens')

#

Empty1=tk.Label(win,bd=2,height=5,bg='pink')

Empty1.grid(row=8,column=0,sticky='wens',columnspan=4)

#Кнопки

balance_btn=tk.Button(win,text='Уведомление',bg='purple',bd=2,fg='orange',relief=tk.SUNKEN,width=5,height=1,command=notice)

balance_btn.config(font=('Calibri',12))

balance_btn.grid(row=9,column=0,sticky='wens')


moneytransfer_btn=tk.Button(win,text='Перевод денег',bg='purple',fg='orange',bd=2,relief=tk.SUNKEN,width=12,height=1,command=money_transfer)

moneytransfer_btn.config(font=('Calibri',12))

moneytransfer_btn.grid(row=9,column=1,sticky='wens')


opera_btn=tk.Button(win,text='Д/В',bg='purple',width=5,bd=2,fg='orange',relief=tk.SUNKEN,height=1,command=updbalans)

opera_btn.config(font=('Calibri',12))

opera_btn.grid(row=9,column=2,sticky='wens',columnspan=2)

img3=PhotoImage(file='C:\Users\Администратор\Documents\Ex11\Wallet\card.png')

cards_btn=tk.Button(win,text='Мои карты',bg='purple',width=5,image=img3,bd=2,fg='orange',relief=tk.SUNKEN,height=20, compound='left',command=my_cards)

cards_btn.config(font=('Calibri',12))

cards_btn.grid(row=10,column=0,sticky='wens',columnspan=4)

#

date_now=datetime.datetime.now()

Empty1=tk.Label(win,bd=2,height=5,justify=tk.LEFT,bg='orange',fg='blue',anchor='w',text=f'''Дата и время:{date_now:%d-%m-%y %H:%M}\n#NabievAsliddin\nphone:200-94-91-91\nemail:aslnabiev2002@gmail.com''')

Empty1.config(font=('Arial',14,'bold'))

Empty1.grid(row=11,column=0,sticky='wens',columnspan=4)


win.mainloop()   

