#!/usr/bin/python
# -- coding: latin-1 --
import os, sys
from typing import List

'''
Bancos Chain vai receber do documento o tipo de banco e pode ser exibido em buscar documento.
'''


class BancosChain():
    def __init__(self, palavrasolicitada):
        self.palavrasolicitada = palavrasolicitada

    def handle(self, request):
        handled = self.processRequest(request)
        if not handled:
            self.nxt.handle(request)

    def processRequest(self, request):
        raise NotImplementedError('First implement it !')

class BancoIa(BancosChain):
    def __init__(self, palavrasolicitada):
        super().__init__(palavrasolicitada)
        self.palavrasolicitada = palavrasolicitada


    def exibe (self):
        nome = 'Banco IA'
        user = os.getlogin()
        dirPath = f"C:\\Users\\{user}\\Documents\\BancoIa"
        result = [f for f in os.listdir(dirPath) if os.path.isfile(os.path.join(dirPath, f))]
        return result,nome

    def diretorio(self):
        user = os.getlogin()
        dir = f"C:\\Users\\{user}\\Documents\\BancoIa"
        return dir

class BancoMl(BancosChain):
    def __init__(self, palavrasolicitada):
        super().__init__(palavrasolicitada)
        self.palavrasolicitada = palavrasolicitada

    def exibe (self):
        nome = 'Banco ML'
        user = os.getlogin()
        dirPath = f"C:\\Users\\{user}\\Documents\\BancoMl"
        result = [f for f in os.listdir(dirPath) if os.path.isfile(os.path.join(dirPath, f))]
        return result, nome

    def diretorio(self):
        user = os.getlogin()
        dir = f"C:\\Users\\{user}\\Documents\\BancoMl"
        return dir

class BancoPadroes(BancosChain):
    def __init__(self, palavrasolicitada):
        super().__init__(palavrasolicitada)
        self.nomebanco = palavrasolicitada


    def exibe (self):
        nome = 'Banco Padroes'
        user = os.getlogin()
        dirPath = f"C:\\Users\\{user}\\Documents\\BancoPadroes"
        result = [f for f in os.listdir(dirPath) if os.path.isfile(os.path.join(dirPath, f))]
        return result, nome

    def diretorio(self):
        user = os.getlogin()
        dir = f"C:\\Users\\{user}\\Documents\\BancoPadroes"
        return dir