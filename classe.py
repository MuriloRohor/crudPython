from leituraArquivo import *

class Musica:
    __nome: str
    __estilo: str
    __banda: str
    __ano: str
    __link: str

    def __init__(self, nome, estilo, banda, ano, link):
        self.__nome = nome
        self.__estilo = estilo
        self.__banda = banda
        self.__ano = ano
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