import boto3
from datetime import datetime
import os

# Configurações iniciais
bucket = "bucket-name"
perfil_aws = "defaut"
arquivo_original_movies = "movies.csv"
arquivo_original_series = "series.csv"

# Ajuste os caminhos para o diretório atual do script
local_path_movies = "/data/movies.csv"
local_path_series = "/data/series.csv"

# Data atual para o path
data_atual = datetime.now()
ano, mes, dia = data_atual.strftime("%Y"), data_atual.strftime("%m"), data_atual.strftime("%d")

# Cria uma sessão Boto3 usando o perfil AWS SSO
session = boto3.Session(profile_name=perfil_aws)

# Cria o cliente S3 a partir da sessão
s3 = session.client('s3')

# Função para upload
def upload_file(local_path, tipo, file_name):
    """
    Realiza o upload de um arquivo para o S3 seguindo o padrão de path.
    """
    key = f"Raw/Local/CSV/{tipo}/{ano}/{mes}/{dia}/{file_name}"
    s3.upload_file(local_path, bucket, key)
    print(f"Arquivo {local_path} enviado para s3://{bucket}/{key}")

# Executa o upload para filmes e séries
upload_file(local_path_movies, "Movies", arquivo_original_movies)
upload_file(local_path_series, "Series", arquivo_original_series)