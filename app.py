
from tkinter import *

window = Tk()

class App():

# Função de loop para inicialização da janela
    def __init__(self):
        self.root= window
        self.tela()
        self.divisoes_da_tela()
        window.mainloop()
        

# Função para configurações de layout da janela
    def tela(self):
        self.root.title("Ficha de Cadastro")
        self.root.configure(background= 'gray')
        self.root.geometry("1024x880")
        self.root.maxsize(width=1024, height=880)
        self.root.minsize(width=780, height=400)

# Função para frames dentro da janela
    def divisoes_da_tela(self):

        #Configurações primeira section
        self.div_1 = Frame(self.root, bd=4, bg="white", highlightbackground="black", highlightthickness=1)
        self.div_1.place(relx=0.025, rely=0.04, relwidth=0.95, relheight=0.45)
        
        #Configurações segunda section
        self.div_2 = Frame(self.root, bd=4, bg="white", highlightbackground="black", highlightthickness=1)
        self.div_2.place(relx=0.025, rely=0.5, relwidth=0.95, relheight=0.45)
    


App()