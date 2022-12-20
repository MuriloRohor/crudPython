from leituraArquivo import *

class Musica:
    __nome: str
    __estilo: str
    __banda: str
    __ano: str
    __link: str

    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome

    def get_estilo(self):
        return self.__estilo
    
    def set_estilo(self, estilo):
        self.__estilo = estilo

    def get_banda(self):
        return self.__banda

    def set_banda(self, banda):
        self.__banda = banda

    def get_ano(self):
        return self.__ano
    
    def set_ano(self, ano):
        self.__ano = ano

    def get_link(self):
        return self.__link 

    def set_link(self, link):
        self.__link = link

    def tooDict(self):
        return {
            'nome': self.__nome,
            'estilo': self.__estilo,
            'banda': self.__banda,
            'ano': self.__ano,
            'link': self.__link
        }