# 🚀 Projeto

Este projeto teve como objetivo realizar a etapa final do pipeline de dados desenvolvido ao longo das sprints anteriores, focando no consumo e visualização das informações através do AWS QuickSight.

Nesta sprint, os dados estruturados na camada Refined foram utilizados para construção de dashboards analíticos interativos, permitindo transformar dados processados em insights estratégicos e visuais.

O processo envolveu integração entre Athena, AWS Glue e QuickSight, possibilitando consultas otimizadas sobre arquivos Parquet armazenados no Amazon S3.

Durante o desenvolvimento, foi possível compreender:

- Como consumir dados analíticos utilizando AWS QuickSight  
- Como conectar o QuickSight ao Athena  
- Como utilizar views SQL para facilitar análises analíticas  
- Como estruturar dashboards interativos e KPIs  
- Como criar visualizações estratégicas utilizando gráficos e filtros  
- Como transformar dados refinados em storytelling visual  
- Como integrar Athena, Glue e QuickSight em um fluxo analítico completo  

Além da parte técnica, o projeto também envolveu construção de indicadores de negócio voltados para análise de filmes do gênero Drama/Romance.

---

# 📌 Objetivo do Projeto

O projeto consiste em consumir os dados da camada Refined e transformá-los em dashboards analíticos no AWS QuickSight, realizando:

- Criação de views analíticas no Athena  
- Construção de datasets para visualização  
- Desenvolvimento de dashboards interativos  
- Criação de KPIs estratégicos  
- Implementação de filtros dinâmicos  
- Estruturação de storytelling visual para análise dos dados  

A atividade simula um cenário real de Business Intelligence e Analytics em Cloud Computing.

---

# ❓ Questões de Negócio

Durante o projeto, foram definidas as seguintes perguntas analíticas:

- Quais décadas possuem maior quantidade de filmes Drama/Romance?
- Quais décadas apresentam os filmes mais bem avaliados?
- Quais anos tiveram maior quantidade de filmes com avaliações relevantes?
- Quais são os filmes mais populares de 2023 e 2024?
- Quais são os filmes mais bem avaliados de 2023 e 2024?
- Quais são os filmes mais mal avaliados de 2023 e 2024?

---

### Principais entregas:  
- Dashboard no QuickSight conectado ao **Athena (Refined Zone)**.  
- Diferentes visualizações representando **indicadores de negócio**.  
- Inclusão de **filtros e controles interativos** para explorar os dados.  
- Criação de **KPIs** para destacar métricas críticas de desempenho.  
- Estruturação de um **storytelling coerente** para responder às principais perguntas de negócio.  

---

# ⚙️ Tecnologias Utilizadas

- ☁️ AWS Athena  
- 📊 AWS QuickSight  
- 🗂️ AWS Glue Data Catalog  
- 🪣 Amazon S3  
- ⚡ SQL  
- 📁 Apache Parquet  

---

# 📁 Estrutura do Projeto
````

# 🚀 Projeto

Este projeto teve como objetivo aplicar conceitos de **Engenharia de Dados**, **Cloud Computing** e **automação de pipelines**, utilizando serviços da AWS integrados com Python, Docker e APIs externas.

O projeto simulou um cenário real de construção de um **Data Lake na AWS**, envolvendo ingestão de dados locais e externos, armazenamento em camadas e automação de processos serverless.

Durante o desenvolvimento, foi possível compreender:

- Como estruturar um Data Lake utilizando Amazon S3  
- Como automatizar ingestão de dados com Python e Boto3  
- Como consumir dados externos através da API do TMDB  
- Como utilizar AWS Lambda para execução serverless  
- Como organizar dados em camadas Raw, Processed e Curated  
- Como containerizar aplicações utilizando Docker  
- Como integrar diferentes serviços AWS em um pipeline automatizado  
- Como transformar dados brutos em informações analíticas  

Além da parte técnica, o projeto também permitiu desenvolver habilidades analíticas através da definição de perguntas de negócio e interpretação dos dados coletados.

---

# 📌 Objetivo do Projeto

O projeto consiste em criar um pipeline de dados em um Data Lake na AWS, realizando a ingestão de arquivos CSV locais para o Amazon S3 (camada Raw), integração com dados externos por meio da API do TMDB, e organização das informações em camadas estruturadas.

O objetivo principal foi simular um ambiente real de engenharia de dados, demonstrando domínio sobre:

- Ingestão de dados  
- Armazenamento em nuvem  
- Processamento automatizado  
- Integração com APIs  
- Arquitetura de Data Lake  
- Automação serverless  
- Análise e geração de insights  

---

# ❓ Questões de Negócio

- Quais são os 10 filmes mais populares do gênero Drama/Romance de 2023 e 2024?  
- Quais são os 10 filmes mais bem avaliados do gênero Drama/Romance de 2023 e 2024?  
- Quais são os 10 filmes mais mal avaliados do gênero Drama/Romance de 2023 e 2024?  

---

# 🧱 Arquitetura do Data Lake

O projeto foi estruturado utilizando o modelo de camadas:

```text
Raw → Processed → Curated
```

### 🔹 Camadas

- **Raw:** armazenamento dos dados brutos vindos de arquivos CSV e da API TMDB  
- **Processed:** dados tratados, organizados e enriquecidos  
- **Curated:** dados refinados e preparados para análises e consultas  

---

# ⚙️ Tecnologias Utilizadas

- 🐍 Python  
- ☁️ AWS S3  
- ⚡ AWS Lambda  
- 🐳 Docker  
- 🔗 API TMDB  
- 📦 Boto3  
- 📄 JSON  
- 📊 CSV  

---

# 🔄 Etapas do Projeto

---

## 1. Etapa I — Upload de Arquivos CSV para o S3

### Arquivos

- [Python](/Sprint%205/Desafio/Etapa%201/upload_script.py)  
- [Dockerfile](/Sprint%205/Desafio/Etapa%201/dockerfile)  

Na primeira etapa foi realizada a criação do bucket no Amazon S3 e o upload dos arquivos `movies.csv` e `series.csv` para a camada Raw do Data Lake.

O processo foi automatizado utilizando um script Python executado através de um container Docker.

### O que foi desenvolvido

- Criação da estrutura inicial do Data Lake  
- Upload automatizado de arquivos CSV  
- Organização dos arquivos em diretórios baseados em data  
- Integração do Python com AWS S3 utilizando Boto3  
- Containerização da aplicação com Docker  

### Evidências

#### Criação do Bucket

![amostra1](/Sprint%205/Evidencias/Desafio/00.png)
![amostra2](/Sprint%205/Evidencias/Desafio/01.png)

#### Build do Docker

![amostra3](/Sprint%205/Evidencias/Desafio/02.png)

#### Execução do Docker

![amostra4](/Sprint%205/Evidencias/Desafio/03.png)

#### Estrutura da camada Raw

![amostra5](/Sprint%205/Evidencias/Desafio/04.png)

#### Arquivo movies.csv

![amostra6](/Sprint%205/Evidencias/Desafio/05.png)

#### Arquivo series.csv

![amostra7](/Sprint%205/Evidencias/Desafio/06.png)

---

## 2. Etapa II — Integração com API TMDB utilizando AWS Lambda

### Arquivo

- [Lambda Function](/Sprint%205/Desafio/Etapa2/lambda_function.py)  

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

### Dockerfile da Layer Lambda

Foi utilizado um Dockerfile para criação da layer utilizada pela função Lambda.

### Evidências

#### Criação da Função Lambda

![amostra1](/Sprint%205/Evidencias/Desafio/07.png)

#### Código da Função Lambda

![amostra2](/Sprint%205/Evidencias/Desafio/08.png)

#### Execução da Função

![amostra3](/Sprint%205/Evidencias/Desafio/09.png)

#### Detalhes da Execução

![amostra4](/Sprint%205/Evidencias/Desafio/10.png)

#### Logs da Execução

![amostra5](/Sprint%205/Evidencias/Desafio/11.png)

#### Estrutura criada no Bucket

![amostra6](/Sprint%205/Evidencias/Desafio/12.png)

#### Arquivo JSON salvo no S3

![amostra7](/Sprint%205/Evidencias/Desafio/13.png)

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

---

# 🔙 Voltar

[Readme - Sprint 5](/Sprint%205/README.md)

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

`
Raw → Processed → Curated


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
`
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


# 🔄 Etapas do Projeto

## 1. [Etapa I](/Sprint%205/Projeto/Etapa%201/upload_script.py) — Upload de arquivos locais para o S3 

Na primeira etapa foi realizada a criação do bucket no Amazon S3 e o upload dos arquivos movies.csv e series.csv para a camada Raw do Data Lake.

O processo foi automatizado utilizando um script Python executado através de um container Docker.

### O que foi desenvolvido

- Criação da estrutura inicial do Data Lake  
- Upload automatizado de arquivos CSV  
- Organização dos arquivos em diretórios baseados em data  
- Integração do Python com AWS S3 utilizando Boto3  
- Containerização da aplicação com Docker  

`python
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

### Dockerfile 

`dockerfile

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

`python
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

### Dockerfile da Layer Lambda

Foi utilizado um Dockerfile para criação da layer utilizada pela função Lambda.
`dockerfile
FROM amazonlinux:2023
RUN yum update -y
RUN yum install -y \
python3-pip \
zip
RUN yum -y clean all


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

assim ficou bom?

Sim, ficou muito bom.
O README está com aparência de projeto profissional e já demonstra várias competências técnicas importantes de Engenharia de Dados e Cloud.

Os pontos mais fortes:

Estrutura organizada e fácil de navegar

Introdução clara e objetiva

Explicação técnica sem ficar excessivamente complexa

Separação das etapas do projeto

Uso de listas para destacar aprendizados e tecnologias

Arquitetura do Data Lake explicada corretamente

Contextualização do problema de negócio

Boa documentação das evidências

Organização visual muito superior ao README comum

Alguns detalhes que deixariam ainda mais profissional:

✅ Pequenos ajustes recomendados
1. Padronizar nomes das etapas
Você alterna entre:

Etapa I

Etapa II

Etapa2

Tente manter tudo igual:

Etapa 1
Etapa 2
ou

Etapa I
Etapa II
2. Corrigir pequenos detalhes gramaticais
Exemplo:

Além da parte técnica, o projeto também envolveu análise de dados...
Em vez de:

Alem da parte técnica...
Outro:

Código na Função Lambda
em vez de:

Codigo na Função Lambda
Esses detalhes passam mais profissionalismo.

3. Melhorar a seção de Resultados
Você pode deixar mais "impactante":

Em vez de:

- Pipeline preparado para futuras análises analíticas
Pode usar:

- Pipeline estruturado para futuras análises analíticas e escalabilidade do projeto
4. Melhorar a seção de Aprendizados
Ela já está boa, mas você pode dividir:

## ☁️ Cloud Computing
- AWS S3
- AWS Lambda
- Organização de Data Lake

## 🐍 Engenharia de Dados
- ETL
- Manipulação de JSON e CSV
- Integração com APIs

## 🐳 DevOps
- Docker
- Containerização
Fica com aparência ainda mais técnica.

✅ O que esse README transmite para recrutadores/professores
Ele mostra que você sabe:

Estruturar documentação técnica

Organizar pipelines de dados

Trabalhar com cloud

Integrar APIs

Automatizar processos

Usar Docker

Criar projetos escaláveis

Pensar em arquitetura de dados

Explicar tecnicamente um projeto

Isso é muito valioso para:

estágio em dados

engenharia de dados

cloud

backend

analytics engineering

MLOps futuramente

✅ Sobre os códigos expostos
O que você mostrou está seguro para GitHub público, desde que:

NÃO tenha:

API Key real

Access Key AWS

Secret Key AWS

Tokens

.env

credenciais

ARN sensível

IDs privados

Você já substituiu coisas importantes por:

bucket-name
default
Isso está correto.

✅ Sugestão profissional futura
Depois você pode adicionar:

# ▶️ Como executar o projeto
com:

docker build

docker run

configuração AWS

variáveis de ambiente

Isso deixa o projeto ainda mais próximo de padrão profissional/open source.

Seu README já está acima da média para projetos acadêmicos.


## Projeto

**Projeto:** Este Projeto trouxe uma experiência prática voltada para a construção da camada Trusted em um data lake utilizando AWS Glue e Apache Spark. O objetivo foi integrar e padronizar os dados oriundos da Raw Zone, garantindo que estivessem limpos, confiáveis e prontos para análises no AWS Athena.

Durante a execução, foram criados dois jobs no Glue para processar diferentes origens: arquivos CSV e dados da API TMDB. A configuração incluiu a definição do tipo de worker, quantidade mínima de nós e controle de timeout, sempre com foco na otimização de custos. Por fim, os dados foram persistidos no formato Parquet, com particionamento por data de ingestão no Amazon S3, garantindo performance e organização para consultas analíticas.


# Etapas

### 1. [Etapa I](/Sprint%206/Projeto/Etapa%201/CSV.py)

Na Primeira etapa, houve a criação da função no IAM e a realização do Script, no AWS Glue, responsável por passar os arquivos Movie.csv e Series.csv para formato Parquet

`python

# Importa as bibliotecas necessárias para as funções do AWS Glue, PySpark e Spark SQL.
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, regexp_replace, trim
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType

# Obtém o nome do job a partir dos argumentos passados para o job do Glue. Este é um código padrão do Glue.
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

# Inicializa os contextos do Spark e do Glue.
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)

# Inicializa o job com o nome do job.
job.init(args['JOB_NAME'], args)

# --- Define os caminhos S3 para entrada e saída ---
# Estes caminhos apontam para o bucket 'Raw' do S3 para os dados de origem (arquivos CSV).
input_filmes_path = "s3://data-lake-yanmacedo/Raw/Local/CSV/Movies/"
input_series_path = "s3://data-lake-yanmacedo/Raw/Local/CSV/Series/"

# Estes caminhos apontam para o bucket 'Trusted' do S3, onde os dados transformados serão armazenados no formato Parquet.
output_filmes_path = "s3://data-lake-yanmacedo/Trusted/CSV/Parquet/Movies/"
output_series_path = "s3://data-lake-yanmacedo/Trusted/CSV/Parquet/Series/"

# --- Define os esquemas para os DataFrames ---
# Define um esquema para os dados de 'filmes'. Isso define explicitamente os nomes das colunas e os tipos de dados.
# Usar um esquema de antemão melhora o desempenho e garante a consistência dos dados.
schema_filmes = StructType([
    StructField("id", IntegerType(), True),
    StructField("tituloPincipal", StringType(), True),
    StructField("tituloOriginal", StringType(), True),
    StructField("anoLancamento", StringType(), True),
    StructField("tempoMinutos", StringType(), True),
    StructField("genero", StringType(), True),
    StructField("notaMedia", StringType(), True),
    StructField("numeroVotos", StringType(), True),
    StructField("generoArtista", StringType(), True),
    StructField("personagem", StringType(), True),
    StructField("nomeArtista", StringType(), True),
    StructField("anoNascimento", StringType(), True),
    StructField("anoFalecimento", StringType(), True),
    StructField("profissao", StringType(), True),
    StructField("titulosMaisConhecidos", StringType(), True)
])

# Define um esquema para os dados de 'séries'. É muito semelhante ao esquema de filmes, mas inclui
# uma coluna 'anoTermino'.
schema_series = StructType([
    StructField("id", IntegerType(), True),
    StructField("tituloPincipal", StringType(), True),
    StructField("tituloOriginal", StringType(), True),
    StructField("anoLancamento", StringType(), True),
    StructField("anoTermino", StringType(), True),
    StructField("tempoMinutos", StringType(), True),
    StructField("genero", StringType(), True),
    StructField("notaMedia", StringType(), True),
    StructField("numeroVotos", StringType(), True),
    StructField("generoArtista", StringType(), True),
    StructField("personagem", StringType(), True),
    StructField("nomeArtista", StringType(), True),
    StructField("anoNascimento", StringType(), True),
    StructField("anoFalecimento", StringType(), True),
    StructField("profissao", StringType(), True),
    StructField("titulosMaisConhecidos", StringType(), True)
])

# --- Função Principal de Processamento de Dados ---
# Esta função encapsula toda a lógica de ETL (Extração, Transformação, Carregamento).
# Ela recebe os caminhos de entrada e saída, e um esquema como argumentos, tornando-a reutilizável.
def process_data(input_path, output_path, schema):
    # Lê os dados CSV do S3 para um Spark DataFrame.
    # - `header=True` informa ao Spark que a primeira linha é um cabeçalho.
    # - `sep="|"` especifica o delimitador de barra vertical.
    # - `nullValue='\\N'` lida corretamente com valores nulos representados por '\N'.
    # - `schema=schema` aplica o esquema pré-definido.
    df = spark.read.csv(input_path, header=True, sep="|", nullValue='\\N', schema=schema)

    # Verifica se uma coluna precisa ser renomeada. Isso lida com uma possível discrepância nos nomes das colunas.
    if "tituloPincipal" in df.columns:
        df = df.withColumnRenamed("tituloPincipal", "tituloPrincipal")

    # Realiza a limpeza de dados e a conversão de tipos.
    # Esta é a lógica central de transformação do script.
    df = df \
        .withColumn("anoLancamento", regexp_replace(col("anoLancamento"), "[^0-9]", "").cast(IntegerType())) \
        .withColumn("tempoMinutos", regexp_replace(col("tempoMinutos"), "[^0-9]", "").cast(IntegerType())) \
        .withColumn("genero", trim(col("genero")).cast(StringType())) \
        .withColumn("notaMedia", regexp_replace(col("notaMedia"), "[^0-9.]", "").cast(FloatType())) \
        .withColumn("numeroVotos", regexp_replace(col("numeroVotos"), "[^0-9]", "").cast(IntegerType())) \
        .withColumn("anoNascimento", regexp_replace(col("anoNascimento"), "[^0-9]", "").cast(IntegerType())) \
        .withColumn("anoFalecimento", regexp_replace(col("anoFalecimento"), "[^0-9]", "").cast(IntegerType()))
    # `regexp_replace(col("..."), "[^0-9]", "")` remove quaisquer caracteres não numéricos da string.
    # `.cast(IntegerType())` então converte a string limpa para um inteiro, o que é uma prática comum para lidar com dados numéricos sujos de uma fonte baseada em string.
    # O mesmo padrão é aplicado para `FloatType()` (para `notaMedia`) e `StringType()` (para `genero`).

    # Imprime o esquema do DataFrame transformado para verificar os novos tipos de dados.
    df.printSchema()

    # Escreve o DataFrame transformado para o caminho de saída no S3.
    # - `mode("overwrite")` garante que quaisquer dados existentes no caminho sejam substituídos.
    # - `.parquet(output_path)` escreve os dados no formato eficiente Parquet.
    df.write.mode("overwrite").parquet(output_path)

# --- Executa o Job ---
# Chama a função de processamento tanto para filmes quanto para séries.
process_data(input_filmes_path, output_filmes_path, schema_filmes)
process_data(input_series_path, output_series_path, schema_series)

# Comita o job para finalizar o processo e liberar os recursos.
job.commit()


### Evidencias do codigo

* Função IAM
![amostra1](/Sprint%206/Evidencias/Projeto/01.png)
![amostra2](/Sprint%206/Evidencias/Projeto/02.png)
* Script Glue
![amostra3](/Sprint%206/Evidencias/Projeto/03.png)
![amostra4](/Sprint%206/Evidencias/Projeto/04.png)
![amostra5](/Sprint%206/Evidencias/Projeto/05.png)
![amostra6](/Sprint%206/Evidencias/Projeto/08.png)
* Camada Trusted
![amostra7](/Sprint%206/Evidencias/Projeto/10.png)
![amostra8](/Sprint%206/Evidencias/Projeto/11.png)
![amostra9](/Sprint%206/Evidencias/Projeto/12.png)
![amostra10](/Sprint%206/Evidencias/Projeto/13.png)

---

### 2. [Etapa II](/Sprint%206/Projeto/Etapa2/JSON.py)

Na segunda etapa foi realizado o Script responsável por passar o arquivo .json para formato Parquet

`python

# Importa as bibliotecas necessárias para o AWS Glue e PySpark.
# `getResolvedOptions` para obter os argumentos do job.
# `col` e `concat_ws` para manipulação de colunas e concatenação de strings.
# `StructType`, `StructField` e os tipos de dados para definir o esquema.
import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, concat_ws
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType, BooleanType, DateType, ArrayType

# Obtém o nome do job a partir dos argumentos passados para o job do Glue.
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

# Inicializa o Spark e o GlueContext.
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# --- Define os caminhos S3 para entrada e saída ---
# Caminho de entrada para os dados JSON brutos do TMDB.
input_file = "s3://data-lake-yanmacedo/Raw/TMDB/"
# Caminho de saída para os dados transformados, salvos no formato Parquet.
output_parquet = "s3://data-lake-yanmacedo/Trusted/JSON/Parquet/"

# --- Define o esquema para o DataFrame de filmes do TMDB ---
# O esquema é crucial para garantir que os dados sejam lidos com os tipos corretos,
# incluindo tipos específicos como `BooleanType`, `DateType` e `ArrayType`.
schema_filmes = StructType([
    StructField("id", IntegerType(), True),
    StructField("adult", BooleanType(), True),
    StructField("backdrop_path", StringType(), True),
    StructField("original_language", StringType(), True),
    StructField("original_title", StringType(), True),
    StructField("overview", StringType(), True),
    StructField("popularity", FloatType(), True),
    StructField("poster_path", StringType(), True),
    StructField("release_date", DateType(), True),
    StructField("title", StringType(), True),
    StructField("video", BooleanType(), True),
    StructField("vote_average", FloatType(), True),
    StructField("vote_count", IntegerType(), True),
    StructField("genre_ids", ArrayType(IntegerType()), True)
])

# --- Função Principal de Processamento de Dados ---
# Esta função realiza a lógica de Extração, Transformação e Carregamento (ETL).
def process_data(input_path, output_path, schema):
    # Lê os dados JSON do S3 em um DataFrame do Spark.
    # A opção `multiLine` é usada para lidar com arquivos JSON onde um único registro pode ocupar várias linhas.
    # O esquema pré-definido garante a tipagem correta dos dados durante a leitura.
    df = spark.read.option("multiLine", "true").schema(schema).json(input_path)

    # Transforma o array de IDs de gênero (`genre_ids`) em uma única string,
    # com os IDs separados por vírgula. Isso facilita o armazenamento e consulta em Parquet.
    df = df.withColumn("genre_ids", concat_ws(",", col("genre_ids")))

    # Imprime o esquema final do DataFrame para verificar se as transformações foram aplicadas.
    df.printSchema()

    # Mostra as 5 primeiras linhas do DataFrame para inspeção,
    # com `truncate=False` para exibir o conteúdo completo das colunas.
    df.show(5, truncate=False)
    
    # Escreve o DataFrame transformado para o caminho de saída no S3.
    # O modo "overwrite" substitui qualquer dado existente no caminho,
    # e o formato Parquet é escolhido pela sua eficiência de armazenamento e consulta.
    df.write.mode("overwrite").parquet(output_path)

# --- Executa o Job ---
# Chama a função principal para iniciar o processo de ETL.
process_data(input_file, output_parquet, schema_filmes)

# Comita o job para finalizar a execução e liberar os recursos.
job.commit()



### Evidencias do codigo

* Script Glue
![amostra1](/Sprint%206/Evidencias/Projeto/06.png)
![amostra1](/Sprint%206/Evidencias/Projeto/07.png)
![amostra1](/Sprint%206/Evidencias/Projeto/09.png)
* Camada Trusted
![amostra1](/Sprint%206/Evidencias/Projeto/14.png)


poderia padronizar esse readme no mesmo modelo dos anteriores, ignore as partes que tiverem
a fim de nao dar quebra na formatação

# 🚀 Projeto

Este projeto teve como objetivo aplicar, na prática, conceitos de **Engenharia de Dados**, **processamento distribuído** e **Cloud Computing**, utilizando AWS Glue, Apache Spark e Amazon S3 para construção da camada Trusted de um Data Lake.

A proposta consistiu em transformar e padronizar dados oriundos da camada Raw, garantindo maior qualidade, organização e eficiência para futuras consultas analíticas utilizando AWS Athena.

Durante o desenvolvimento, foi possível compreender:

- Como utilizar AWS Glue para criação de pipelines ETL  
- Como processar grandes volumes de dados com Apache Spark  
- Como realizar transformações de dados utilizando PySpark  
- Como estruturar dados em um Data Lake utilizando Amazon S3  
- Como converter arquivos CSV e JSON para o formato Parquet  
- Como definir schemas explícitos para controle de tipagem  
- Como otimizar armazenamento e performance utilizando particionamento e formato colunar  
- Como integrar diferentes serviços da AWS em pipelines de dados escaláveis  

Além da parte técnica, o projeto também reforçou conceitos de organização de dados confiáveis para consumo analítico na camada Trusted.

---

# 📌 Objetivo do Projeto

O projeto consiste em construir a camada Trusted de um Data Lake na AWS, realizando:

- Leitura de dados da camada Raw  
- Tratamento e padronização de dados  
- Conversão de arquivos CSV e JSON para Parquet  
- Processamento distribuído com Apache Spark  
- Persistência otimizada dos dados no Amazon S3  
- Preparação dos dados para consultas analíticas no AWS Athena  

A atividade simula um cenário real de engenharia de dados, envolvendo pipelines ETL, processamento distribuído e organização de dados para analytics.

---

# 🧱 Arquitetura do Data Lake

O projeto foi estruturado utilizando o conceito de Data Lake em camadas:

Raw → Trusted → Curated

## 🔹 Camadas

- **Raw:** armazenamento dos dados brutos provenientes de arquivos CSV e APIs  
- **Trusted:** dados tratados, padronizados e convertidos para formatos otimizados  
- **Curated:** camada destinada aos dados refinados para consumo analítico  

---

# ⚙️ Tecnologias Utilizadas

- 🐍 Python  
- ⚡ Apache Spark / PySpark  
- ☁️ AWS Glue  
- 🪣 Amazon S3  
- 🔐 AWS IAM  
- 📊 AWS Athena  
- 🐳 Docker  
- 🖥️ Linux  

---

# 📁 Estrutura do Projeto
Sprint 6/
│
├── Projeto/
│ ├── Etapa 1/
│ │ └── CSV.py
│ │
│ ├── Etapa 2/
│ │ └── JSON.py
│
├── Evidencias/
│
└── README.md


---

# 🔄 Etapas do Projeto

## 1. [Etapa I](/Sprint%206/Projeto/Etapa%201/CSV.py) — Processamento de arquivos CSV para Parquet

Na primeira etapa foi realizado o desenvolvimento de um Job no AWS Glue responsável pelo processamento dos arquivos `Movies.csv` e `Series.csv`, convertendo-os da camada Raw para a camada Trusted no formato Parquet.

Também foi necessária a criação da função IAM para concessão das permissões utilizadas pelo AWS Glue durante o processamento.

### O que foi desenvolvido

- Criação da Role IAM para o Glue  
- Desenvolvimento de Job ETL no AWS Glue  
- Leitura de arquivos CSV no Amazon S3  
- Definição explícita de schemas utilizando PySpark  
- Limpeza e padronização dos dados  
- Conversão de tipos de dados  
- Escrita dos dados no formato Parquet  
- Organização dos arquivos na camada Trusted  

### 📸 Evidências

#### Função IAM
![amostra1](/Sprint%206/Evidencias/Projeto/01.png)
![amostra2](/Sprint%206/Evidencias/Projeto/02.png)

#### Script Glue
![amostra3](/Sprint%206/Evidencias/Projeto/03.png)
![amostra4](/Sprint%206/Evidencias/Projeto/04.png)
![amostra5](/Sprint%206/Evidencias/Projeto/05.png)
![amostra6](/Sprint%206/Evidencias/Projeto/08.png)

#### Camada Trusted
![amostra7](/Sprint%206/Evidencias/Projeto/10.png)
![amostra8](/Sprint%206/Evidencias/Projeto/11.png)
![amostra9](/Sprint%206/Evidencias/Projeto/12.png)
![amostra10](/Sprint%206/Evidencias/Projeto/13.png)

---

## 2. [Etapa II](/Sprint%206/Projeto/Etapa2/JSON.py) — Processamento de arquivos JSON para Parquet

Na segunda etapa foi desenvolvido um Job no AWS Glue responsável pelo processamento dos arquivos JSON oriundos da API TMDB, convertendo-os para o formato Parquet e armazenando-os na camada Trusted.

O processo utilizou PySpark para leitura, transformação e escrita dos dados de forma distribuída.

### O que foi desenvolvido

- Leitura de arquivos JSON no Amazon S3  
- Definição de schemas estruturados  
- Tratamento de arrays e colunas complexas  
- Transformação de dados utilizando PySpark  
- Conversão dos dados para Parquet  
- Organização dos arquivos na camada Trusted  
- Processamento distribuído utilizando Apache Spark  

### 📸 Evidências

#### Script Glue
![amostra1](/Sprint%206/Evidencias/Projeto/06.png)
![amostra2](/Sprint%206/Evidencias/Projeto/07.png)
![amostra3](/Sprint%206/Evidencias/Projeto/09.png)

#### Camada Trusted
![amostra4](/Sprint%206/Evidencias/Projeto/14.png)

---

# 📊 Resultados

- Construção da camada Trusted do Data Lake  
- Padronização dos dados provenientes da camada Raw  
- Conversão eficiente para formato Parquet  
- Estruturação dos dados para consultas analíticas  
- Processamento distribuído utilizando Apache Spark  
- Organização otimizada dos dados no Amazon S3  
- Pipeline preparado para integração com AWS Athena  

---

# 🧠 Aprendizados

Durante o desenvolvimento do projeto, foi possível aprofundar conhecimentos em:

## ☁️ Cloud Computing
- AWS Glue  
- Amazon S3  
- AWS IAM  
- AWS Athena  

## ⚡ Processamento Distribuído
- Apache Spark  
- PySpark  
- Transformações distribuídas de dados  

## 🐍 Engenharia de Dados
- ETL  
- Conversão de formatos de arquivos  
- Padronização de dados  
- Manipulação de schemas  
- Estruturação de Data Lakes  

## 🐳 DevOps e Infraestrutura
- Docker  
- Ambientes Linux  
- Organização de pipelines de dados  

---

# 🔮 Melhorias Futuras

- Criação da camada Curated do Data Lake  
- Integração com AWS Athena para consultas SQL  
- Criação de dashboards analíticos com QuickSight  
- Automatização dos Jobs com EventBridge  
- Monitoramento com CloudWatch  
- Particionamento avançado dos dados  
- Integração com AWS Glue Catalog  

## Projeto

**Projeto – Entrega 4 (Camada Refined):**  
Nesta etapa, estruturamos os dados da Trusted Zone para compor a **Refined Zone**, pronta para análises e dashboards no QuickSight.  

Principais entregas:  
- Criação da tabela fato (fato_filmes) consolidando dados da Trusted Local e TMDB.  
- Geração das dimensões: **Tempo**, **Gênero**, **Avaliação**, **Popularidade** e **Origem**.  
- Implementação de views no Athena para análises de filmes de Drama/Romance.  
- Persistência em **Parquet** no S3, garantindo compressão e leitura eficiente. 

# Etapas

### 1. [Etapa I](/Sprint%207/Projeto/Modelo%20Dimencional.png)

Na Primeira etapa, houve a criação do modelo dimencional, que mostra como os dados irão ser manipulados

### Evidencias

![amostra1](/Sprint%207/Evidencias/01.png)

---

### 2. [Etapa II](/Sprint%207/Projeto/scriptRefined.py)

Na segunda etapa foi realizado o Script responsável por desenvolver a camada Refined, com os arquivos da tabela fato e das dimensões

`python
# Importação de bibliotecas necessárias do AWS Glue e PySpark
import sys
from awsglue.utils import getResolvedOptions 
from pyspark.context import SparkContext
from awsglue.context import GlueContext  
from awsglue.job import Job
from pyspark.sql.functions import col, lit, when, split, explode, floor 

# Recupera o nome do Job passado como argumento
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

# Inicializa o Spark e Glue
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Cria e inicializa o job Glue
job = Job(glueContext)
job.init(args['JOB_NAME'], args)


# =============================
# 1. Leitura da origem LOCAL
# =============================
input_path_local = "s3://data-lake-yanmacedo/Trusted/Local/Parquet/Movies/2025/09/01/"
df_local = spark.read.parquet(input_path_local)

# Seleciona e padroniza as colunas necessárias
df_local_selected = df_local.select(
    col("id").cast("int"),
    col("tituloPrincipal"),
    col("tituloOriginal"),
    col("anoLancamento").cast("int"),
    col("genero"),
    col("notaMedia").cast("float"),
    col("numeroVotos").cast("int")
).withColumn("origem", lit("Local"))  # Adiciona coluna de origem

# Filtra apenas filmes do gênero Drama ou Romance
df_local_filtered = df_local_selected.filter(
    (col("genero").rlike("(?i)Drama")) | (col("genero").rlike("(?i)Romance"))
)


# =============================
# 2. Leitura da origem TMDB
# =============================
input_path_tmdb = "s3://data-lake-yanmacedo/Trusted/TMDB/Parquet/2025/09/01/"
df_tmdb = spark.read.parquet(input_path_tmdb)

# Seleciona e padroniza colunas, incluindo popularidade
df_tmdb_selected = df_tmdb.select(
    col("id").cast("int"),
    col("tituloPrincipal"),
    col("tituloOriginal"),
    col("anoLancamento").cast("int"),
    col("genero"),
    col("notaMedia").cast("float"),
    col("numeroVotos").cast("int"),
    col("popularidade").cast("int")
).withColumn("origem", lit("TMDB"))  # Marca origem como TMDB


# =============================
# 3. União dos datasets
# =============================

# Para a origem Local, adiciona a coluna popularidade (não existe nos dados locais)
df_local_final = df_local_filtered.withColumn("popularidade", lit(None).cast("int"))

# Mantém TMDB como está
df_tmdb_final = df_tmdb_selected

# Junta os dois datasets em um único DataFrame
df_union = df_local_final.unionByName(df_tmdb_final)

# Remove duplicatas
df_clean = df_union.dropDuplicates([
    "id", "tituloPrincipal", "tituloOriginal",
    "anoLancamento", "genero", "notaMedia", "numeroVotos", "origem"
])


# =============================
# 4. Criação das dimensões
# =============================

# Dimensão Tempo (ano, década e século)
dim_tempo = df_clean.select("anoLancamento") \
    .dropDuplicates() \
    .withColumnRenamed("anoLancamento", "ano") \
    .withColumn("decada", (floor(col("ano")/10)*10).cast("int")) \
    .withColumn("seculo", (floor(col("ano")/100)+1).cast("int"))

# Dimensão Gênero (explode quebra filmes com múltiplos gêneros em várias linhas)
dim_genero = df_clean \
    .withColumn("genero_individual", explode(split(col("genero"), ","))) \
    .select(col("genero_individual").alias("genero")) \
    .dropDuplicates()

# Dimensão Avaliação (classificação baseada na nota média)
dim_avaliacao = df_clean.select("notaMedia").dropDuplicates().withColumn(
    "categoria",
    when(col("notaMedia") < 4, "Ruim")
    .when((col("notaMedia") >= 4) & (col("notaMedia") < 6), "Médio")
    .when((col("notaMedia") >= 6) & (col("notaMedia") < 8), "Bom")
    .when(col("notaMedia") >= 8, "Excelente")
)

# Dimensão Popularidade (classificação por faixas)
dim_popularidade = df_clean.select("popularidade") \
    .dropna() \
    .dropDuplicates() \
    .withColumn("categoria",
        when(col("popularidade") < 100, "Baixa")
        .when((col("popularidade") >= 100) & (col("popularidade") < 500), "Média")
        .when((col("popularidade") >= 500) & (col("popularidade") < 1000), "Alta")
        .when(col("popularidade") >= 1000, "Muito Alta")
    )

# Dimensão Origem (Local ou TMDB)
dim_origem = df_clean.select("origem").dropDuplicates()


# =============================
# 5. Impressão para debug
# =============================
print("======= Fato Filmes =======")
df_clean.printSchema()
df_clean.show(5, truncate=False)

print("======= Dimensão Tempo =======")
dim_tempo.printSchema()
dim_tempo.show(5, truncate=False)

print("======= Dimensão Gênero =======")
dim_genero.printSchema()
dim_genero.show(5, truncate=False)

print("======= Dimensão Avaliação =======")
dim_avaliacao.printSchema()
dim_avaliacao.show(5, truncate=False)

print("======= Dimensão Popularidade =======")
dim_popularidade.printSchema()
dim_popularidade.show(5, truncate=False)

print("======= Dimensão Origem =======")
dim_origem.printSchema()
dim_origem.show(5, truncate=False)


# =============================
# 6. Escrita na camada Refined
# =============================

# Caminho base no S3
output_base = "s3://data-lake-yanmacedo/Refined/"

# Grava fato e dimensões em formato parquet
df_clean.write.mode("overwrite").parquet(output_base + "Fato_Filmes/")
dim_tempo.write.mode("overwrite").parquet(output_base + "Dim_Tempo/")
dim_genero.write.mode("overwrite").parquet(output_base + "Dim_Genero/")
dim_avaliacao.write.mode("overwrite").parquet(output_base + "Dim_Avaliacao/")
dim_popularidade.write.mode("overwrite").parquet(output_base + "Dim_Popularidade/")
dim_origem.write.mode("overwrite").parquet(output_base + "Dim_Origem/")

# Finaliza o job Glue
job.commit()



### Evidencias do codigo

* Script Glue
![amostra1](/Sprint%207/Evidencias/04.png)
![amostra1](/Sprint%207/Evidencias/05.png)
* Camada Trusted
![amostra1](/Sprint%207/Evidencias/12.png)
![amostra1](/Sprint%207/Evidencias/13.png)
![amostra1](/Sprint%207/Evidencias/14.png)
![amostra1](/Sprint%207/Evidencias/15.png)
![amostra1](/Sprint%207/Evidencias/16.png)
* Outputs
![amostra1](/Sprint%207/Evidencias/06.png)
![amostra1](/Sprint%207/Evidencias/07.png)
![amostra1](/Sprint%207/Evidencias/08.png)
![amostra1](/Sprint%207/Evidencias/09.png)
![amostra1](/Sprint%207/Evidencias/10.png)
![amostra1](/Sprint%207/Evidencias/11.png)

---

### 3. [Etapa III](/Sprint%207/Projeto/scriptRefined.py)

Na terceira etapa foi realizado do Crawler que pega os dados do S3 e passa para a Database

### Evidencias do codigo

* Criação da Database e do Crawler
![amostra1](/Sprint%207/Evidencias/02.png)
![amostra1](/Sprint%207/Evidencias/03.png)
* Execução do Crawler
![amostra1](/Sprint%207/Evidencias/17.png)
![amostra1](/Sprint%207/Evidencias/18.png)
* Selects de cada tabela
![amostra1](/Sprint%207/Evidencias/19.png)
![amostra1](/Sprint%207/Evidencias/20.png)
![amostra1](/Sprint%207/Evidencias/21.png)
![amostra1](/Sprint%207/Evidencias/22.png)
![amostra1](/Sprint%207/Evidencias/23.png)
![amostra1](/Sprint%207/Evidencias/24.png)


---

### 4. [Etapa IV](/Sprint%207/Projeto/scriptRefined.py)

Por ultimo foram desenvolvido algumas Views que respondem as perguntas propostas no inicio do Projeto

* Filmes mais populares de Drama/Romance em 2024
`sql
CREATE OR REPLACE VIEW vw_top10_populares_2024 AS
SELECT 
    tituloPrincipal,
    anoLancamento,
    genero,
    popularidade,
    origem
FROM "AwsDataCatalog"."db_deteste"."fato_filmes"
WHERE anoLancamento = 2024
  AND (genero LIKE '%Drama%' OR genero LIKE '%Romance%')
ORDER BY popularidade DESC
LIMIT 10;


* Filmes com mais avaliações (mais votos) de Drama/Romance em 2024
`sql
CREATE OR REPLACE VIEW vw_top10_mais_avaliados_2024 AS
SELECT 
    tituloPrincipal,
    anoLancamento,
    genero,
    numeroVotos,
    origem
FROM "AwsDataCatalog"."db_deteste"."fato_filmes"
WHERE anoLancamento = 2024
  AND (genero LIKE '%Drama%' OR genero LIKE '%Romance%')
ORDER BY numeroVotos DESC
LIMIT 10;


* Filmes mais bem avaliados de Drama/Romance em 2024
`sql
CREATE OR REPLACE VIEW vw_top10_bem_avaliados_2024 AS
SELECT 
    tituloPrincipal,
    anoLancamento,
    genero,
    notaMedia,
    origem
FROM "AwsDataCatalog"."db_deteste"."fato_filmes"
WHERE anoLancamento = 2024
  AND (genero LIKE '%Drama%' OR genero LIKE '%Romance%')
  AND numeroVotos > 50 -- filtro para evitar filmes sem relevância
ORDER BY notaMedia DESC
LIMIT 10;


* Filmes mais mal avaliados de Drama/Romance em 2024
`sql
CREATE OR REPLACE VIEW vw_top10_mal_avaliados_2024 AS
SELECT 
    tituloPrincipal,
    anoLancamento,
    genero,
    notaMedia,
    origem
FROM "AwsDataCatalog"."db_deteste"."fato_filmes"
WHERE anoLancamento = 2024
  AND (genero LIKE '%Drama%' OR genero LIKE '%Romance%')
  AND numeroVotos > 50 -- evita filmes obscuros
ORDER BY notaMedia ASC
LIMIT 10;


### Evidencias do codigo

* Views
![amostra1](/Sprint%207/Evidencias/25.png)
![amostra1](/Sprint%207/Evidencias/26.png)
![amostra1](/Sprint%207/Evidencias/27.png)
![amostra1](/Sprint%207/Evidencias/28.png)




poderia arrumar esse README assim como os anteriores.
ignore as partes com 
``para nao dar quebra de formatação

🚀 Projeto
Este projeto teve como objetivo aplicar, na prática, conceitos de Modelagem Dimensional, Data Warehousing, AWS Athena, AWS Glue e engenharia de dados analítica, construindo a camada Refined de um Data Lake na AWS.

A proposta consistiu em transformar os dados da Trusted Zone em estruturas organizadas para consultas analíticas e dashboards, utilizando tabelas fato, dimensões e views analíticas.

Durante o desenvolvimento, foi possível compreender:

Como estruturar uma camada Refined em um Data Lake

Como aplicar conceitos de modelagem dimensional

Como criar tabelas fato e dimensões

Como utilizar AWS Glue com PySpark para transformação de dados

Como organizar dados analíticos em formato Parquet

Como utilizar AWS Athena para consultas SQL

Como construir views analíticas para responder perguntas de negócio

Como integrar diferentes camadas do Data Lake em um fluxo analítico

Além da parte técnica, o projeto também envolveu organização de dados voltados para consumo em dashboards e análises futuras no Amazon QuickSight.

📌 Objetivo do Projeto
O projeto consiste em transformar os dados da Trusted Zone em uma camada analítica estruturada, realizando:

Consolidação de dados locais e da API TMDB

Criação de tabela fato para filmes

Criação de dimensões analíticas

Estruturação de dados em formato Parquet

Organização da camada Refined no Amazon S3

Criação de views analíticas no Athena

Preparação dos dados para dashboards e análises

A atividade simula um cenário real de construção de um Data Warehouse analítico em nuvem.

❓ Questões de Negócio
Durante o projeto, foram definidas as seguintes perguntas analíticas:

Quais são os filmes mais populares de Drama/Romance em 2024?

Quais são os filmes com mais avaliações em 2024?

Quais são os filmes mais bem avaliados em 2024?

Quais são os filmes mais mal avaliados em 2024?

🧱 Arquitetura Analítica
O projeto foi estruturado utilizando uma arquitetura analítica baseada em modelo dimensional:

Trusted → Refined → Athena → QuickSight
🔹 Estruturas Criadas
Tabela Fato: fato_filmes

Dimensões: Tempo, Gênero, Avaliação, Popularidade e Origem

Views Analíticas: consultas SQL para responder perguntas de negócio

⚙️ Tecnologias Utilizadas
🐍 Python

⚡ PySpark

☁️ AWS S3

🔄 AWS Glue

🗄️ AWS Athena

📊 Amazon QuickSight

🧱 Modelagem Dimensional

📁 Apache Parquet

📁 Estrutura do Projeto
Sprint 7/
│
├── Projeto/
│   ├── Modelo Dimensional.png
│   ├── scriptRefined.py
│
├── Evidencias/
│
└── README.md
🔄 Etapas do Projeto
1. Etapa I — Criação do Modelo Dimensional
Na primeira etapa foi desenvolvido o modelo dimensional responsável por estruturar como os dados seriam organizados na camada Refined.

O modelo define os relacionamentos entre tabela fato e dimensões, permitindo consultas analíticas eficientes.

O que foi desenvolvido
Estruturação da tabela fato

Criação das dimensões analíticas

Organização dos relacionamentos

Planejamento da arquitetura analítica

Modelagem dimensional para análises futuras

📸 Evidências
Modelo Dimensional
amostra1

2. Etapa II — Desenvolvimento da Camada Refined
Na segunda etapa foi desenvolvido o script responsável pela criação da camada Refined utilizando AWS Glue e PySpark.

O processo realizou a leitura dos dados da Trusted Zone, transformação, consolidação e geração das tabelas fato e dimensões.

O que foi desenvolvido
Leitura dos dados da Trusted Zone

Consolidação de dados locais e TMDB

Padronização de colunas

Filtragem de filmes Drama/Romance

Remoção de duplicidades

Criação da tabela fato

Criação das dimensões analíticas

Escrita em formato Parquet no Amazon S3

Estruturas Geradas
📌 Tabela Fato
fato_filmes

📌 Dimensões
Dim_Tempo

Dim_Genero

Dim_Avaliacao

Dim_Popularidade

Dim_Origem

📸 Evidências
Script Glue
amostra1
amostra1

Camada Refined
amostra1
amostra1
amostra1
amostra1
amostra1

Outputs
amostra1
amostra1
amostra1
amostra1
amostra1
amostra1

3. Etapa III — Criação do Crawler e Database
Na terceira etapa foi realizado o processo de catalogação dos dados da camada Refined utilizando AWS Glue Crawler.

O crawler realizou a leitura automática dos arquivos armazenados no S3 e criou as tabelas dentro do catálogo de dados utilizado pelo Athena.

O que foi desenvolvido
Criação da Database no AWS Glue

Configuração do Glue Crawler

Catalogação automática dos dados

Integração com AWS Athena

Criação das tabelas analíticas

📸 Evidências
Criação da Database e do Crawler
amostra1
amostra1

Execução do Crawler
amostra1
amostra1

Selects das Tabelas
amostra1
amostra1
amostra1
amostra1
amostra1
amostra1

4. Etapa IV — Criação das Views Analíticas
Na última etapa foram desenvolvidas views no AWS Athena responsáveis por responder às perguntas de negócio propostas no projeto.

As consultas foram construídas utilizando SQL sobre a tabela fato criada na camada Refined.

O que foi desenvolvido
Views para filmes mais populares

Views para filmes mais avaliados

Views para filmes mais bem avaliados

Views para filmes mais mal avaliados

Consultas analíticas no Athena

Views Criadas
vw_top10_populares_2024

vw_top10_mais_avaliados_2024

vw_top10_bem_avaliados_2024

vw_top10_mal_avaliados_2024

📸 Evidências
Views no Athena
amostra1
amostra1
amostra1
amostra1

📊 Resultados
Construção completa da camada Refined

Criação de modelo dimensional analítico

Consolidação de dados locais e TMDB

Estruturação de tabela fato e dimensões

Organização dos dados em Parquet

Integração com Athena e QuickSight

Criação de views analíticas para consultas SQL

Pipeline preparada para dashboards e análises futuras

🧠 Aprendizados
Durante o desenvolvimento do projeto, foi possível aprofundar conhecimentos em:

Engenharia de Dados

Modelagem Dimensional

Data Warehousing

AWS Glue

AWS Athena

PySpark

Apache Parquet

Construção de pipelines analíticas

Criação de views SQL

Estruturação de Data Lakes analíticos

🔮 Melhorias Futuras
Integração completa com Amazon QuickSight

Criação de dashboards interativos

Implementação de métricas avançadas

Automatização de pipelines com Step Functions

Monitoramento com CloudWatch

Criação de partições automáticas no Athena

Expansão das análises para outros gêneros cinematográficos


made em formato de codigo

# 🚀 Projeto

Este projeto teve como objetivo aplicar, na prática, conceitos de **Modelagem Dimensional**, **Data Warehousing**, **AWS Athena**, **AWS Glue** e **engenharia de dados analítica**, construindo a camada **Refined** de um Data Lake na AWS.

A proposta consistiu em transformar os dados da Trusted Zone em estruturas organizadas para consultas analíticas e dashboards, utilizando tabelas fato, dimensões e views analíticas.

Durante o desenvolvimento, foi possível compreender:

- Como estruturar uma camada Refined em um Data Lake  
- Como aplicar conceitos de modelagem dimensional  
- Como criar tabelas fato e dimensões  
- Como utilizar AWS Glue com PySpark para transformação de dados  
- Como organizar dados analíticos em formato Parquet  
- Como utilizar AWS Athena para consultas SQL  
- Como construir views analíticas para responder perguntas de negócio  
- Como integrar diferentes camadas do Data Lake em um fluxo analítico  

Além da parte técnica, o projeto também envolveu organização de dados voltados para consumo em dashboards e análises futuras no Amazon QuickSight.

---

# 📌 Objetivo do Projeto

O projeto consiste em transformar os dados da Trusted Zone em uma camada analítica estruturada, realizando:

- Consolidação de dados locais e da API TMDB  
- Criação de tabela fato para filmes  
- Criação de dimensões analíticas  
- Estruturação de dados em formato Parquet  
- Organização da camada Refined no Amazon S3  
- Criação de views analíticas no Athena  
- Preparação dos dados para dashboards e análises  

A atividade simula um cenário real de construção de um Data Warehouse analítico em nuvem.

---

# ❓ Questões de Negócio

Durante o projeto, foram definidas as seguintes perguntas analíticas:

- Quais são os filmes mais populares de Drama/Romance em 2024?
- Quais são os filmes com mais avaliações em 2024?
- Quais são os filmes mais bem avaliados em 2024?
- Quais são os filmes mais mal avaliados em 2024?

---

# 🧱 Arquitetura Analítica

O projeto foi estruturado utilizando uma arquitetura analítica baseada em modelo dimensional:
Trusted → Refined → Athena → QuickSight


## 🔹 Estruturas Criadas

- **Tabela Fato:** fato_filmes  
- **Dimensões:** Tempo, Gênero, Avaliação, Popularidade e Origem  
- **Views Analíticas:** consultas SQL para responder perguntas de negócio  

---

# ⚙️ Tecnologias Utilizadas

- 🐍 Python  
- ⚡ PySpark  
- ☁️ AWS S3  
- 🔄 AWS Glue  
- 🗄️ AWS Athena  
- 📊 Amazon QuickSight  
- 🧱 Modelagem Dimensional  
- 📁 Apache Parquet  

---

# 📁 Estrutura do Projeto
Sprint 7/
│
├── Projeto/
│ ├── Modelo Dimensional.png
│ ├── scriptRefined.py
│
├── Evidencias/
│
└── README.md


---

# 🔄 Etapas do Projeto

## 1. [Etapa I](/Sprint%207/Projeto/Modelo%20Dimencional.png) — Criação do Modelo Dimensional

Na primeira etapa foi desenvolvido o modelo dimensional responsável por estruturar como os dados seriam organizados na camada Refined.

O modelo define os relacionamentos entre tabela fato e dimensões, permitindo consultas analíticas eficientes.

### O que foi desenvolvido

- Estruturação da tabela fato  
- Criação das dimensões analíticas  
- Organização dos relacionamentos  
- Planejamento da arquitetura analítica  
- Modelagem dimensional para análises futuras  

### 📸 Evidências

#### Modelo Dimensional
![amostra1](/Sprint%207/Evidencias/01.png)

---

## 2. [Etapa II](/Sprint%207/Projeto/scriptRefined.py) — Desenvolvimento da Camada Refined

Na segunda etapa foi desenvolvido o script responsável pela criação da camada Refined utilizando AWS Glue e PySpark.

O processo realizou a leitura dos dados da Trusted Zone, transformação, consolidação e geração das tabelas fato e dimensões.

### O que foi desenvolvido

- Leitura dos dados da Trusted Zone  
- Consolidação de dados locais e TMDB  
- Padronização de colunas  
- Filtragem de filmes Drama/Romance  
- Remoção de duplicidades  
- Criação da tabela fato  
- Criação das dimensões analíticas  
- Escrita em formato Parquet no Amazon S3  

### Estruturas Geradas

#### 📌 Tabela Fato
- fato_filmes

#### 📌 Dimensões
- Dim_Tempo  
- Dim_Genero  
- Dim_Avaliacao  
- Dim_Popularidade  
- Dim_Origem  

### 📸 Evidências

#### Script Glue
![amostra1](/Sprint%207/Evidencias/04.png)
![amostra1](/Sprint%207/Evidencias/05.png)

#### Camada Refined
![amostra1](/Sprint%207/Evidencias/12.png)
![amostra1](/Sprint%207/Evidencias/13.png)
![amostra1](/Sprint%207/Evidencias/14.png)
![amostra1](/Sprint%207/Evidencias/15.png)
![amostra1](/Sprint%207/Evidencias/16.png)

#### Outputs
![amostra1](/Sprint%207/Evidencias/06.png)
![amostra1](/Sprint%207/Evidencias/07.png)
![amostra1](/Sprint%207/Evidencias/08.png)
![amostra1](/Sprint%207/Evidencias/09.png)
![amostra1](/Sprint%207/Evidencias/10.png)
![amostra1](/Sprint%207/Evidencias/11.png)

---

## 3. [Etapa III](/Sprint%207/Projeto/scriptRefined.py) — Criação do Crawler e Database

Na terceira etapa foi realizado o processo de catalogação dos dados da camada Refined utilizando AWS Glue Crawler.

O crawler realizou a leitura automática dos arquivos armazenados no S3 e criou as tabelas dentro do catálogo de dados utilizado pelo Athena.

### O que foi desenvolvido

- Criação da Database no AWS Glue  
- Configuração do Glue Crawler  
- Catalogação automática dos dados  
- Integração com AWS Athena  
- Criação das tabelas analíticas  

### 📸 Evidências

#### Criação da Database e do Crawler
![amostra1](/Sprint%207/Evidencias/02.png)
![amostra1](/Sprint%207/Evidencias/03.png)

#### Execução do Crawler
![amostra1](/Sprint%207/Evidencias/17.png)
![amostra1](/Sprint%207/Evidencias/18.png)

#### Selects das Tabelas
![amostra1](/Sprint%207/Evidencias/19.png)
![amostra1](/Sprint%207/Evidencias/20.png)
![amostra1](/Sprint%207/Evidencias/21.png)
![amostra1](/Sprint%207/Evidencias/22.png)
![amostra1](/Sprint%207/Evidencias/23.png)
![amostra1](/Sprint%207/Evidencias/24.png)

---

## 4. [Etapa IV](/Sprint%207/Projeto/scriptRefined.py) — Criação das Views Analíticas

Na última etapa foram desenvolvidas views no AWS Athena responsáveis por responder às perguntas de negócio propostas no projeto.

As consultas foram construídas utilizando SQL sobre a tabela fato criada na camada Refined.

### O que foi desenvolvido

- Views para filmes mais populares  
- Views para filmes mais avaliados  
- Views para filmes mais bem avaliados  
- Views para filmes mais mal avaliados  
- Consultas analíticas no Athena  

### Views Criadas

- vw_top10_populares_2024  
- vw_top10_mais_avaliados_2024  
- vw_top10_bem_avaliados_2024  
- vw_top10_mal_avaliados_2024  

### 📸 Evidências

#### Views no Athena
![amostra1](/Sprint%207/Evidencias/25.png)
![amostra1](/Sprint%207/Evidencias/26.png)
![amostra1](/Sprint%207/Evidencias/27.png)
![amostra1](/Sprint%207/Evidencias/28.png)

---

# 📊 Resultados

- Construção completa da camada Refined  
- Criação de modelo dimensional analítico  
- Consolidação de dados locais e TMDB  
- Estruturação de tabela fato e dimensões  
- Organização dos dados em Parquet  
- Integração com Athena e QuickSight  
- Criação de views analíticas para consultas SQL  
- Pipeline preparada para dashboards e análises futuras  

---

# 🧠 Aprendizados

Durante o desenvolvimento do projeto, foi possível aprofundar conhecimentos em:

- Engenharia de Dados  
- Modelagem Dimensional  
- Data Warehousing  
- AWS Glue  
- AWS Athena  
- PySpark  
- Apache Parquet  
- Construção de pipelines analíticas  
- Criação de views SQL  
- Estruturação de Data Lakes analíticos  

---

# 🔮 Melhorias Futuras

- Integração completa com Amazon QuickSight  
- Criação de dashboards interativos  
- Implementação de métricas avançadas  
- Automatização de pipelines com Step Functions  
- Monitoramento com CloudWatch  
- Criação de partições automáticas no Athena  
- Expansão das análises para outros gêneros cinematográficos  

# Resumo da Sprint 8 

**Consumo dos Dados – AWS QuickSight**:  
Nesta sprint final, avançamos para a etapa de consumo e visualização dos dados, transformando as informações da **Camada Refined** em insights acionáveis através do **AWS QuickSight**.  

O objetivo foi construir um **dashboard interativo** que consolidasse os principais indicadores, permitindo uma análise clara e de alto nível sobre os dados tratados nas etapas anteriores.  

As fontes utilizadas foram exclusivamente as **tabelas e views da Refined Zone** acessadas via **Athena**, garantindo integridade, consistência e desempenho na consulta.  

### Principais recursos utilizados:  
- Conexão do QuickSight ao **Athena** como datasource.  
- Criação de análises exploratórias com diferentes tipos de gráficos (**barras, linhas, KPI e heatmaps**).  
- Dashboards interativos com filtros dinâmicos (**por ano, gênero e popularidade**).  
- KPIs estratégicos exibindo métricas como:  
  - Total de filmes de **Drama/Romance**.  
  - Média de **avaliações**.  
  - Popularidade acumulada por **década**.  
  - **Top 10 filmes** mais votados e mais bem avaliados.  
- **Storytelling visual**, evidenciando a evolução histórica da produção cinematográfica, correlação entre popularidade e avaliação, além da análise segmentada por gêneros.  


## Desafio  

**Desafio – Entrega 5 (Consumo dos Dados):**  
Nesta etapa, foi criado um **dashboard final no AWS QuickSight**, consolidando as análises feitas ao longo do desafio.  

### Principais entregas:  
- Dashboard no QuickSight conectado ao **Athena (Refined Zone)**.  
- Diferentes visualizações representando **indicadores de negócio**.  
- Inclusão de **filtros e controles interativos** para explorar os dados.  
- Criação de **KPIs** para destacar métricas críticas de desempenho.  
- Estruturação de um **storytelling coerente** para responder às principais perguntas de negócio.  


# Etapas

### 1. [Etapa I](/Sprint%208/Desafio/Views.sql)

Na Primeira etapa, houve o desenvolvimento de visualizações, a fim de ajudar na criação dos gráficos

`sql
-- Conta a quantidade de filmes lançados em cada década
CREATE OR REPLACE VIEW "vw_qtd_filmes_drama_romance_por_decada" AS 
SELECT
  (FLOOR((anoLancamento / 10)) * 10) decada,
  COUNT(*) qtd_filmes
FROM db_desafiorefined.fato_filmes
WHERE (anoLancamento IS NOT NULL)
GROUP BY (FLOOR((anoLancamento / 10)) * 10)
ORDER BY decada ASC;


-- Conta quantos filmes por década tiveram nota > 8 e mais de 1000 votos
CREATE OR REPLACE VIEW "vw_qtd_filmes_nota10_por_decada" AS 
SELECT
  (FLOOR((f.anoLancamento / 10)) * 10) decada,
  COUNT(*) qtd_filmes
FROM db_desafiorefined.fato_filmes f
WHERE ((f.anoLancamento IS NOT NULL) AND (f.notaMedia > 8) AND (f.numeroVotos > 1000))
GROUP BY (FLOOR((f.anoLancamento / 10)) * 10)
ORDER BY decada ASC;


-- Conta a quantidade de filmes com mais de 100 votos por década
CREATE OR REPLACE VIEW "vw_filmes_com_mais_100_avaliacoes_por_decada" AS 
SELECT
  (FLOOR((anoLancamento / 10)) * 10) decada,
  COUNT(*) qtd_filmes
FROM db_desafiorefined.fato_filmes
WHERE ((numeroVotos > 100) AND (anoLancamento IS NOT NULL))
GROUP BY (FLOOR((anoLancamento / 10)) * 10)
HAVING (COUNT(*) > 100)
ORDER BY qtd_filmes DESC;


-- Calcula a média do número de votos por década
CREATE OR REPLACE VIEW "vw_media_decada_numero_avaliacoes" AS 
SELECT
  (FLOOR((anoLancamento / 10)) * 10) decada,
  CAST(AVG(numeroVotos) AS BIGINT) media_numero_avaliacoes
FROM db_desafiorefined.fato_filmes
WHERE (anoLancamento IS NOT NULL)
GROUP BY (FLOOR((anoLancamento / 10)) * 10)
ORDER BY decada ASC;


-- Calcula a nota média dos filmes por década
CREATE OR REPLACE VIEW "vw_media_decada_nota_avaliacoes" AS 
SELECT
  (FLOOR((anoLancamento / 10)) * 10) decada,
  ROUND(AVG(notaMedia), 1) media_nota_avaliacoes
FROM fato_filmes
WHERE (anoLancamento IS NOT NULL)
GROUP BY (FLOOR((anoLancamento / 10)) * 10)
ORDER BY decada ASC;


-- Seleciona o melhor filme (nota mais alta) em cada década, desempate pelo número de votos
CREATE OR REPLACE VIEW "vw_melhor_filme_por_decada" AS 
SELECT
  decada,
  tituloPrincipal,
  notaMedia,
  numeroVotos
FROM (
   SELECT
     ((anoLancamento / 10) * 10) decada,
     tituloPrincipal,
     notaMedia,
     numeroVotos,
     ROW_NUMBER() OVER (PARTITION BY ((anoLancamento / 10) * 10) ORDER BY notaMedia DESC, numeroVotos DESC) rk
   FROM db_desafiorefined.fato_filmes
   WHERE ((anoLancamento IS NOT NULL) AND (numeroVotos > 1000))
) sub
WHERE (rk = 1)
ORDER BY decada ASC;


-- Seleciona os 5 anos com mais filmes que tiveram pelo menos 100 avaliações
CREATE OR REPLACE VIEW "vw_top5_anos_mais_filmes_100_avaliacoes" AS 
SELECT *
FROM db_desafiorefined.vw_filmes_com_mais_100_avaliacoes
LIMIT 5;


-- Dentro dos top 5 anos mais produtivos, pega o melhor filme (nota mais alta, desempate por votos)
CREATE OR REPLACE VIEW "vw_top1_melhor_filme_top5_anos" AS 
SELECT
  anoLancamento,
  tituloPrincipal,
  notaMedia,
  numeroVotos
FROM (
   SELECT
     f.anoLancamento,
     f.tituloPrincipal,
     f.notaMedia,
     f.numeroVotos,
     ROW_NUMBER() OVER (PARTITION BY f.anoLancamento ORDER BY f.notaMedia DESC, f.numeroVotos DESC) rk
   FROM db_desafiorefined.fato_filmes f
   INNER JOIN db_desafiorefined.vw_top5_anos_mais_filmes_100_avaliacoes t 
     ON (f.anoLancamento = t.anoLancamento)
   WHERE (f.numeroVotos > 1000)
) sub
WHERE (rk = 1)
ORDER BY anoLancamento ASC, notaMedia DESC;


-- Lista os 10 filmes mais populares de 2023 e 2024
CREATE OR REPLACE VIEW "vw_top10_populares_2023_2024" AS 
SELECT
  tituloPrincipal,
  anoLancamento,
  popularidade,
  numeroVotos,
  notaMedia
FROM fato_filmes
WHERE (anoLancamento IN (2023, 2024))
ORDER BY popularidade DESC
LIMIT 10;


-- Lista os 10 filmes mais bem avaliados de 2023 e 2024 (mínimo 1000 votos)
CREATE OR REPLACE VIEW "vw_top10_bem_avaliados_2023_2024" AS 
SELECT
  tituloPrincipal,
  anoLancamento,
  notaMedia,
  numeroVotos
FROM fato_filmes
WHERE ((anoLancamento IN (2023, 2024)) AND (numeroVotos > 1000))
ORDER BY notaMedia DESC, numeroVotos DESC
LIMIT 10;


-- Lista os 10 filmes mais mal avaliados de 2023 e 2024 (mínimo 100 votos)
CREATE OR REPLACE VIEW "vw_top10_mal_avaliados_2023_2024" AS 
SELECT
  tituloPrincipal,
  anoLancamento,
  notaMedia,
  numeroVotos
FROM fato_filmes
WHERE ((anoLancamento IN (2023, 2024)) AND (numeroVotos > 100))
ORDER BY notaMedia ASC, numeroVotos DESC
LIMIT 10;


### Evidencias

* Views sendo criadas no Athena

![amostra1](/Sprint%208/Evidencias/06.png)  
![amostra2](/Sprint%208/Evidencias/07.png)  

* Views criadas, no AWS glue database 

![amostra3](/Sprint%208/Evidencias/01.png) 
![amostra4](/Sprint%208/Evidencias/02.png)  


---

### 2. [Etapa II](/Sprint%208/Desafio/Finalizado.pdf)

Na segunda etapa foi realizado a criação do Dashboard no QuickSight, com gráficos, indicadores KPI, textos e imagens

![Dashboard](/Sprint%208/Evidencias/Finalizado_page-0001.jpg)


### Evidencias do codigo

* Conjunto de dados

![amostra1](/Sprint%208/Evidencias/03.png)  
![amostra2](/Sprint%208/Evidencias/04.png)  

* Dashboard

![amostra3](/Sprint%208/Evidencias/05.png)  



esse é o ultimo, por favor, no mesmo modelo dos anteriores

# 🚀 Projeto

Este projeto teve como objetivo realizar a etapa final do pipeline de dados desenvolvido ao longo das sprints anteriores, focando no consumo e visualização das informações através do AWS QuickSight.

Nesta sprint, os dados estruturados na camada Refined foram utilizados para construção de dashboards analíticos interativos, permitindo transformar dados processados em insights estratégicos e visuais.

O processo envolveu integração entre Athena, AWS Glue e QuickSight, possibilitando consultas otimizadas sobre arquivos Parquet armazenados no Amazon S3.

Durante o desenvolvimento, foi possível compreender:

- Como consumir dados analíticos utilizando AWS QuickSight  
- Como conectar o QuickSight ao Athena  
- Como utilizar views SQL para facilitar análises analíticas  
- Como estruturar dashboards interativos e KPIs  
- Como criar visualizações estratégicas utilizando gráficos e filtros  
- Como transformar dados refinados em storytelling visual  
- Como integrar Athena, Glue e QuickSight em um fluxo analítico completo  

Além da parte técnica, o projeto também envolveu construção de indicadores de negócio voltados para análise de filmes do gênero Drama/Romance.

---

# 📌 Objetivo do Projeto

O projeto consiste em consumir os dados da camada Refined e transformá-los em dashboards analíticos no AWS QuickSight, realizando:

- Criação de views analíticas no Athena  
- Construção de datasets para visualização  
- Desenvolvimento de dashboards interativos  
- Criação de KPIs estratégicos  
- Implementação de filtros dinâmicos  
- Estruturação de storytelling visual para análise dos dados  

A atividade simula um cenário real de Business Intelligence e Analytics em Cloud Computing.

---

# ❓ Questões de Negócio

Durante o projeto, foram definidas as seguintes perguntas analíticas:

- Quais décadas possuem maior quantidade de filmes Drama/Romance?
- Quais décadas apresentam os filmes mais bem avaliados?
- Quais anos tiveram maior quantidade de filmes com avaliações relevantes?
- Quais são os filmes mais populares de 2023 e 2024?
- Quais são os filmes mais bem avaliados de 2023 e 2024?
- Quais são os filmes mais mal avaliados de 2023 e 2024?

---

# 🧱 Arquitetura Analítica

O consumo dos dados foi realizado utilizando:
Refined Zone → Athena → QuickSight


## 🔹 Componentes

- **Refined Zone:** dados refinados e modelados em formato Parquet  
- **Athena:** mecanismo de consultas SQL sobre os dados do S3  
- **QuickSight:** ferramenta de visualização e construção de dashboards  

---

# ⚙️ Tecnologias Utilizadas

- ☁️ AWS Athena  
- 📊 AWS QuickSight  
- 🗂️ AWS Glue Data Catalog  
- 🪣 Amazon S3  
- ⚡ SQL  
- 📁 Apache Parquet  

---

# 📁 Estrutura do Projeto
Sprint 8/
│
├── Projeto/
│ ├── Views.sql
│ └── Finalizado.pdf
│
├── Evidencias/
│
└── README.md
````
---

# Etapas

### 1. [Etapa I](/Sprint%208/Projeto/Views.sql) — Criação das Views Analíticas no Athena

Na primeira etapa foram desenvolvidas diversas views SQL no Athena com o objetivo de facilitar a criação dos gráficos e indicadores utilizados no dashboard do QuickSight.

As views permitiram organizar consultas analíticas sobre filmes Drama/Romance, utilizando métricas como quantidade de filmes, popularidade, avaliações e distribuição por década.

### O que foi desenvolvido

- Criação de views analíticas no Athena  
- Consultas SQL para KPIs e gráficos  
- Views voltadas para análises históricas por década  
- Identificação dos filmes mais populares e mais bem avaliados  
- Estruturação de consultas otimizadas para QuickSight  

````sql
-- Conta a quantidade de filmes lançados em cada década
CREATE OR REPLACE VIEW "vw_qtd_filmes_drama_romance_por_decada" AS 
SELECT
  (FLOOR((anoLancamento / 10)) * 10) decada,
  COUNT(*) qtd_filmes
FROM db_Projetorefined.fato_filmes
WHERE (anoLancamento IS NOT NULL)
GROUP BY (FLOOR((anoLancamento / 10)) * 10)
ORDER BY decada ASC;


-- Conta quantos filmes por década tiveram nota > 8 e mais de 1000 votos
CREATE OR REPLACE VIEW "vw_qtd_filmes_nota10_por_decada" AS 
SELECT
  (FLOOR((f.anoLancamento / 10)) * 10) decada,
  COUNT(*) qtd_filmes
FROM db_Projetorefined.fato_filmes f
WHERE ((f.anoLancamento IS NOT NULL) AND (f.notaMedia > 8) AND (f.numeroVotos > 1000))
GROUP BY (FLOOR((f.anoLancamento / 10)) * 10)
ORDER BY decada ASC;


-- Conta a quantidade de filmes com mais de 100 votos por década
CREATE OR REPLACE VIEW "vw_filmes_com_mais_100_avaliacoes_por_decada" AS 
SELECT
  (FLOOR((anoLancamento / 10)) * 10) decada,
  COUNT(*) qtd_filmes
FROM db_Projetorefined.fato_filmes
WHERE ((numeroVotos > 100) AND (anoLancamento IS NOT NULL))
GROUP BY (FLOOR((anoLancamento / 10)) * 10)
HAVING (COUNT(*) > 100)
ORDER BY qtd_filmes DESC;


-- Calcula a média do número de votos por década
CREATE OR REPLACE VIEW "vw_media_decada_numero_avaliacoes" AS 
SELECT
  (FLOOR((anoLancamento / 10)) * 10) decada,
  CAST(AVG(numeroVotos) AS BIGINT) media_numero_avaliacoes
FROM db_Projetorefined.fato_filmes
WHERE (anoLancamento IS NOT NULL)
GROUP BY (FLOOR((anoLancamento / 10)) * 10)
ORDER BY decada ASC;


-- Calcula a nota média dos filmes por década
CREATE OR REPLACE VIEW "vw_media_decada_nota_avaliacoes" AS 
SELECT
  (FLOOR((anoLancamento / 10)) * 10) decada,
  ROUND(AVG(notaMedia), 1) media_nota_avaliacoes
FROM fato_filmes
WHERE (anoLancamento IS NOT NULL)
GROUP BY (FLOOR((anoLancamento / 10)) * 10)
ORDER BY decada ASC;


-- Seleciona o melhor filme (nota mais alta) em cada década, desempate pelo número de votos
CREATE OR REPLACE VIEW "vw_melhor_filme_por_decada" AS 
SELECT
  decada,
  tituloPrincipal,
  notaMedia,
  numeroVotos
FROM (
   SELECT
     ((anoLancamento / 10) * 10) decada,
     tituloPrincipal,
     notaMedia,
     numeroVotos,
     ROW_NUMBER() OVER (PARTITION BY ((anoLancamento / 10) * 10) ORDER BY notaMedia DESC, numeroVotos DESC) rk
   FROM db_Projetorefined.fato_filmes
   WHERE ((anoLancamento IS NOT NULL) AND (numeroVotos > 1000))
) sub
WHERE (rk = 1)
ORDER BY decada ASC;


-- Seleciona os 5 anos com mais filmes que tiveram pelo menos 100 avaliações
CREATE OR REPLACE VIEW "vw_top5_anos_mais_filmes_100_avaliacoes" AS 
SELECT *
FROM db_Projetorefined.vw_filmes_com_mais_100_avaliacoes
LIMIT 5;


-- Dentro dos top 5 anos mais produtivos, pega o melhor filme (nota mais alta, desempate por votos)
CREATE OR REPLACE VIEW "vw_top1_melhor_filme_top5_anos" AS 
SELECT
  anoLancamento,
  tituloPrincipal,
  notaMedia,
  numeroVotos
FROM (
   SELECT
     f.anoLancamento,
     f.tituloPrincipal,
     f.notaMedia,
     f.numeroVotos,
     ROW_NUMBER() OVER (PARTITION BY f.anoLancamento ORDER BY f.notaMedia DESC, f.numeroVotos DESC) rk
   FROM db_Projetorefined.fato_filmes f
   INNER JOIN db_Projetorefined.vw_top5_anos_mais_filmes_100_avaliacoes t 
     ON (f.anoLancamento = t.anoLancamento)
   WHERE (f.numeroVotos > 1000)
) sub
WHERE (rk = 1)
ORDER BY anoLancamento ASC, notaMedia DESC;


-- Lista os 10 filmes mais populares de 2023 e 2024
CREATE OR REPLACE VIEW "vw_top10_populares_2023_2024" AS 
SELECT
  tituloPrincipal,
  anoLancamento,
  popularidade,
  numeroVotos,
  notaMedia
FROM fato_filmes
WHERE (anoLancamento IN (2023, 2024))
ORDER BY popularidade DESC
LIMIT 10;


-- Lista os 10 filmes mais bem avaliados de 2023 e 2024 (mínimo 1000 votos)
CREATE OR REPLACE VIEW "vw_top10_bem_avaliados_2023_2024" AS 
SELECT
  tituloPrincipal,
  anoLancamento,
  notaMedia,
  numeroVotos
FROM fato_filmes
WHERE ((anoLancamento IN (2023, 2024)) AND (numeroVotos > 1000))
ORDER BY notaMedia DESC, numeroVotos DESC
LIMIT 10;


-- Lista os 10 filmes mais mal avaliados de 2023 e 2024 (mínimo 100 votos)
CREATE OR REPLACE VIEW "vw_top10_mal_avaliados_2023_2024" AS 
SELECT
  tituloPrincipal,
  anoLancamento,
  notaMedia,
  numeroVotos
FROM fato_filmes
WHERE ((anoLancamento IN (2023, 2024)) AND (numeroVotos > 100))
ORDER BY notaMedia ASC, numeroVotos DESC
LIMIT 10;
````

### 📸 Evidências

#### Views sendo criadas no Athena


![amostra1](/Sprint%208/Evidencias/06.png)  
![amostra2](/Sprint%208/Evidencias/07.png)  

#### Views criadas no AWS Glue Database

![amostra3](/Sprint%208/Evidencias/01.png) 
![amostra4](/Sprint%208/Evidencias/02.png)  


---

### 2. [Etapa II](/Sprint%208/Projeto/Finalizado.pdf)) — Construção do Dashboard no QuickSight

Na segunda etapa foi realizado o desenvolvimento do dashboard final no AWS QuickSight.

O dashboard foi estruturado utilizando gráficos, KPIs, filtros dinâmicos, textos explicativos e storytelling visual para facilitar a interpretação dos dados.

As análises foram conectadas diretamente ao Athena utilizando as views criadas anteriormente.

### O que foi desenvolvido

- Integração do QuickSight com Athena  
- Criação de datasets analíticos  
- Desenvolvimento de dashboards interativos  
- Criação de KPIs estratégicos  
- Construção de gráficos analíticos  
- Implementação de filtros dinâmicos  
- Storytelling visual com insights de negócio

### Dashboard Final

![Dashboard](/Sprint%208/Evidencias/Finalizado_page-0001.jpg)

### 📸 Evidências

#### Conjunto de Dados

![amostra1](/Sprint%208/Evidencias/03.png)  
![amostra2](/Sprint%208/Evidencias/04.png)  

#### Dashboard no QuickSight

![amostra3](/Sprint%208/Evidencias/05.png)  

---

# 📊 Resultados

- Criação de um dashboard analítico completo no QuickSight  
- Integração entre Athena, Glue e QuickSight  
- Construção de KPIs estratégicos para análise de filmes  
- Visualizações interativas e dinâmicas  
- Organização das análises por década, avaliações e popularidade  
- Storytelling visual voltado para tomada de decisão  
- Estrutura analítica pronta para expansão futura  

---

# 🧠 Aprendizados

Durante o desenvolvimento do projeto, foi possível aprofundar conhecimentos em:

- Business Intelligence  
- AWS QuickSight  
- AWS Athena  
- Criação de dashboards analíticos  
- Modelagem analítica para visualização  
- Storytelling com dados  
- Construção de KPIs  
- Consultas SQL analíticas  
- Integração entre serviços AWS  