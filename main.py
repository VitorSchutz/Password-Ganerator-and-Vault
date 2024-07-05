from ntpath import join
import random
from tkinter import *
from tkinter import ttk
import string
import base64
import openpyxl
from openpyxl import Workbook

# Gerar Senha e Critografa-la

def Password():
    senha = gerar_senha()
    print(Encoded_Password)
    Passwordtext["text"] = Encoded_Password
    global SavePassword


    return senha

def gerar_senha(tamanho=12):

    global Encoded_Password

    caracteres = string.ascii_letters + string.digits
    Encoded_Password = ''.join(random.choice(caracteres) for i in range(tamanho))
    print(Encoded_Password)

    

    return 

# Criando a Interface do Usuario

window = Tk()
window.title("Password Generator")

BlankColunm = Label(window, text="")
BlankColunm.grid(column=3, row=1)

GeneratorBottom = Button(window, text="Ganerate a New Password", command= Password)
GeneratorBottom.grid(column=1, row=3)
Passwordtext = Label(window,text="")
Passwordtext.grid(column=2, row=3)

PasswordNameBox = Entry(window, bd=2, width=20, justify=CENTER)
PasswordNameBox.grid(column=2, row=1)

# Conseguindo as Informações da Interface
def get_data():
    
    global PasswordName
  
    PasswordName = str(PasswordNameBox.get())



    if PasswordName == "":
        print("Invalid Name.")
        invalid = Label(window, text="Invalid Name.")
        invalid.grid(column=4, row=4)
    else:
        invalid = Label(window, text="Password Saved.")
        invalid.grid(column=4, row=4)
        print("PasswordName Getted")

        PasswordDB = ("{0}: {1}").format(PasswordName, Encoded_Password)

        global DataBase

        DataBase = open("DataBase.txt", "a")
        DataBase.write(f"{PasswordDB}\n")
        DataBase.close()

    return


def OpenDataBase():

    PasswordVault = Tk()
    PasswordVault.title("My Passwords")

    
    DataBase = open("DataBase.txt", "r")
    read = DataBase.read()
    
    ShowInfo = Text(PasswordVault, height=20, borderwidth=0, font="arial, 12")
    ShowInfo.insert(1.0, f"{read}")
    ShowInfo.pack()

    ShowInfo.configure(state="disabled")
    ShowInfo.configure(inactiveselectbackground=ShowInfo.cget("selectbackground"))

    PasswordVault.mainloop()

    return

GetPasswordBottom = Button(window, text="Save Password to Vault", command= get_data)
GetPasswordBottom.grid(column=1, row=1)

ShowPassword = Button(window, text="Show All My Passwords", command= OpenDataBase)
ShowPassword.grid(column=4, row=1)


window.mainloop()

