# 🚀 Projeto

Este projeto teve como objetivo aplicar, na prática, conceitos de **Engenharia de Dados**, **Cloud Computing** e **processamento distribuído**, utilizando serviços da AWS em conjunto com Python, Docker e PySpark.

A proposta consistiu na construção de um pipeline de dados completo em um **Data Lake na AWS**, realizando ingestão de dados locais e externos, armazenamento em camadas e automação de processos serverless.

Durante o desenvolvimento, foi possível compreender:

- Como estruturar um Data Lake utilizando o Amazon S3  
- Como automatizar ingestão de dados com AWS Lambda  
- Como consumir dados de APIs externas utilizando Python  
- Como utilizar Docker para empacotamento e execução da aplicação  
- Como organizar dados em camadas Raw, Processed e Curated  
- Como trabalhar com PySpark para processamento de grandes volumes de dados  
- Como integrar diferentes serviços da AWS em uma pipeline escalável  

Além da parte técnica, o projeto também envolveu análise de dados e geração de insights estratégicos utilizando informações coletadas da API do TMDB.

---

# 📌 Objetivo do Projeto

O projeto consiste em criar um pipeline de dados em um Data Lake na AWS, realizando:

- Ingestão de arquivos CSV locais para o Amazon S3  
- Integração com dados externos através da API do TMDB  
- Organização dos dados em camadas estruturadas  
- Automação do processo com AWS Lambda  
- Armazenamento de dados em formato estruturado no S3  
- Preparação dos dados para futuras análises e consultas  

A atividade simula um cenário real de engenharia de dados em nuvem, envolvendo ingestão, armazenamento, automação e enriquecimento de dados.

---

# ❓ Questões de Negócio

Durante o projeto, foram definidas as seguintes perguntas analíticas:

- Quais são os 10 filmes mais populares do gênero Drama/Romance de 2023/2024?
- Quais são os 10 filmes mais bem avaliados do gênero Drama/Romance de 2023/2024?
- Quais são os 10 filmes mais mal avaliados do gênero Drama/Romance de 2023/2024?

---

# 🧱 Arquitetura do Data Lake

O projeto foi estruturado utilizando o conceito de Data Lake em camadas:

````
Raw → Processed → Curated
````

## 🔹 Camadas

- **Raw:** armazenamento dos dados brutos vindos de arquivos CSV e da API TMDB  
- **Processed:** dados tratados, organizados e preparados para análises  
- **Curated:** dados refinados e prontos para consumo analítico  

---

# ⚙️ Tecnologias Utilizadas

- 🐍 Python  
- ⚡ PySpark  
- 🐳 Docker  
- ☁️ AWS S3  
- 🔄 AWS Lambda  
- 🔑 AWS CLI + SSO  
- 🎬 API TMDB  
- 🖥️ Máquina Virtual Linux  

---

# 📁 Estrutura do Projeto
````
Sprint 5/
│
├── Projeto/
│   ├── Etapa 1/
│   │   ├── upload_script.py
│   │   └──  Dockerfile
│   │
│   ├── Etapa 2/
│   │   ├── lambda_function.py
│   │   └── Dockerfile
│
├── Evidencias/
│
└── README.md
````

# 🔄 Etapas do Projeto

## 1. [Etapa I](/Sprint%205/Projeto/Etapa%201/upload_script.py) — Upload de arquivos locais para o S3 

Na primeira etapa foi realizada a criação do bucket no Amazon S3 e o upload dos arquivos `movies.csv` e `series.csv` para a camada Raw do Data Lake.

O processo foi automatizado utilizando um script Python executado através de um container Docker.

### O que foi desenvolvido

- Criação da estrutura inicial do Data Lake  
- Upload automatizado de arquivos CSV  
- Organização dos arquivos em diretórios baseados em data  
- Integração do Python com AWS S3 utilizando Boto3  
- Containerização da aplicação com Docker  

````python
import boto3
from datetime import datetime
import os

# Configurações iniciais
bucket = "bucket-name"
perfil_aws = "default"
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

````
### Dockerfile 

````dockerfile

# Usa a imagem oficial do Python 3.9 para o container.
FROM python:3.9-slim-buster

# Define o diretório de trabalho como /app.
WORKDIR /app

# Copia o script para o container.
COPY upload_script.py .

# Copia os arquivos de dados para o container, na pasta /data/.
COPY movies.csv /data/
COPY series.csv /data/

# Instala a biblioteca 'boto3'.
RUN pip install boto3

# Define o comando para rodar o script quando o container iniciar.
CMD ["python", "upload_script.py"]

````

### 📸 Evidências

#### Criação do Bucket
![amostra1](/Sprint%205/Evidencias/Projeto/00.png)
![amostra2](/Sprint%205/Evidencias/Projeto/01.png)
#### Build do Docker
![amostra3](/Sprint%205/Evidencias/Projeto/02.png)
#### Execução do Docker
![amostra4](/Sprint%205/Evidencias/Projeto/03.png)
#### Pasta Raw
![amostra5](/Sprint%205/Evidencias/Projeto/04.png)
#### Arquivo movie.csv
![amostra6](/Sprint%205/Evidencias/Projeto/05.png)
#### Arquivo serie.csv
![amostra7](/Sprint%205/Evidencias/Projeto/06.png)

---

### 2. [Etapa II](/Sprint%205/Projeto/Etapa2/lambda_function.py) — Integração com API TMDB utilizando AWS Lambda

Na segunda etapa foi desenvolvida uma função AWS Lambda responsável por consumir dados da API do TMDB e armazenar os resultados em formato JSON dentro do bucket S3.

A função realiza buscas automatizadas de filmes do gênero Drama/Romance dos anos de 2023 e 2024.

### O que foi desenvolvido

- Integração com a API do TMDB  
- Coleta automatizada de dados externos  
- Paginação de requisições da API  
- Armazenamento dos resultados em JSON  
- Organização automática dos arquivos no Data Lake  
- Utilização de AWS Lambda para execução serverless  
- Criação de camada Docker para suporte da função Lambda  

````python
import os
import json
import requests
import boto3
from datetime import datetime

# --- Função de Ingestão de Dados da API ---
# Esta função é responsável por se comunicar com a API do TMDB.
def get_movies_by_genre_and_year(api_key, year, genre_ids):
    """
    Busca todos os filmes de um ano e gênero específicos, paginando a API.
    A paginação é crucial para APIs que limitam o número de resultados por requisição.
    """
    all_movies = []
    page = 1
    total_pages = 1  # Inicia com 1, o valor real será atualizado após a primeira requisição.

    # O loop 'while' garante que todas as páginas de resultados sejam coletadas.
    while page <= total_pages:
        # Constrói a URL completa para a requisição, incluindo a chave da API e os parâmetros de busca.
        url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&language=pt-BR&sort_by=popularity.desc&primary_release_year={year}&with_genres={','.join(map(str, genre_ids))}&page={page}"
        
        try:
            # Faz a requisição HTTP GET para a API.
            response = requests.get(url)
            # Levanta um erro se a requisição não for bem-sucedida (ex: 404, 500).
            response.raise_for_status()
            # Converte a resposta JSON em um dicionário Python.
            data = response.json()
            
            # Adiciona os filmes da página atual à lista principal.
            all_movies.extend(data['results'])
            
            # Atualiza o número total de páginas a serem processadas.
            if 'total_pages' in data:
                total_pages = data['total_pages']
            
            print(f"Página {page}/{total_pages} do ano {year} processada.")
            
            # Avança para a próxima página no loop.
            page += 1
            
        except requests.exceptions.RequestException as e:
            # Captura erros de requisição, como problemas de conexão ou HTTP.
            print(f"Erro na requisição à API do TMDB na página {page} para o ano {year}: {e}")
            break # Interrompe o loop em caso de erro para evitar falhas repetidas.
            
    return all_movies

# --- Função Principal da AWS Lambda ---
# Esta é a função de entrada que a AWS Lambda irá executar.
def lambda_handler(event, context):
    """
    Função principal que será executada pela AWS Lambda.
    'event' e 'context' são parâmetros padrão passados pela AWS.
    """
    # 1. Configura a API e o S3
    # Obtém a chave da API de uma variável de ambiente, uma prática de segurança recomendada.
    tmdb_api_key = os.environ.get('TMDB_API_KEY')
    
    # Define o nome do bucket S3 de destino.
    bucket_name = "bucket-name"  
    
    # Cria um cliente S3 para interagir com o serviço. O Boto3 usa as credenciais do IAM Role da Lambda.
    s3_client = boto3.client('s3')

    # Verifica se a chave da API foi configurada corretamente.
    if not tmdb_api_key:
        print("Erro: A variável de ambiente 'TMDB_API_KEY' não está configurada.")
        # Retorna uma resposta de erro para a Lambda.
        return {
            'statusCode': 500,
            'body': json.dumps('Configuração de ambiente ausente.')
        }

    # 2. Define os parâmetros de busca
    genre_ids_to_search = [18, 10749]  # ID do gênero Drama (18) e Romance (10749).
    years_to_search = [2023, 2024] # Anos de interesse para a busca.
    all_movie_data = []

    # 3. Coleta os dados de todos os anos
    # Itera sobre a lista de anos para buscar os filmes.
    for year in years_to_search:
        print(f"\nColetando filmes de drama/romance do ano: {year}...")
        movies_for_year = get_movies_by_genre_and_year(tmdb_api_key, year, genre_ids_to_search)
        all_movie_data.extend(movies_for_year)

    # Verifica se a lista de dados está vazia antes de tentar salvar.
    if not all_movie_data:
        print("Nenhum dado encontrado para salvar.")
        return {
            'statusCode': 204, # Código HTTP 204 significa "No Content".
            'body': json.dumps('Nenhum dado encontrado.')
        }

    # 4. Salva os dados no S3 com o caminho padronizado
    # Obtém a data e hora atuais para criar a estrutura de pastas no S3 (formato Data Lake).
    data_atual = datetime.now()
    ano, mes, dia = data_atual.strftime("%Y"), data_atual.strftime("%m"), data_atual.strftime("%d")
    
    # Constrói o caminho completo do arquivo no S3.
    # O caminho é: Raw/TMDB/JSON/Ano/Mês/Dia/NomeDoArquivo.json
    file_path = f"Raw/TMDB/JSON/{ano}/{mes}/{dia}/movies_drama_romance_{years_to_search[0]}_{years_to_search[-1]}_{data_atual.strftime('%Y-%m-%d_%H-%M-%S')}.json"
    
    try:
        # Usa o cliente S3 para fazer o upload do objeto (o arquivo JSON).
        s3_client.put_object(
            Bucket=bucket_name,
            Key=file_path,
            # Converte a lista de filmes em uma string JSON formatada.
            Body=json.dumps(all_movie_data, indent=2, ensure_ascii=False),
            ContentType='application/json' # Define o tipo de conteúdo do arquivo.
        )
        print(f"Busca concluída. Total de filmes encontrados: {len(all_movie_data)}")
        print(f"Dados salvos com sucesso em s3://{bucket_name}/{file_path}")
        
        # Retorna uma resposta de sucesso para a Lambda, indicando que a função terminou bem.
        return {
            'statusCode': 200,
            'body': json.dumps('Dados da API do TMDB salvos com sucesso!')
        }
    except Exception as e:
        # Captura qualquer outro erro que possa ocorrer durante a operação do S3.
        print(f"Erro ao salvar dados no S3: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps(f"Erro na ingestão: {str(e)}")
        }
````
### Dockerfile da Layer Lambda

Foi utilizado um Dockerfile para criação da layer utilizada pela função Lambda.
````dockerfile
FROM amazonlinux:2023
RUN yum update -y
RUN yum install -y \
python3-pip \
zip
RUN yum -y clean all
````

### 📸 Evidências

#### Criação da Função Lambda
![amostra1](/Sprint%205/Evidencias/Projeto/07.png)
#### Codigo na Função Lambda
![amostra2](/Sprint%205/Evidencias/Projeto/08.png)
#### Execução do código
![amostra3](/Sprint%205/Evidencias/Projeto/09.png)
#### Detalhes da execução do código
![amostra4](/Sprint%205/Evidencias/Projeto/10.png)
#### Resultado do Log
![amostra5](/Sprint%205/Evidencias/Projeto/11.png)
#### Pasta TMDB criada
![amostra6](/Sprint%205/Evidencias/Projeto/12.png)
#### Arquivo .json salvo
![amostra7](/Sprint%205/Evidencias/Projeto/13.png)

---

# 📊 Resultados

- Estruturação completa de um Data Lake na AWS  
- Ingestão automatizada de arquivos CSV  
- Integração com dados externos via API  
- Organização dos dados em camadas  
- Automação serverless utilizando Lambda  
- Armazenamento eficiente em JSON no S3  
- Pipeline preparado para futuras análises analíticas  

---

# 🧠 Aprendizados

Durante o desenvolvimento do projeto, foi possível aprofundar conhecimentos em:

- Engenharia de Dados  
- Arquitetura de Data Lake  
- Integração com APIs REST  
- Automação com AWS Lambda  
- Manipulação de arquivos JSON e CSV  
- Uso do Amazon S3 com Boto3  
- Containerização com Docker  
- Organização de pipelines de ingestão de dados  
- Estruturação de projetos cloud-native  

---

# 🔮 Melhorias Futuras

- Processamento dos dados com AWS Glue  
- Criação de consultas analíticas utilizando Athena  
- Integração com QuickSight para dashboards  
- Automatização completa com Step Functions  
- Monitoramento com CloudWatch  
- Criação de camada Curated com dados refinados  
- Agendamento automático da Lambda com EventBridge  