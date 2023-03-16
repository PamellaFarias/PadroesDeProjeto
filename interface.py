#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys
import tkinter
from tkinter import *
from abc import ABC, abstractmethod


class SubscriberJanela1:
    def __init__(self, toplevel):
        self.frame = Frame(toplevel)
        self.frame.pack()
        self.texto = Label(self.frame, text='Bem vindo ao organizador de arquivos!')
        self.texto['width'] = 50
        self.texto['height'] = 5
        self.texto.pack()
        self.botaosalvar= Button(self.frame, text='Salvar arquivo')
        self.botaosalvar['background'] = 'blue'
        self.botaosalvar.pack()
        self.botaobuscar = Button(self.frame, text='Buscar arquivo')
        self.botaobuscar['background'] = 'blue'
        self.botaobuscar.pack()
        self.botaoremover = Button(self.frame, text='Remover arquivo')
        self.botaoremover['background'] = 'blue'
        self.botaoremover.pack()
    
raiz = Tk()
SubscriberJanela1(raiz)
raiz.geometry("500x250+200+200")
raiz.resizable(True,True)

raiz.mainloop()