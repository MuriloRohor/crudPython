from leituraArquivo import * 

class Musica:
    __nome: str
    __estilo: str
    __banda: str
    __data: str
    __link: str

    def __init__(self, nome, estilo, banda, data, link):
        self.__nome = nome
        self.__estilo = estilo
        self.__banda = banda
        self.__data = data
        self.__link = link
    
    def criar(self, dado: dict) -> dict:
        dados = lerArquivo()
        dados.append(dado)
        salvarArquivo(dados)

    def cadastrarMusica(self, nome, estilo, banda, data, link):
        self.__nome = nome
        self.__estilo = estilo
        self.__banda = banda
        self.__data = data
        self.__link = link






   
def cadastrarMusica():
    dados = Musica()
    print("-------- Cadastro de Musica --------")
    musica = {}
    musica['nome'] = input('Nome: ')
    musica['estilo'] = input('Estilo: ')
    musica['banda'] = input('Banda: ')
    musica['Data'] = input('Data: ')
    musica['Link'] = input('link: ')

    return musica   