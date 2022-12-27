import json


def read_credentials():
    aws_access_key_id = []
    aws_secret_access_key = []
    region_name = []

    with open("files/aws_credentials.json", encoding='utf-8') as credentials_json:
        dados = json.load(credentials_json)

        indice = 0

        for registros in dados:
            aws_access_key_id.append(registros['AWS_ACCESS_KEY'])
            aws_secret_access_key.append(registros['AWS_SECRET_KEY'])
            region_name.append(registros['AWS_REGION'])

            print("AWS ACCESS KEY ID    : " + aws_access_key_id[indice])
            print("AWS SECRET ACCESS KEY: " + aws_secret_access_key[indice])
            print("AWS REGION           : " + region_name[indice])
            indice += 1

    return aws_access_key_id, aws_secret_access_key, region_name


if '__name__' == '__main__':
    read_credentials()
