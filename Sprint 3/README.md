# 🚀 Projeto

O projeto teve como objetivo aplicar, na prática, os conceitos estudados durante a sprint, utilizando Docker para automatizar um processo de ETL e análise de dados.

A aplicação foi estruturada em múltiplos containers, permitindo separar responsabilidades entre etapas de limpeza e processamento de dados.

Durante o desenvolvimento, foi possível compreender:

- Como criar imagens Docker personalizadas  
- Como executar scripts Python em containers  
- Como compartilhar arquivos entre containers utilizando volumes  
- Como automatizar fluxos utilizando Docker Compose  
- Como estruturar aplicações em ambientes isolados e reutilizáveis  

---

## 🎯 Objetivos Técnicos

- Aplicar conceitos de containerização  
- Automatizar execução de processos ETL  
- Compartilhar dados entre containers  
- Utilizar Docker Compose para orquestração  
- Processar e analisar dados com Python  

---

# 🔄 Etapas

### 1. [Etapa I](/Sprint%203/Projeto/Etapa%201/etl.py) — Limpeza e Tratamento dos Dados  

Na primeira etapa, foi realizada a leitura do dataset `concert_tours_by_women.csv`, seguida pelo processo de limpeza e padronização dos dados.

As principais transformações realizadas foram:

- Remoção de espaços em nomes de colunas  
- Separação dos anos inicial e final das turnês  
- Tratamento de valores nulos  
- Conversão de colunas monetárias para formato numérico  
- Padronização de tipos de dados  
- Criação de ranking baseado no faturamento ajustado  

Ao final do processo, foi gerado o arquivo `csv_limpo.csv`, utilizado nas próximas etapas do pipeline.

````python
import pandas as pd
import re

df = pd.read_csv("concert_tours_by_women.csv")

df.columns = [col.strip() for col in df.columns]

df[['Start year', 'End year']] = df['Year(s)'].str.extract(r'(\d{4})(?:–|-)?(\d{4})?')
df['End year'] = df['End year'].fillna(df['Start year'])

df['Start year'] = df['Start year'].astype(int)
df['End year'] = df['End year'].astype(int)

df = df.dropna(subset=[
    'Actual gross', 
    'Adjustedgross (in 2022 dollars)', 
    'Artist', 
    'Tour title', 
    'Shows', 
    'Average gross', 
    'Start year', 
    'End year'
])

def to_float(val):
    if isinstance(val, str):
        cleaned = re.sub(r"[^\d.]", "", val)
        return float(cleaned) if cleaned else 0.0
    return val

df['Actual gross'] = df['Actual gross'].apply(to_float)
df['Adjustedgross (in 2022 dollars)'] = df['Adjustedgross (in 2022 dollars)'].apply(to_float)
df['Average gross'] = df['Average gross'].apply(to_float)

df['Shows'] = df['Shows'].astype(int)

df = df.rename(columns={"Adjustedgross (in 2022 dollars)": "Adjusted gross (in 2022 dollars)"})

df = df.sort_values(by="Adjusted gross (in 2022 dollars)", ascending=False).reset_index(drop=True)
df["Rank"] = df.index + 1

colunas_desejadas = [
    "Rank",
    "Actual gross",
    "Adjusted gross (in 2022 dollars)",
    "Artist",
    "Tour title",
    "Shows",
    "Average gross",
    "Start year",
    "End year"
]

tabela_filtrada = df[colunas_desejadas]

tabela_filtrada.to_csv("/data/csv_limpo.csv", index=False)

print("Arquivo 'csv_limpo.csv' gerado com sucesso.")
````

### 📸 Evidências

* [amostra](/Sprint%203/Evidencias/Projeto/Codigo/Projeto.ipynb)

---

### 2. [Etapa II](/Sprint%203/Projeto/Etapa%202/job.py) — Análise de Dados  

Após o tratamento dos dados, foi iniciado o processo de análise exploratória.

Nesta etapa, foram realizadas análises relacionadas a:

- Artista mais frequente no dataset  
- Média de faturamento bruto  
- Turnês de maior desempenho  
- Valor médio arrecadado por show  
- Quantidade total de shows por artista  

Além das análises textuais, também foram gerados gráficos para visualização dos resultados.

Arquivos gerados:

- `respostas.txt`
- `Q4.png`
- `Q5.png`

````python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("csv_limpo.csv")

df["valor_por_show"] = df["Adjusted gross (in 2022 dollars)"] / df["Shows"]

most_common_artist = df["Artist"].value_counts().idxmax()
media = df[df["Artist"] == most_common_artist]["Actual gross"].mean()

one_year = df[df["Start year"] == df["End year"]]
melhor = one_year.loc[one_year["Average gross"].idxmax()]

top3 = df.nlargest(3, "valor_por_show")[["Tour title", "Artist", "valor_por_show"]]

with open("/app/volume/respostas.txt", "w") as f:
    f.write(f"Q1:\n--- {most_common_artist} com média de ${media:,.2f}\n\n")
    f.write(f"Q2:\n--- {melhor['Tour title']} ({melhor['Artist']}) com média de ${melhor['Average gross']:,.2f}\n\n")
    f.write("Q3:\n---\n")
    for _, row in top3.iterrows():
        f.write(f"{row['Tour title']} ({row['Artist']}) - ${row['valor_por_show']:,.2f}\n")


df_artista = df[df["Artist"] == most_common_artist]

faturamento_ano = df_artista.groupby("Start year")["Actual gross"].sum().reset_index()

plt.figure(figsize=(10, 6))
sns.lineplot(data=faturamento_ano, x="Start year", y="Actual gross", marker="o")
plt.title(f"Faturamento por ano - {most_common_artist}")
plt.xlabel("Ano de início da turnê")
plt.ylabel("Faturamento bruto (USD)")
plt.grid(True)
plt.tight_layout()
plt.savefig("/app/volume/Q4.png")
plt.close()

top5_artistas = df.groupby("Artist")["Shows"].sum().nlargest(5).reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(data=top5_artistas, x="Artist", y="Shows", hue="Artist", palette="viridis", legend=False)
plt.title("Top 5 artistas com mais shows na lista")
plt.xlabel("Artista")
plt.ylabel("Total de Shows")
plt.tight_layout()
plt.grid(axis="y")
plt.savefig("/app/volume/Q5.png")
plt.close()
````

### 📸 Evidências

* [amostra](/Sprint%203/Evidencias/Projeto/Codigo/Projeto.ipynb)

---

### 3. [Etapa III](/Sprint%203/Projeto/Etapa%201/Dockerfile) — Dockerização da Etapa ETL  

Após a criação do script de ETL, foi desenvolvido um Dockerfile responsável por construir a imagem da aplicação de limpeza e tratamento de dados.

Nesta etapa, foi possível:

- Criar uma imagem baseada em Python  
- Configurar ambiente de execução  
- Instalar dependências necessárias  
- Automatizar a execução do script ETL  

````Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY etl.py .

RUN pip install pandas

CMD ["python", "etl.py"]
````

### 📸 Evidências

![amostra](/Sprint%203/Evidencias/Projeto/ProjetoResultado.png)

---

### 4. [Etapa IV](/Sprint%203/Projeto/Etapa%202/Dockerfile) — Dockerização da Etapa Analítica  

Após a construção do processo ETL, foi criado um segundo Dockerfile voltado para execução da etapa analítica.

O container foi responsável por:

- Ler os dados tratados  
- Executar análises exploratórias  
- Gerar arquivos de saída  
- Produzir gráficos automaticamente  


````Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY job.py .

RUN pip install pandas matplotlib seaborn

CMD ["python", "job.py"]
````

### 📸 Evidências

![amostra](/Sprint%203/Evidencias/Projeto/ProjetoResultado.png)

---


### 5. [Etapa V](/Sprint%203/Projeto/docker-compose.yml) — Orquestração com Docker Compose  

Na etapa final, foi utilizado o Docker Compose para orquestrar toda a aplicação.

A configuração permitiu:

- Execução coordenada dos containers  
- Compartilhamento de volumes entre serviços  
- Dependência entre etapas do pipeline  
- Automatização completa da execução  

Com isso, o pipeline passou a funcionar de forma integrada e reutilizável.


````yml
version: "3.8"

services:
  etl:
    build:
      context: ./Etapa 1
    container_name: etl_cleanup
    volumes:
      - ./Etapa 2:/data
      - ./Etapa 1:/app
    working_dir: /app
    command: ["python", "etl.py"]

  job:
    build:
      context: ./Etapa 2
    container_name: job_analysis
    volumes:
      - ./Etapa 2:/app
      - ./volume:/app/volume
    depends_on:
      - etl
    working_dir: /app
    command: ["sh", "-c", "while [ ! -f csv_limpo.csv ]; do sleep 1; done; python job.py"]

````

### 📸 Evidências

![amostra](/Sprint%203/Evidencias/Projeto/ProjetoResultado.png)
![amostra](/Sprint%203/Evidencias/Projeto/ProjetoResultado2.png)

---

# 📊 Resultados

- Pipeline ETL automatizado com Docker  
- Processamento de dados em containers isolados  
- Compartilhamento de arquivos entre serviços  
- Geração automática de análises e gráficos  
- Estrutura reutilizável e escalável  

---

# 🧠 Aprendizados

- Criação e gerenciamento de containers Docker  
- Construção de imagens com Dockerfile  
- Orquestração com Docker Compose  
- Manipulação e análise de dados com Python  
- Compartilhamento de volumes entre containers  
- Automação de pipelines ETL 