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

## 🔹 Estruturas Criadas

- **Tabela Fato:** fato_filmes  
- **Dimensões:** Tempo, Gênero, Avaliação, Popularidade e Origem  
- **Views Analíticas:** consultas SQL para responder perguntas de negócio  

---

# 📁 Estrutura do Projeto
````
Sprint 7/
│
├── Projeto/
│ ├── Modelo Dimensional.png
│ ├── scriptRefined.py
│
├── Evidencias/
│
└── README.md
````
---

# Etapas

### 1. [Etapa I](/Sprint%207/Projeto/Modelo%20Dimencional.png) — Criação do Modelo Dimensional

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

### 2. [Etapa II](/Sprint%207/Projeto/scriptRefined.py) — Desenvolvimento da Camada Refined

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


````python
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

````

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

### 3. [Etapa III](/Sprint%207/Projeto/scriptRefined.py) — Criação do Crawler e Database

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

### 4. [Etapa IV](/Sprint%207/Projeto/scriptRefined.py) — Criação das Views Analíticas

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

* Filmes mais populares de Drama/Romance em 2024
````sql
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

````

* Filmes com mais avaliações (mais votos) de Drama/Romance em 2024
````sql
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

````

* Filmes mais bem avaliados de Drama/Romance em 2024
````sql
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

````

* Filmes mais mal avaliados de Drama/Romance em 2024
````sql
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
````

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