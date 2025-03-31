
from tkinter import *

window = Tk()

class App():

    def __init__(self):
        self.root= window
        self.tela()
        window.mainloop()

    def tela(self):
        self.root.title("Ficha de Cadastro")
        self.root.configure(background= 'gray')
        self.root.geometry("1024x780")
        self.root.maxsize(width=1024, height=780)
        self.root.minsize(width=780, height=400)
    


App()