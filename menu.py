from telas import *
from funcao import *

def menu():
    limpar()
    print("-=-=-=-=- Musicas -=-=-=-=-")
    print("1 - Cadatrar Musica")
    print("2 - Editar Musica")
    print("3 - Excluir Musica")
    print("4 - Selecionar Musica")
    print("5 - Listar Musicas")
    print("6 - Sair")
    print("-=-=-=-=--=-=-=-=--=-=-=-=-")
    opcao = int(input("Digite a opção desejada: "))
    return opcao

while True:
    opcao = menu()
    if opcao == 1:
        musica = cadastrarMusica()
        criar(musica)
        exibirMensagem("Musica salva!")

    elif opcao == 2:
        nome = selecionarMusica()
        musica = editarMusica()
        edicao = editar(musica, nome)
        if edicao == None:
            exibirMensagem(f"Musica '{nome}' não foi encontrado")
        else:
            exibirMensagem(f"Musica {nome} editada!")

    elif opcao == 3:
        limpar()
        nome = selecionarMusica()
        musica = excluir(nome)
        if musica == None:
            exibirMensagem(f"Musica '{nome}' não foi encontrado")
        else:
            exibirMensagem(f"Musica {nome} excluida!")
        
    elif opcao == 4:
        nome = selecionarMusica()
        musica = selecionar(nome)
        limpar()
        if musica == None:
            exibirMensagem(f"Musica '{nome}' não foi encontrado")
        else:
            exibirMusica(musica)
            travar()

    elif opcao == 5:
        musicas = listar()
        listagem = selecionarMusicas(musicas)
    
    elif opcao == 6:
        break




