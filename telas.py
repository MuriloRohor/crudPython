from musica import Musica
import os

def cadastrarMusica() -> Musica:
    limpar()
    print("-------- Cadastrar Musica --------")
    musica = Musica()
    musica.set_nome(input("- Nome da Musica: "))
    musica.set_estilo(input("- Estilo: "))
    musica.set_banda(input("- Banda/Artista: "))
    musica.set_ano(input("- Ano de Lançamento: "))
    musica.set_link(input("- Link: "))
    
    return musica

def editarMusica() -> Musica:
    limpar()
    print("-------- Editar Musica --------")
    musica = Musica()
    musica.set_nome(input("- Nome da Musica: "))
    musica.set_estilo(input("- Estilo: "))
    musica.set_banda(input("- Banda/Artista: "))
    musica.set_ano(input("- Ano de Lançamento: "))
    musica.set_link(input("- Link: "))
    return musica

def selecionarMusica():
    limpar()
    print("-------- Selecionar Musica --------")
    musica = input("- Nome da Musica: ")
    return musica

def listarMusicas(musicas):
    limpar()
    print("-------- Lista de Musicas --------")
    for musica in musicas:
        exibirMusica(musica)
    travar()

def exibirMusica(musica: Musica):
    print("-------- Musica --------")
    print(f"- Nome da Musica: {musica.get_nome()}")
    print(f"- Estilo: {musica.get_estilo()}")
    print(f"- Banda/Arista: {musica.get_banda()}")
    print(f"- Ano de Lançamento: {musica.get_ano()}")
    print(f"- Link: {musica.get_link()}")

def limpar():
    os.system('clear' if os.name == 'posix' else 'cls')

def travar():
    input("Digite ENTER para continuar...")

def exibirMensagem(msg):
    print(msg)
    travar()