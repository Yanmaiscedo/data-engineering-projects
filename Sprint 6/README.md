## Projeto

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

# 📁 Estrutura do Projeto
````
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
````

# Etapas

### 1. [Etapa I](/Sprint%206/Projeto/Etapa%201/CSV.py) — Processamento de arquivos CSV para Parquet

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

````python

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
input_filmes_path = "s3://bucket-name/Raw/Local/CSV/Movies/"
input_series_path = "s3://bucket-name/Raw/Local/CSV/Series/"

# Estes caminhos apontam para o bucket 'Trusted' do S3, onde os dados transformados serão armazenados no formato Parquet.
output_filmes_path = "s3://bucket-name/Trusted/CSV/Parquet/Movies/"
output_series_path = "s3://bucket-name/Trusted/CSV/Parquet/Series/"

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


````

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

### 2. [Etapa II](/Sprint%206/Projeto/Etapa2/JSON.py) — Processamento de arquivos JSON para Parquet

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

````python

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
input_file = "s3://bucket-name/Raw/TMDB/"
# Caminho de saída para os dados transformados, salvos no formato Parquet.
output_parquet = "s3://bucket-name/Trusted/JSON/Parquet/"

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

````
### 📸 Evidências

#### Script Glue
![amostra1](/Sprint%206/Evidencias/Projeto/06.png)
![amostra1](/Sprint%206/Evidencias/Projeto/07.png)
![amostra1](/Sprint%206/Evidencias/Projeto/09.png)
#### Camada Trusted
![amostra1](/Sprint%206/Evidencias/Projeto/14.png)

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