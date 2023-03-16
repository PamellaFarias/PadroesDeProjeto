#!/usr/bin/python
# -- coding: latin-1 --
import os, sys
import PyPDF2

'''Converter pdf para txt
'''
"""
    Define o tipo de documento usado e receber o mesmo.
    """
class Pdf:

    def __init__(self, documentoleitura):
        self.documentoleitura = documentoleitura
    '''
    Recebe o documento salvo'''
    def ler_documento(self):
        user1 = os.getlogin()
        dir1 = f"C:\\Users\\{user1}\\Documents"
        arq_path1 = os.path.join(dir1, self.documentoleitura)
        with open(arq_path1, "rb") as pdf_file:
            read_pdf = PyPDF2.PdfFileReader(pdf_file)
            number_of_pages = read_pdf.getNumPages()
            page = read_pdf.pages[0]
            self.page_content = page.extractText()
"""
    Converter o documento de pdf para txt e gravar o mesmo.
    """

class Adapter(Pdf):

    def __init__(self,documentosaida,banco,documentoleitura):
        super().__init__(documentoleitura)
        self.documentosaida = documentosaida
        self.banco = banco

    def gravar_documento(self,):

        user2 = os.getlogin()
        if self.banco == "IA":
            dir2 = f"C:\\Users\\{user2}\\Documents\\BancoIa"
        elif self.banco == "ML":
            dir2 = f"C:\\Users\\{user2}\\Documents\\BancoMl"
        elif self.banco == "Padroes":
            dir2 = f"C:\\Users\\{user2}\\Documents\\BancoPadroes"
        arq_path2 = os.path.join(dir2, self.documentosaida)
        with open(arq_path2, 'w')  as self.documento:
            self.documento.write(self.page_content)
            return self.page_content

'''documentoleitura = input("digite o nome do documento que deseja converter em formato pdf\n")
pdf = Pdf(documentoleitura)
pdf.ler_documento()
documentosaida = input("digite o nome do documento que deseja salvar em formato txt\n")
banco = input("digite o nome do banco em que deseja salvar o documento com formato txt\n")
adapter = Adapter(documentosaida,banco,documentoleitura)
adapter.ler_documento()
adapter.gravar_documento()'''