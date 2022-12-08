from leituraArquivo import *


def criar(dado: dict) -> dict:
    musicas = lerArquivo()
    musicas.append(dado)
    salvarArquivo(musicas)


def excluir(dado: str):
    musicas = lerArquivo()
    for musica in musicas:
        if musica['Nome'] == dado:
            musicas.remove(musica)
    salvarArquivo(musicas)


def editar(dado: str):
    musicas = lerArquivo()
    musica = input("- Qual Musica Editar: ")
    for i, e in enumerate(musicas):
        if e['Nome'] == musica:
            musicas[i] = dado
    salvarArquivo(musicas)


def selecionar(dado: str):
    musicas = lerArquivo()
    musica = dado
    for i, e in enumerate(musicas):
        if e['Nome'] == musica:
            return i


def listar():
    return lerArquivo()
