# 🚀 Projeto

Este projeto teve como objetivo aplicar, na prática, conceitos de **Engenharia de Dados em Cloud Computing**, utilizando serviços da AWS para construir um pipeline simples de ingestão, processamento, armazenamento e análise de dados.

Durante o desenvolvimento, foi possível integrar ferramentas como **Amazon S3**, **AWS CLI**, **Boto3**, **Pandas** e bibliotecas de visualização de dados, permitindo automatizar tarefas de ETL e manipulação de arquivos diretamente na nuvem.

A atividade utilizou um conjunto de dados sobre **consumo de energia por órgãos públicos**, possibilitando realizar processos de limpeza, transformação e análise exploratória dos dados, além da geração de relatórios e visualizações analíticas.

Ao longo do projeto, foram trabalhados conceitos como:

- Criação e gerenciamento de buckets no Amazon S3  
- Upload e leitura de arquivos diretamente da AWS  
- Integração entre Python e serviços AWS utilizando Boto3  
- Limpeza e transformação de dados com Pandas  
- Geração de análises automatizadas  
- Exportação de arquivos `.txt` e gráficos `.png`  
- Estruturação de um fluxo simples de ETL em ambiente cloud  

O projeto proporcionou uma visão prática de como pipelines de dados podem ser construídos utilizando serviços serverless e armazenamento em nuvem, aproximando o desenvolvimento de cenários reais da área de Engenharia de Dados.

---

# Etapas

### 1. [Etapa I](/Sprint%204/Projeto/etapa1/Projeto-etapa1.ipynb)

Na primeira etapa do projeto, foi realizada a criação e configuração do bucket no **Amazon S3**, que seria utilizado como camada de armazenamento dos arquivos processados.

Após isso, foi feito o processo de leitura e tratamento do arquivo `consumo-energia.csv`, utilizando Python e Pandas para limpeza e padronização dos dados.

Durante o processamento foram realizadas atividades como:

- Remoção de inconsistências  
- Conversão de tipos numéricos  
- Tratamento de datas  
- Padronização de colunas  
- Filtragem de valores nulos  
- Seleção das informações relevantes  

Ao final da etapa, o dataset tratado foi exportado como `consumo_energia_limpo.csv` e enviado automaticamente para o bucket S3 utilizando a biblioteca **Boto3**.

````python

import pandas as pd
import boto3
import io

# Configurações iniciais
arquivo_original = "consumo-energia.csv"
bucket = "bucket-name"
caminho_s3 = "consumo_energia_limpo.csv"
perfil_aws = "default"

# Leitura do arquivo e limpeza
df = pd.read_csv(arquivo_original)
linhas_antes = df.shape[0]

df.columns = df.columns.str.strip()

df['media_consumo_mes_2018_2019'] = pd.to_numeric(df['media_consumo_mes_2018_2019'], errors='coerce')
df['consumo_mes_referencia'] = pd.to_numeric(df['consumo_mes_referencia'], errors='coerce')

df['mes_ano'] = df['mes_ano'].astype(str).str.zfill(6)
df['mes'] = df['mes_ano'].str.slice(0, len(df['mes_ano'][0]) - 4).astype(int)
df['ano'] = df['mes_ano'].str[-4:].astype(int)

df['mes_ano_corrigido'] = pd.to_datetime(
    df['ano'].astype(str) + '-' + df['mes'].astype(str).str.zfill(2),
    format='%Y-%m',
    errors='coerce'
)

df_limpo = df.dropna(subset=['media_consumo_mes_2018_2019', 'consumo_mes_referencia', 'orgao'])

colunas_relevantes = [
    'mes_ano_corrigido',
    'mes_ano',
    'orgao',
    'sigla_orgao',
    'media_consumo_mes_2018_2019',
    'consumo_mes_referencia',
    'justificativa_meta',
    'observacao'
]
df_limpo = df_limpo[colunas_relevantes]
linhas_depois = df_limpo.shape[0]

# Envio para o Bucket
session = boto3.Session(profile_name=perfil_aws)
s3 = session.client("s3")

buffer = io.StringIO()
df_limpo.to_csv(buffer, index=False)
buffer.seek(0)

s3.put_object(Body=buffer.getvalue(), Bucket=bucket, Key=caminho_s3)

print("Número de linhas antes da limpeza:", linhas_antes)
print("Número de linhas após a limpeza:", linhas_depois)
print(f"\nArquivo limpo enviado com sucesso para s3://{bucket}/{caminho_s3}")

````

### 📸 Evidências

![amostra](/Sprint%204/Evidencias/Projeto/Execucao%20da%20limpeza.png)
![amostra](/Sprint%204/Evidencias/Projeto/Criacao%20do%20bucket.png)
![amostra](/Sprint%204/Evidencias/Projeto/csv-limpo%20no%20bucket.png)

---

### 2. [Etapa II](/Sprint%204/Projeto/etapa1/Projeto-etapa1.ipynb)

Na segunda etapa, foram desenvolvidas análises exploratórias utilizando os dados já tratados e armazenados no Amazon S3.

O processo envolveu a leitura direta do arquivo hospedado no bucket, sem necessidade de download manual, permitindo trabalhar os dados diretamente da nuvem.

As análises realizadas tiveram como objetivo identificar padrões e comportamentos relacionados ao consumo energético dos órgãos públicos.

Entre os resultados gerados, destacam-se:

- Órgãos que mais economizaram energia  
- Órgãos que mais aumentaram o consumo  
- Ranking dos maiores consumidores de energia  
- Justificativas dos órgãos que não atingiram metas de redução  

Os resultados foram exportados em arquivos `.txt` e gráficos `.png`, sendo posteriormente enviados novamente para o bucket S3.

````python

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import boto3
import io

# Configurações
arquivo_csv = "consumo_energia_limpo.csv"
bucket = "bucket-name"
pasta_s3 = "analises-etapa1/"
perfil_aws = "default"

# Sessão AWS
session = boto3.Session(profile_name=perfil_aws)
s3 = session.client('s3')

# Leitura do CSV direto do Bucker
obj = s3.get_object(Bucket=bucket, Key=f"{arquivo_csv}")
df = pd.read_csv(io.BytesIO(obj["Body"].read()), parse_dates=["mes_ano_corrigido"])

# Analise 1: Economia de Energia
df['variacao_percentual'] = ((df['consumo_mes_referencia'] - df['media_consumo_mes_2018_2019']) / df['media_consumo_mes_2018_2019']) * 100
economias = df.groupby('sigla_orgao')['variacao_percentual'].mean().sort_values()
top_5_economias = economias.head(5)

with open("analise1.txt", "w") as f:
    f.write("Top 5 órgãos que mais economizaram energia:\n")
    f.write(top_5_economias.to_string())

# Analise 2: Aumento de consumo de Energia
top_5_desperdicio = economias.tail(5)
with open("analise2.txt", "w") as f:
    f.write("Top 5 órgãos que mais aumentaram o consumo de energia:\n")
    f.write(top_5_desperdicio.to_string())

# Analise 3: Maiores Consumidores de Energia
orgao_consumo = df.groupby("sigla_orgao")["consumo_mes_referencia"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 6))
sns.barplot(
    x=orgao_consumo.values,
    y=orgao_consumo.index,
    hue=orgao_consumo.index,
    palette='viridis',
    legend=False
)
plt.title("Top 10 órgãos com maior consumo total")
plt.xlabel("Consumo Total (kWh)")
plt.tight_layout()
plt.savefig("analise3.png")
plt.close()

# Analise 4: Justificativas dos que não atingiram a meta
df["atingiu_meta"] = df["consumo_mes_referencia"] < df["media_consumo_mes_2018_2019"]
df["atingiu_meta"] = df["atingiu_meta"].map({True: "SIM", False: "NÃO"})

nao_cumpriram = df[df["atingiu_meta"] == "NÃO"]
analise4_df = nao_cumpriram[["orgao", "media_consumo_mes_2018_2019", "consumo_mes_referencia", "justificativa_meta"]].head()

texto_analise4 = "ANÁLISE 4: Justificativas dos órgãos que não atingiram a meta (Top 5)\n\n"
for idx, row in analise4_df.iterrows():
    texto_analise4 += f"Órgão: {row['orgao']}\n"
    texto_analise4 += f"Consumo médio histórico: {row['media_consumo_mes_2018_2019']} kWh\n"
    texto_analise4 += f"Consumo atual: {row['consumo_mes_referencia']} kWh\n"
    texto_analise4 += f"Justificativa: {row['justificativa_meta']}\n"
    texto_analise4 += "-" * 40 + "\n"

with open("analise4.txt", "w", encoding="utf-8") as f:
    f.write(texto_analise4)

# Envio dos resultados para a pasta analises-etapa1/ no Bucket
arquivos = [
    "analise1.txt",
    "analise2.txt",
    "analise3.png",
    "analise4.txt"
]

for arquivo in arquivos:
    s3.upload_file(arquivo, bucket, f"{pasta_s3}{arquivo}")
    print(f"{arquivo} enviado para o bucket '{bucket}' na pasta '{pasta_s3}'")

````

### 📸 Evidências

![amostra1](/Sprint%204/Evidencias/Projeto/etapa1%20de%20analises.png)
![amostra2](/Sprint%204/Evidencias/Projeto/Arquivos%20salvos-etapa1.png)
![amostra3](/Sprint%204/Evidencias/Projeto/arquivos%20no%20bucket.png)

---

### 3. [Etapa III](/Sprint%204/Projeto/etapa2/Projeto-etapa2.ipynb)

Na terceira etapa, foram realizadas análises complementares utilizando funções condicionais, agregações, filtros lógicos e manipulação temporal dos dados.

O foco desta etapa foi aprofundar o tratamento analítico das informações, explorando diferentes abordagens de análise com Pandas.

As atividades desenvolvidas incluíram:

- Comparação entre consumo atual e média histórica  
- Identificação de órgãos que atingiram metas de economia  
- Análise dos maiores consumidores em períodos específicos  
- Avaliação temporal do consumo energético  
- Cálculo de consumo semestral agregado  

Os resultados foram exportados em arquivos `.txt` e armazenados automaticamente no bucket S3, consolidando o fluxo de processamento em nuvem.

````python

import pandas as pd
import boto3
import io

# Configurações
arquivo_csv = "consumo_energia_limpo.csv"
bucket = "bucket-name"
pasta_s3 = "analises-etapa2/"
perfil_aws = "default"

# Leitura do arquivo diretamente do Bucker
session = boto3.Session(profile_name=perfil_aws)
s3 = session.client("s3")

obj = s3.get_object(Bucket=bucket, Key=f"{arquivo_csv}")
df = pd.read_csv(io.BytesIO(obj["Body"].read()), parse_dates=["mes_ano_corrigido"])

# Analise 1: Função de conversão + subtração direta entre colunas numéricas.
# Comparação entre consumo atual e média histórica
df['diferenca'] = df['consumo_mes_referencia'] - df['media_consumo_mes_2018_2019']
analise1 = df[['sigla_orgao', 'media_consumo_mes_2018_2019', 'consumo_mes_referencia', 'diferenca']].head(10)
analise1_txt = "analise1_comparacao_consumo.txt"
analise1.to_string(open(analise1_txt, "w", encoding="utf-8"), index=False)

# Analise 2: Função condicional + Agregação simples
# Quantidade de órgãos que atingiram a meta de economia
df['atingiu_meta'] = df['consumo_mes_referencia'] < df['media_consumo_mes_2018_2019']
resumo_meta = df['atingiu_meta'].value_counts().rename(index={True: 'Atingiram a meta', False: 'Não atingiram'})
analise2_txt = "analise2_resumo_metas.txt"
with open(analise2_txt, "w", encoding="utf-8") as f:
    f.write("Resumo de metas atingidas:\n")
    f.write(resumo_meta.to_string())

# Analise 3: Filtro com operador lógico  + Agregação por grupo
# Top 5 maiores consumidores em 2022
df['ano'] = df['mes_ano_corrigido'].dt.year
consumo_2022 = df[df['ano'] == 2022]
top_consumidores = consumo_2022.groupby('sigla_orgao')['consumo_mes_referencia'].sum().sort_values(ascending=False).head(5)
analise3_txt = "analise3_top_consumidores_2022.txt"
top_consumidores.to_string(open(analise3_txt, "w", encoding="utf-8"))

# Analise 4: Função de string + Organização temporal
# Evolução mensal do consumo de órgãos da área de saúde
min_saude = df[df['orgao'].str.contains('saúde', case=False, na=False)]
evolucao_saude = min_saude[['mes_ano_corrigido', 'consumo_mes_referencia']].sort_values('mes_ano_corrigido')
analise4_txt = "analise4_evolucao_min_saude.txt"
evolucao_saude.to_string(open(analise4_txt, "w", encoding="utf-8"), index=False)

# Analise 5: Função de data + Função condicional  + Agregação temporal
# Total de consumo por semestre
df['semestre'] = df['mes_ano_corrigido'].dt.month.apply(lambda m: 1 if m <= 6 else 2)
consumo_semestral = df.groupby(['ano', 'semestre'])['consumo_mes_referencia'].sum().sort_index()
analise5_txt = "analise5_consumo_semestral.txt"
consumo_semestral.to_string(open(analise5_txt, "w", encoding="utf-8"))

# Envio dos arquivos para o Bucket
for arquivo in [analise1_txt, analise2_txt, analise3_txt, analise4_txt, analise5_txt]:
    s3.upload_file(arquivo, bucket, f"{pasta_s3}{arquivo}")
    print(f" Enviado: {arquivo} → s3://{bucket}/{pasta_s3}{arquivo}")

````
---

# 🛠️ Tecnologias Utilizadas

- 🐍 Python  
- 🐼 Pandas  
- 📊 Matplotlib  
- 🎨 Seaborn  
- ☁️ Amazon S3  
- 🔐 AWS CLI + SSO  
- ⚡ Boto3  

---

# 📈 Resultados Obtidos

- Automatização do upload e leitura de arquivos na AWS  
- Pipeline simples de ETL em ambiente cloud  
- Dados tratados e organizados para análise  
- Integração prática entre Python e serviços AWS  
- Geração automatizada de relatórios e gráficos  
- Estruturação de análises diretamente na nuvem  

---

# 🧠 Aprendizados

- Manipulação de dados com Pandas  
- Integração entre aplicações Python e AWS  
- Utilização prática do Amazon S3  
- Automação de processos com Boto3  
- Estruturação de pipelines de dados  
- Organização de projetos de Engenharia de Dados em cloud  