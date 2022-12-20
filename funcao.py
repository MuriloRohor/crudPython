from leituraArquivo import leituraArquivo
from musica import Musica
import os

class Funcao:
    __banco = leituraArquivo()


    def criar(self, dado: Musica) -> Musica:
        musicas = self.selecionar_todos()
        musicas.append(dado)
        self.__banco.salvarArquivo(list(map(lambda x: x.tooDict(), musicas)))


    def excluir(self, dado: str):
        musicas = self.selecionar_todos()
        for musica in musicas:
            if musica.get_nome() == dado:
                musicas.remove(musica)
        self.__banco.salvarArquivo(musicas)


                
    def editar(self, dado: str, musica):
        musicas = self.selecionar_todos()
        for i, e in enumerate(musicas):
            if e.get_nome() == musica:
                musicas[i] = dado
                self.__banco.salvarArquivo(list(map(lambda x: x.tooDict(), musicas)))
                return True


    def selecionar(self, dado: str):
        musicas = self.selecionar_todos()
        for i, e in enumerate(musicas):
            if e.get_nome() == dado:
                return musicas[i]

    def selecionar_todos(self):
        musicas = []
        for i in self.__banco.lerArquivo():
            musica = Musica()
            musica.set_nome(i['nome'])
            musica.set_estilo(i['estilo'])
            musica.set_banda(i['banda'])
            musica.set_ano(i['ano'])
            musica.set_link(i['link'])
            musicas.append(musica)
        return musicas

    def listar(self):
        return self.__banco.lerArquivo()


        
