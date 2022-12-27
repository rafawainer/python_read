import csv


def leitura():

    arquivo = open("accounts_csv_downloaded.csv", "r", encoding='utf-8')
    registros = csv.DictReader(arquivo)

    for linhas in registros:
        print(linhas)

    arquivo.close()

if '__name__' == '__main__':
    leitura()
