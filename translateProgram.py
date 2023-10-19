from googletrans import Translator
#from tkinter import *
import copy
from customtkinter import *
from PIL import Image


"""Variáveis"""
dict_idiomas = {"Inglês": 'en', "Português": 'pt', "Francês": 'fr',
                'Alemão': 'de', "Italiano": "it", 'Japonês': 'ja',
                "Detectar Idioma": 'auto'}
lista_idiomas_dest = ["Inglês", "Português", "Francês", "Alemão", "Italiano", "Japonês"]
lista_idiomas_src = copy.deepcopy(lista_idiomas_dest)
lista_idiomas_src.append("Detectar Idioma")

id_src = 'auto'
id_dest = 'pt'


"""Funções"""
def idioma_origem(id):
    """Troca o idioma de origem de acordo com o menu de opções"""
    global id_src
    id_src = dict_idiomas[id]
    print(id_src)


def idioma_destino(id):
    """Troca o idioma de destino de acordo com o menu de opções"""
    global id_dest
    id_dest = dict_idiomas[id]
    print(id_dest)


def traduz():
    """recebe, traduz e retorna uma string de qualquer idioma para o português"""
    tO = texto_original.get("0.0", "end")
    tt = translator.translate(tO, src=id_src, dest=id_dest)

    texto_traduzido.delete("0.0", "end") #apaga o texto que já existe
    texto_traduzido.insert("0.0", tt.text) #insere o novo texto traduzido
    print(tt.text)


"""Main"""
translator = Translator()
janela = CTk()
janela.geometry("850x400")

set_appearance_mode("Dark")
set_default_color_theme("dark-blue")

img = CTkImage(Image.open("imagens/logotranslator.png"), size=(420, 62))
logo = CTkLabel(janela, image=img, text="")
logo.place(x=20, y=10)

titulo1 = CTkLabel(janela, text="Texto Original  →  Texto traduzido", font=("arial bold", 16), text_color="lightgray")
titulo1.place(x=315, y=85)

texto_original = CTkTextbox(janela, width=400, height=200, corner_radius=10)
texto_original.place(x=20, y=120)
texto_original.insert("0.0", "Hello World !")

texto_traduzido = CTkTextbox(janela, width=400, height=200, corner_radius=10)
texto_traduzido.place(x=430, y=120)

traduzir = CTkButton(janela, width=100, text="TRADUZIR", command=traduz)
traduzir.place(x=375 ,y=330)

src = CTkOptionMenu(janela, width=150,
                    values=lista_idiomas_src,
                    command=idioma_origem)
src.set("Detectar Idioma")
src.place(x=20, y=330)

dest = CTkOptionMenu(janela, width=150,
                     values=lista_idiomas_dest,
                     command=idioma_destino)
dest.set("Português")
dest.place(x=680, y=330)

janela.mainloop()