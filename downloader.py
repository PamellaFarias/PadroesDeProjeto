
import os
from urllib import response
import requests

class Downloader:
    def Download():
        user = os.getlogin()
        dir = f"C:\\Users\\{user}\\Documents"
        url = str(input('Insira o URL do arquivo desejado '))



        response = requests.get(url)
        if response.status_code == 200:
            arq_path = os.path.join(dir, os.path.basename(url))
            with open(arq_path, 'wb') as f:
                f.write(response.content)
            print('O Documento',os.path.basename(url), "foi salvo no formato pdf na pasta escolhida")
            print('O Documento', os.path.basename(url), 'agora pode ser convertido do formato pdf para txt, para isso basta digitar o nome dele abaixo')

    def Notificar(self):
        if Downloader.Download():
            return True