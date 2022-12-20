from telas import *
from funcao import Funcao

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

funcao = Funcao()

while True:
    opcao = menu()

    if opcao == 1:
        musica = cadastrarMusica()
        funcao.criar(musica)
        exibirMensagem("Musica salva!")

    elif opcao == 2:
        nome = selecionarMusica()
        musica = editarMusica()
        edicao = funcao.editar(musica, nome)
        if edicao == True:
            exibirMensagem(f"Musica '{nome}' editada!")
        else:
            exibirMensagem(f"Musica '{nome}' não foi encontrado")
            
    elif opcao == 3:
        limpar()
        nome = selecionarMusica()
        funcao.excluir(nome)
        exibirMensagem(f"Musica '{nome}' excluida!")
        
    elif opcao == 4:
        nome = selecionarMusica()
        musica = funcao.selecionar(nome)
        limpar()
        if musica == None:
            exibirMensagem(f"Musica '{nome}' não foi encontrado")
        else:
            exibirMusica(musica)
            travar()

    elif opcao == 5:
        musicas = funcao.selecionar_todos()
        listagem = listarMusicas(musicas)
    
    elif opcao == 6:
        break




