from builder import ConcreteBuilder
from Adapter import Adapter
from Adapter import Pdf


class Facade:
    opcao = int(input('Selecione a funcionalidade:\n 1 - Busca\n 2 - Download\n 3 - Excluir\n '))

    if opcao == 1:
        ConcreteBuilder.Buscar()
    elif opcao == 2:
        ConcreteBuilder.Download()
        documentoleitura = input("digite o nome do documento que deseja converter em formato pdf\n")
        pdf = Pdf(documentoleitura)
        pdf.ler_documento()
        documentosaida = input("digite o nome do documento que deseja salvar em formato txt\n")
        banco = input("digite o nome do banco em que deseja salvar o documento com formato txt\n")
        adapter = Adapter(documentosaida, banco, documentoleitura)
        adapter.ler_documento()
        adapter.gravar_documento()
    elif opcao == 3:
        ConcreteBuilder.Remover()

Facade()
