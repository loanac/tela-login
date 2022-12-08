from tkinter import *
from tkinter import Tk, StringVar, ttk
from tkinter import messagebox
import tkinter
from PIL import Image, ImageTk 

# cores
cor1= "#203A43" #verde claro
cor2= "#0F2027" # escuro

#janela
log = Tk()
log.title("Login")
log.geometry("800x500")
log.iconbitmap("")
log.resizable(False,False)

#imagem da tela inicial 
bg_log = tkinter.PhotoImage(file='login.png')
bg_log.subsample(1,1)

b_log = Label(log,image=bg_log)
b_log.pack()



#acesso
credenciais = ['admin', '1234']

#funcao
def verificarSenha():
    nome = e_user.get()
    senha = e_passw.get()
    
    if nome == 'admin' and senha == '1234':
            telaInicio()
    elif credenciais[0] == nome and credenciais[1]== senha:
        telaInicio()
    else:
        messagebox.showwarning(title='Erro',message='verifique o usuário e senha')
        

        
        
#funcao apos verificação
# tela de opcao dps do login


    
def telaInicio():
    log.destroy()
    cadastro = Tk()
    cadastro.title("Tela Inicial")
    cadastro.geometry("800x500")
    cadastro.iconbitmap("")
    cadastro.resizable(False,False)
    
    bg_img = tkinter.PhotoImage(file='blog.png')
    bg_img.subsample(1,1)

    b_img = Label(cadastro,image=bg_img)
    b_img.pack()

    bt_cad = Button(cadastro,font=('Impact 14'),text="Bem vindo Admin",width=25, height=4, bg="#2C5364",fg="white",relief=GROOVE,cursor="hand2",overrelief=RIDGE)
    bt_cad.place(x=280,y=100)
        
    
    cadastro.mainloop()






# entradas 
e_user = Entry(width=10,justify='center',font=("",15),bg=cor2,fg="white",border=0)
e_user.place(x=350,y=260)

#senha
e_passw = Entry(width=10,justify='center',font=("",15),show="*", bg=cor2,fg="white",border=0)
e_passw.place(x=350,y=349)

#botao
entra = Button(font=('Ivy 8 bold'),command=verificarSenha,text="Entrar",width=9, height=2, bg=cor2,fg="white",relief=GROOVE,cursor="hand2",overrelief=RIDGE)
entra.place(x=370,y=405)
log.mainloop()
