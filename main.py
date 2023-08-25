import tkinter as tki
import _mysql_connector as ms
from time import sleep as s
from tkinter import *
from banco import conectar

class tela:
    def __init__(self, master=None):
         self.fonte = ("Verdana", "8")
         self.container1 = Frame(master)
         self.container1["pady"] = 10
         self.container1.pack()
         self.container2 = Frame(master)
         self.container2["padx"] = 20
         self.container2["pady"] = 5
         self.container2.pack()
         self.container3 = Frame(master)
         self.container3["padx"] = 20
         self.container3["pady"] = 5
         self.container3.pack()
         self.container4 = Frame(master)
         self.container4["padx"] = 20
         self.container4["pady"] = 5
         self.container4.pack()
         self.container5 = Frame(master)
         self.container5["padx"] = 20
         self.container5["pady"] = 5
         self.container5.pack()

         self.lblemail= Label(self.container1, text="E-mail:",
            font=self.fonte, width=10)
         self.lblemail.pack(side=LEFT)

         self.txtemail = Entry(self.container2)
         self.txtemail["width"] = 25
         self.txtemail["font"] = self.fonte
         self.txtemail.pack(side=LEFT)

         self.lblsenha= Label(self.container3, text="Senha:",
         font=self.fonte, width=10)
         self.lblsenha.pack(side=LEFT)

         self.txtsenha = Entry(self.container4)
         self.txtsenha["width"] = 25
         self.txtsenha["show"] = "*"
         self.txtsenha["font"] = self.fonte
         self.txtsenha.pack(side=LEFT)

         self.bntInsert = Button(self.container5, text="Inserir",
         font=self.fonte, width=12)
         self.bntInsert["command"] = self.consultarUser(self)
         self.bntInsert.pack (side=LEFT)
         

    def consultarUser(self):
        banc = conectar()
        banc.comando()
        
        
root = tki.Tk()
tela(root)
root.mainloop()