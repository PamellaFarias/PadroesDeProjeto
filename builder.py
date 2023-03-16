#!/usr/bin/python
# -- coding: latin-1 --
import buscador
import downloader
import remover
import os
import memento
from abc import ABC, abstractmethod
import buscador
from buscador import Buscador
from memento import Memento

'''DIRETOR É IMPLEMENTADO NA FACHADA, QUE DEFINE A ORDEM
DE INICIALIZAÇÃO DE CADA MÓDULO'''


class Builder(ABC):

    def Buscar(self) -> None:
        pass

    def Download(self) -> None:
        pass

    def Remover(self) -> None:
        pass

    def ExcluiMemento(self) -> None:
        pass

    def RetornaMemento(self) -> None:
        pass

    def ExcluiPermanente(self) -> None:
        pass


class ConcreteBuilder:

    def Buscar():
        palavra = input("Digite a palavra-chave que deseja buscar nos bancos: ")
        buscador = Buscador(palavra)
        buscador.Busca()

    def Download():
        return downloader.Downloader.Download()

    def Remover():
        return remover.Removedor.Remover()

    def ExcluiMemento():
        return memento.Memento.ExcluiMemento()

    def RetornaMemento():
        return memento.Memento.RetornaMemento()

    def ExcluirPermamente():
        return memento.Memento.ExcluiPermanente()