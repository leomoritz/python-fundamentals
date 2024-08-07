from tkinter import *


def btn_click():
    print("Botão pressionado!")


janela_principal = Tk()
texto = Label(master=janela_principal, text="Hello World. It's me, Léo! :)")
# texto.place(x=50, y=100) para adicionar o texto na tela com as coordenadas definidas
texto.pack()  # apenas para adicionar o elemento na tela de forma centralizada e posicionada o mais perto do topo

pic = PhotoImage(file="python.png")
logo = Label(master=janela_principal, image=pic)
logo.pack()

botao = Button(master=janela_principal, text="Clique aqui", command=btn_click)
botao.pack()

janela_principal.mainloop()
