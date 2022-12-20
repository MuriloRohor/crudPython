import json
import os.path

class leituraArquivo:

    __nome_arquivo = 'banco.json'


    def lerArquivo(self):
        arquivo = open(self.__nome_arquivo, 'r', encoding='utf-8')
        data = arquivo.read()
        if len(data) == 0:
            return []
        data = json.loads(data)
        arquivo.close()

        return data


    def salvarArquivo(self, dados):
        arquivo = open(self.__nome_arquivo, 'w+', encoding='utf-8')
        data = json.dumps(dados, indent=4)
        arquivo.write(data)
        arquivo.close()
