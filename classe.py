from leituraArquivo import *

class Musica:
    __id: int
    __nome: str
    __estilo: str
    __banda: str
    __ano: str
    __link: str

    def set_nome(self, nome):
        self.__nome = nome

    def set_estilo(self, estilo):
        self.__estilo = estilo

    def set_banda(self, banda):
        self.__banda = banda

    def set_ano(self, ano):
        self.__ano = ano

    def set_link(self, link):
        self.__link = link
    
    def get_nome(self):
        return self.__nome

    def get_estilo(self):
        return self.__estilo

    def get_banda(self):
        return self.__banda

    def get_ano(self):
        return self.__ano

    def get_link(self):
        return self.__link

dados = Musica()

def get_musica():
    musica = {} 
    musica['Nome'] = dados.get_nome()
    musica['Estilo'] = dados.get_estilo()
    musica['Banda'] = dados.get_banda()
    musica['Ano'] = dados.get_ano()
    musica['link'] = dados.get_link()
    return musica

def set_musica():
    dados.set_nome(input("Nome da Musica: "))
    dados.set_estilo(input("Estilo da Musica: ")) 
    dados.set_banda(input("Banda/Artista da Musica: "))
    dados.set_ano(input("Ano de lançamento da Musica: "))
    dados.set_link(input("Link da Musica: "))
    

def menu():
    opcao = int(input("Digite a opção desejada: "))
    return opcao

def criar(dado: dict) -> dict:
    salvar = lerArquivo()
    salvar.append(dado)
    salvarArquivo(salvar)

while True:
    opcao = menu()

    if opcao == 1:
        adicionar = set_musica()
        criar(get_musica())