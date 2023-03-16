from abc import ABC, abstractmethod
import downloader
import remover

class Observador(ABC):

    @abstractmethod
    def update(self):
        pass

class ConcreteObserver1:
    def update(self):
        if downloader.Downloader.Notificar() == True:
            return True

class ConcreteObserver2:
    def update(self):
        if remover.Removedor.Notificar() == True:
            return True