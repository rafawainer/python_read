import time
import boto3

def leitura():

    AWS_ACCESS_KEY = "AWS_ACCESS_KEY"
    AWS_SECRET_KEY = "AWS_SECRET_KEY"
    AWS_REGION = "us-east-1"

    athena_client = boto3.client(
        "athena",
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
        region_name=AWS_REGION
    )

    query_response = athena_client.start_query_execution(
        QueryString="SELECT * FROM database",
        QueryExecutionContext={"Database": SCHEMA_NAME},
        ResultConfiguration={
            "OutputLocation": "queryResultFromBoto3",
            "EncryptionConfiguration": {"EncryptionOption": "SSE_S3"},
        },
    )

    while True:
        try:
            athena_client.get_query_results(
                QueryExecutionId=query_response["QueryExecutionId"]
            )
            break
        except Exception as err:
            if "not yet comlpeted" in str(err):
                time.sleep(0.001)
            else:
                raise err

if '__name__' == '__main__':
    leitura()
