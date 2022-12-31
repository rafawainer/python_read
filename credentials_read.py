import json
import time
from datetime import datetime

import boto3
import dateutil.utils


def read_credentials():

    with open("files/aws_credentials.json", encoding='utf-8') as credentials_json:
        dados = json.load(credentials_json)

    type(dados)

    aws_access_key_id = dados['AWS_ACCESS_KEY']
    aws_secret_access_key = dados['AWS_SECRET_KEY']
    region_name = dados['AWS_REGION']

    print("AWS ACCESS KEY ID    : " + aws_access_key_id)
    print("AWS SECRET ACCESS KEY: " + aws_secret_access_key)
    print("AWS REGION           : " + region_name)

    return (aws_access_key_id, aws_secret_access_key, region_name)

def leitura_athena():

    credentials = read_credentials()

    data = datetime.now()
    datafinal = str(data.year) + str(data.month) + str(data.day) + "-" + str(data.hour) + str(data.minute) + str(data.second)

    athena_client = boto3.client(
        'athena',
        aws_access_key_id=credentials[0],
        aws_secret_access_key=credentials[1],
        region_name=credentials[2]
    )

    query_response = athena_client.start_query_execution(
        QueryString="SELECT * FROM accounts",
        QueryExecutionContext={"Database": "svr_test"},
        ResultConfiguration={
            "OutputLocation": "s3://rafawainer-athena/pyhtonQuery/Saida-{}.csv".format(datafinal),
            "EncryptionConfiguration": {"EncryptionOption": "SSE_S3"}
        },
    )

    while True:
        try:
            athena_client.get_query_results(
                QueryExecutionId=query_response["QueryExecutionId"]
            )
            break
        except Exception as err:
            if "Query has not yet finished" in str(err):
                time.sleep(0.001)
            else:
                raise err

    print("Query executada com sucesso")

if '__name__' == '__main__':
    read_credentials()
