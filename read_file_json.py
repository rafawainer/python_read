import json


def leitura():

    quantidade_saida = 0

    with open("clientes_credores.json", encoding='utf-8') as arquivo_json:
        dados = json.load(arquivo_json)

        arquivo_saida = open("files/arquivo_saida.txt", "w", encoding='utf-8')

        for registro in dados:
            dados_saida = registro['nome'] + " tem " + registro['idade'] + " anos e mora na cidade de " + registro['cidade']

            arquivo_saida.write(dados_saida)
            quantidade_saida += 1

    print("Foram gerados {:03d} registros no arquivo de saida".format(quantidade_saida))


if __name__ == '__main__':
    leitura()
