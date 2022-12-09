from leituraArquivo import *


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


def editar(dado: str):
    musicas = lerArquivo()
    musica = input("- Qual Musica Editar: ")
    for i, e in enumerate(musicas):
        if e['nome'] == musica:
            musicas[i] = dado
    salvarArquivo(musicas)


def selecionar(dado: str):
    musicas = lerArquivo()
    for i, e in enumerate(musicas):
        if e['nome'] == dado:
            return musicas[i]


def listar():
    return lerArquivo()
