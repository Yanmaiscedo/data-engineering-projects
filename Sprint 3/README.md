# Resumo da Sprint

**Docker:** Em relação a Docker, aprendi a utilizar Docker para criar e gerenciar containers, construir imagens com Dockerfile e orquestrar serviços com docker-compose, facilitando o desenvolvimento e a automação de aplicações. No Docker Desktop, acompanhei visualmente o estado de containers, volumes e redes. Com o Postman, testei APIs REST usando requisições como GET e POST, analisando respostas e interações com servidores. Já com Linux, aprendi comandos básicos de terminal, manipulação de arquivos e permissões, o que me ajudou a operar sistemas e ambientes de forma mais eficiente, especialmente em servidores e containers.


## Projeto

**Projeto:** O projeto possibilitou a compreensão prática de como funciona a criação e execução de containers utilizando o Docker, além da construção de imagens com Dockerfile e a orquestração de múltiplos serviços com o docker-compose. Também foi possível entender como compartilhar volumes entre containers para troca de arquivos e como automatizar etapas de um processo de ETL com scripts Python integrados em diferentes containers. A atividade reforçou o uso do Docker Desktop como ferramenta de apoio e proporcionou uma visão clara de como organizar aplicações em ambientes isolados e reutilizáveis.

# Etapas


### 1. [Etapa I](/Sprint%203/Projeto/Etapa%201/etl.py)

Na Primeira etapa houve a leitura do arquivo concert_tours_by_women.csv e a limpeza do mesmo, que gerou um arquivo csv_limpo.csv

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

### Evidencias do codigo

* [amostra](/Sprint%203/Evidencias/Projeto/Codigo/Projeto.ipynb)

---

### 2. [Etapa II](/Sprint%203/Projeto/Etapa%202/job.py)

Depois de tratar os Dados, foi feito as análises e foram gerados os arquivos respostas.txt, Q4.png e Q5.png

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

### Evidencias do codigo

* [amostra](/Sprint%203/Evidencias/Projeto/Codigo/Projeto.ipynb)

---

### 3. [Etapa III](/Sprint%203/Projeto/Etapa%201/Dockerfile)

Depois de ter feito o arquivo etl.py, foi necessario fazer o arquivo Dockerfile que irá rodá-lo

````Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY etl.py .

RUN pip install pandas

CMD ["python", "etl.py"]
````

### Evidencias do codigo

![amostra](/Sprint%203/Evidencias/Projeto/ProjetoResultado.png)

---

### 4. [Etapa IV](/Sprint%203/Projeto/Etapa%202/Dockerfile)

E depois de ter feito o arquivo job.py, foi necessario fazer o arquivo Dockerfile que irá rodá-lo

````Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY job.py .

RUN pip install pandas matplotlib seaborn

CMD ["python", "job.py"]
````

### Evidencias do codigo

![amostra](/Sprint%203/Evidencias/Projeto/ProjetoResultado.png)

---


### 5. [Etapa V](/Sprint%203/Projeto/docker-compose.yml)

Depois de ter feito os Dockerfiles, chegou a ultima etapa, que é o arquivo docker-compose que ira gerenciar toda a aplicação

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

### Evidencias do codigo

![amostra](/Sprint%203/Evidencias/Projeto/ProjetoResultado.png)
![amostra](/Sprint%203/Evidencias/Projeto/ProjetoResultado2.png)
