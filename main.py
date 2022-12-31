from datetime import datetime

import credentials_read

# credentials = credentials_read.read_credentials() # leitura das chaves AWS
# read_file_json.leitura() #leitura de arquivo json
# read_athena.leitura(credentials) #leitura de arquivo a partir de acesso ao S3 da AWS
credentials_read.leitura_athena()

