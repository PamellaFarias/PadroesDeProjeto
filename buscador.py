#!/usr/bin/python
# -*- coding: latin-1 -*-
import fileinput
import sys
import os
#import Chainofresponsability
from Chainofresponsability import BancoIa, BancoMl, BancoPadroes
debug = True
class Buscador:
    def __init__(self,palavra):
        self.palavra = palavra
        lista = []
        self.lista = lista

    def Busca(self):
        user = os.getlogin()
        #Buscar no bancos
        larquivos = BancoIa.exibe(self.palavra)[0], BancoMl.exibe(self.palavra)[0], BancoPadroes.exibe(self.palavra)[0]
        bancos = BancoIa.exibe(self.palavra)[1], BancoMl.exibe(self.palavra)[1], BancoPadroes.exibe(self.palavra)[1]
        diretorios = BancoIa.diretorio(self.palavra), BancoMl.diretorio(self.palavra), BancoPadroes.diretorio(self.palavra)
        bancoscorrespondentes = []

        for i in range(len(larquivos)):
            dir = diretorios[i]
            for j in range(len(larquivos[i])):
                arquivo = larquivos[i][j]
                arq_path = os.path.join(dir, arquivo)
                ficheiro = open(arq_path, "r")
                for line in ficheiro.readlines():
                    if self.palavra in line and arquivo not in self.lista :
                        self.lista.append(arquivo)
                        ficheiro.close()
                        if i == 0:
                            bancoscorrespondentes.append(bancos[i])
                        elif i == 1:
                            bancoscorrespondentes.append(bancos[i])
                        elif i == 2:
                            bancoscorrespondentes.append(bancos[i])
                    else:
                        ficheiro.close()
        print("A Palavra:", self.palavra, "foi encontrada no(s) seguinte(s) documento(s):")
        for i in range (len(self.lista)):
            print(self.lista[i], "presente no",  bancoscorrespondentes[i])
