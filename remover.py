#!/usr/bin/python
# -*- coding: latin-1 -*-
import os
from memento import Memento

class Removedor:
    def Remover():
        filename = (input('Qual arquivo deseja remover?'))
        user = os.getlogin()

        Memento.ExcluiMemento(filename)

        Undo = input('Arquivo excluido, deseja refazer a operacao? ')
        if Undo == 'S':
            Memento.RetornaMemento(filename)
        elif Undo == 'N':
            Memento.ExcluiPermanente(filename)

    def Notificar(self):
        if Memento.ExcluiMemento():
            return True