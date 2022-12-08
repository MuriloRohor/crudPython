from telas import *
from funcao import *


def menu():
    print("-=-=-=-=- Musicas -=-=-=-=-")
    print("1 - Cadatrar Musica")
    print("2 - Editar Musica")
    print("3 - Excluir Musica")
    print("4 - Selecionar Musica")
    print("5 - Listar Musicas")
    print("Pressione 'S' para sair")
    print("-=-=-=-=--=-=-=-=--=-=-=-=-")
    opcao = int(input("Digite a opção desejada: "))
    return opcao


while True:
    opcao = menu()
    if opcao == 1:
        musica = cadastrarMusica()
        criar(musica)

    if opcao == 2:
        musica = editarMusica()
        editar(musica)

    if opcao == 3:
        musica = excluirMusica()
        excluir(musica)

    if opcao == 4:
        musica = selecionarMusica()
        selecionar(musica)
