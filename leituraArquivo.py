import json
import os.path

nome_arquivo = 'banco.json'


def lerArquivo():
    arquivo = open(nome_arquivo, 'r', encoding='utf-8')
    data = arquivo.read()
    data = json.loads(data)
    arquivo.close()

    return data


def salvarArquivo(dados):
    arquivo = open(nome_arquivo, 'w+', encoding='utf-8')
    data = json.dumps(dados, indent=4)
    arquivo.write(data)
    arquivo.close()
