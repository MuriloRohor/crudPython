from classe import Musica


def cadastrarMusica():
    nome = input("- Nome da Musica: ")
    estilo = input("- Estilo: ")
    banda = input("- Banda/Arista:")
    ano = input("- Ano de Lançamento: ")
    link = input("- Link: ")
    novaMusica = Musica(nome, estilo, banda, ano, link)
    musica = {}
    musica['Nome'] = novaMusica.get_nome()
    musica['Estilo'] = novaMusica.get_estilo()
    musica['Banda'] = novaMusica.get_banda()
    musica['Ano'] = novaMusica.get_ano()
    musica['link'] = novaMusica.get_link()
    return musica


def excluirMusica():
    musica = input("Digite o nome da Musica que deseja excluir: ")
    return musica


def editarMusica():
    musica = {}
    musica['Nome'] = input("- Nome da Musica: ")
    musica['Estilo'] = input("- Estilo: ")
    musica['Banda'] = input("- Banda/Arista: ")
    musica['Ano'] = input("- Ano de Lançamento: ")
    musica['link'] = input("- Link: ")
    return musica


def selecionarMusica():
    musica = input("- Nome da Musica: ")
    return musica


def selecionarTodos():
    pass
