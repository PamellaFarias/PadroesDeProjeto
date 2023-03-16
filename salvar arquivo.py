import os
class salvar_arquivo:
    def __init__(self,name):
        self.name = name
    def salvar(self,localentrada,localsaida):
        os.popen(f"copy {src} {destination}")

#main
s1 = salvar_arquivo('pdf')
src = input("Enter src filename:")
destination = input("Enter target filename:")
s1.salvar(src,destination)

