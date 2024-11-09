import socket
import threading
import tkinter
import tkinter.scrolledtext
from tkinter import simpledialog



HOST='127.0.0.1'
PORT=1111

class Client:
    def __init__(self,host,port):
        self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.connect((host,port))

        msg=tkinter.Tk()
        msg.withdraw()

        self.nickname=simpledialog.askstring("Ник","Пожалуйста, выберите ник",parent=msg)
        self.gui_done=False
        self.running=True
        gui_thread=threading.Thread(target=self.gui_loop)
        receive_thread=threading.Thread(target=self.receive)

        gui_thread.start()
        receive_thread.start()
        
    def gui_loop(self):
        self.win=tkinter.Tk()
        self.win.title("Freechat")
        self.win.geometry('1000x900')
        self.win.configure(bg="yellow")
        self.win.resizable(False,True)
        
       
        
        
        self.chat_l=tkinter.Label(self.win,text="ЧАТ:",bg="orange")
        self.chat_l.config(font=("Calibri",12))
        self.chat_l.pack(padx=20,pady=5)

        self.text_plc=tkinter.scrolledtext.ScrolledText(self.win)
        self.text_plc.pack(padx=20,pady=5)
        self.text_plc.config(state='disabled')

        self.msg_l=tkinter.Label(self.win,text="Сообщение:",bg="orange")
        self.msg_l.config(font=("Calibri",12))
        self.msg_l.pack(padx=20,pady=5)

        self.input_plc=tkinter.Text(self.win,height=3)
        self.input_plc.pack(padx=20,pady=5)

        self.send_btn=tkinter.Button(self.win,text="Отправить",bg='orange',command=self.write_msg)
        self.send_btn.config(font=("Calibri",12))
        self.send_btn.pack(padx=20,pady=5)

        self.gui_done=True
        self.win.protocol("WM_DELETE_WINDOW",self.stop)
        self.win.mainloop()
        
    def write_msg(self):
        message=f"{self.nickname}:{self.input_plc.get('1.0','end')}"
        self.sock.send(message.encode('utf-8'))
        self.input_plc.delete('1.0','end')
        
        
    def stop(self):
        self.running=False
        self.win.destroy()
        self.sock.close()
        exit(0)
        
        
        
    def receive(self):
        while self.running:
            try:
                message=self.sock.recv(1024)
                if message=='NICK':
                    self.sock.send(self.nickname.encode('utf-8'))
                else:
                    if self.gui_done:
                        self.text_plc.config(state='normal')
                        self.text_plc.insert('end',message)
                        self.text_plc.yview('end')
                        self.text_plc.config(state='disabled')
            except ConnectionAbortedError:
                break
            except:
                print("Ошибка")
                self.sock.close()
                break
            
client=Client(HOST,PORT)

        
     
    
        
        
        
       
            
   
    
            


