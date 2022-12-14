from classe import Musica
from funcao import limpar, travar

def cadastrarMusica():
    limpar()
    print("-------- Cadastrar Musica --------")
    nome = input("- Nome da Musica: ")
    estilo = input("- Estilo: ")
    banda = input("- Banda/Arista:")
    ano = input("- Ano de Lançamento: ")
    link = input("- Link: ")
    novaMusica = Musica(nome, estilo, banda, ano, link)
    musica = {}
    musica['nome'] = novaMusica.get_nome()
    musica['estilo'] = novaMusica.get_estilo()
    musica['banda'] = novaMusica.get_banda()
    musica['ano'] = novaMusica.get_ano()
    musica['link'] = novaMusica.get_link()
    return musica

def editarMusica():
    limpar()
    print("-------- Editar Musica --------")
    musica = {}
    musica['nome'] = input("- Nome da Musica: ")
    musica['estilo'] = input("- Estilo: ")
    musica['banda'] = input("- Banda/Arista: ")
    musica['ano'] = input("- Ano de Lançamento: ")
    musica['link'] = input("- Link: ")
    return musica

def selecionarMusica():
    limpar()
    print("-------- Selecionar Musica --------")
    musica = input("- Nome da Musica: ")
    return musica

def selecionarMusicas(musicas):
    limpar()
    print("-------- Lista de Musicas --------")
    for musica in musicas:
        exibirMusica(musica)
    travar()

def exibirMusica(dado):
    print("-------- Musica --------")
    print(f"- Nome da Musica: {dado['nome']}")
    print(f"- Estilo: {dado['estilo']}")
    print(f"- Banda/Arista: {dado['banda']}")
    print(f"- Ano de Lançamento: {dado['ano']}")
    print(f"- Link: {dado['link']}")