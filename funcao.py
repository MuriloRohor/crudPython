from leituraArquivo import *
import os

def criar(dado: dict) -> dict:
    musicas = lerArquivo()
    musicas.append(dado)
    salvarArquivo(musicas)


def excluir(dado: str):
    musicas = lerArquivo()
    for musica in musicas:
        if musica['nome'] == dado:
            musicas.remove(musica)
            salvarArquivo(musicas)
            return dado
            
def editar(dado: str, musica):
    musicas = lerArquivo()
    for i, e in enumerate(musicas):
        if e['nome'] == musica:
            musicas[i] = dado
            salvarArquivo(musicas)
            return musica

def selecionar(dado: str):
    musicas = lerArquivo()
    for i, e in enumerate(musicas):
        if e['nome'] == dado:
            return musicas[i]

def listar():
    return lerArquivo()

def limpar():
    os.system('clear' if os.name == 'posix' else 'cls')

def travar():
    input("Digite ENTER para continuar...")

def exibirMensagem(msg):
    print(msg)
    travar()
    
