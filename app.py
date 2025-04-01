
from tkinter import *

window = Tk()

class App():

# Função de loop para inicialização da janela
    def __init__(self):
        self.root= window
        self.tela()
        self.divisoes_da_tela()
        self.criacao_labels()
        self.criacao_botoes()
        window.mainloop()
        

# Função para configurações de layout da janela
    def tela(self):
        self.root.title("Ficha de Cadastro")
        self.root.configure(background= 'gray')
        self.root.geometry("1024x880")
        self.root.maxsize(width=1024, height=880)
        self.root.minsize(width=780, height=650)

# Função para frames dentro da janela
    def divisoes_da_tela(self):

        #Configurações primeira section
        self.div_1 = Frame(self.root, bd=4, bg="white", highlightbackground="black", highlightthickness=1)
        self.div_1.place(relx=0.025, rely=0.04, relwidth=0.95, relheight=0.45)
        
        #Configurações segunda section
        self.div_2 = Frame(self.root, bd=4, bg="white", highlightbackground="black", highlightthickness=1)
        self.div_2.place(relx=0.025, rely=0.5, relwidth=0.95, relheight=0.45)

# Função para botões da section 1
    def criacao_botoes(self):

        #Botão limpar
        self.btn_Limpar = Button(self.div_1, text="Limpar")
        self.btn_Limpar.place(relx=0.1, rely=0.06, relwidth=0.1, relheight=0.08)

        #Botão buscar
        self.btn_Buscar = Button(self.div_1, text="Buscar")
        self.btn_Buscar.place(relx=0.21, rely=0.06, relwidth=0.1, relheight=0.08)

        #Botão novo
        self.btn_Buscar = Button(self.div_1, text="Novo")
        self.btn_Buscar.place(relx=0.6, rely=0.06, relwidth=0.1, relheight=0.08)

        #Botão alterar
        self.btn_Buscar = Button(self.div_1, text="Alterar")
        self.btn_Buscar.place(relx=0.71, rely=0.06, relwidth=0.1, relheight=0.08)

        #Botão apagar
        self.btn_Buscar = Button(self.div_1, text="Apagar")
        self.btn_Buscar.place(relx=0.82, rely=0.06, relwidth=0.1, relheight=0.08)
    
    def criacao_labels(self):

        #Label e entry do Código
        self.lb_codigo = Label(self.div_1, text="Código", bg="white")
        self.lb_codigo.place(relx=0.005, rely=0.001, relwidth=0.07, relheight=0.08)

        self.input_codigo = Entry(self.div_1, highlightbackground="gray", highlightthickness=1)
        self.input_codigo.place(relx=0.02, rely=0.06, relwidth=0.07, relheight=0.08)

        #Label e entry do Nome
        self.lb_nome = Label(self.div_1, text="Nome", bg="white")
        self.lb_nome.place(relx=0.005, rely=0.3, relwidth=0.07, relheight=0.08)

        self.input_nome = Entry(self.div_1, highlightbackground="gray", highlightthickness=1)
        self.input_nome.place(relx=0.02, rely=0.38, relwidth=0.9, relheight=0.08)

        #Label e entry do Telefone
        self.lb_telefone = Label(self.div_1, text="Telefone", bg="white")
        self.lb_telefone.place(relx=0.006, rely=0.6, relwidth=0.07, relheight=0.08)

        self.input_telefone = Entry(self.div_1, highlightbackground="gray", highlightthickness=1)
        self.input_telefone.place(relx=0.02, rely=0.68, relwidth=0.35, relheight=0.08)

        #Label e entry do Cidade
        self.lb_cidade = Label(self.div_1, text="Cidade", bg="white")
        self.lb_cidade.place(relx=0.485, rely=0.6, relwidth=0.07, relheight=0.08)

        self.input_cidade = Entry(self.div_1, highlightbackground="gray", highlightthickness=1)
        self.input_cidade.place(relx=0.5, rely=0.68, relwidth=0.35, relheight=0.08)



App()