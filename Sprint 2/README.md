# 📌 Introdução

Este projeto teve como objetivo desenvolver habilidades práticas em **análise de dados com Python**, utilizando bibliotecas como Pandas e Matplotlib dentro do ambiente Jupyter Notebook.

Durante a atividade, foram explorados conceitos como leitura de dados, limpeza, transformação e geração de visualizações para extração de insights.

---

## 🎯 Objetivos Técnicos

- Manipulação de dados com Pandas  
- Limpeza e tratamento de dados  
- Análise exploratória (EDA)  
- Criação de visualizações com Matplotlib  
- Geração de insights a partir de dados  

---

## 🔄 Etapas


### 1. [Etapa I](/Sprint%202/Projeto/Projeto_Sprint2.ipynb)

Nesta etapa inicial, foi realizada a **leitura do dataset** e a **remoção de registros duplicados**, garantindo maior qualidade e consistência dos dados para as análises posteriores.

Principais ações:

- Leitura do arquivo CSV  
- Verificação da quantidade de registros  
- Identificação e remoção de duplicidades  
- Visualização inicial dos dados  


````python
import pandas as pd
import matplotlib.pyplot as plt

tabela = pd.read_csv("googleplaystore.csv", sep=",")
print(f'Número de linhas: {len(tabela)}')
tabela.head()

print("Antes:", tabela.shape)

tabela = tabela.drop_duplicates()

print("Depois:", tabela.shape)
display(tabela)
````

#### 📸 Evidências

![amostra](/Sprint%202/Evidencias/Projeto/Leitura.png)
![amostra](/Sprint%202/Evidencias/Projeto/Exclusao_duplicadas.png)

---

### 2. [Etapa II](/Sprint%202/Projeto/Projeto_Sprint2.ipynb)

Após o tratamento inicial, foram realizadas análises exploratórias com o objetivo de extrair insights relevantes a partir dos dados.

#### 📊 Top 5 Apps por Número de Instalações

- Conversão da coluna de instalações para formato numérico  
- Ordenação dos dados  
- Seleção dos aplicativos com maior número de downloads  


````python
tabela['Installs'] = tabela['Installs'].astype(str)
tabela['Installs'] = tabela['Installs'].str.replace('[+,]', '', regex=True)
tabela['Installs'] = pd.to_numeric(tabela['Installs'], errors='coerce')

tabela_unica = tabela.sort_values(by='Installs', ascending=False).drop_duplicates(subset='App', keep='first')

top5_unicos = tabela_unica[['App', 'Installs']].head(5)

plt.figure(figsize=(10,5))
plt.bar(top5_unicos['App'], top5_unicos['Installs'], color='mediumseagreen')
plt.title('Top 5 Apps com Mais Instalações (Nomes Únicos)')
plt.xlabel('App')
plt.ylabel('Instalações')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
````
 **📸 Evidência:**

![amostra](/Sprint%202/Evidencias/Projeto/Etapa2.png)

---

#### 📊 Distribuição de Apps por Categoria

- Contagem de aplicativos por categoria  
- Visualização com gráfico de pizza (Top 10 categorias)  

````python
categorias = tabela['Category'].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(categorias[:10],
        labels=categorias.index[:10],
        autopct='%1.1f%%',
        startangle=140,
        colors=plt.cm.Set3.colors)

plt.title('Distribuição dos Apps por Categoria (Top 10)')
plt.axis('equal')
plt.tight_layout()
plt.show()
````

 **📸 Evidência:**

![amostra](/Sprint%202/Evidencias/Projeto/Etapa3.png)

---

#### 💰 App Mais Caro

- Conversão da coluna de preço para valor numérico  
- Identificação do aplicativo com maior preço  
- Estimativa de receita com base no número de instalações  

````python
tabela['Price'] = tabela['Price'].astype(str).str.replace('$', '', regex=False)
tabela['Price'] = pd.to_numeric(tabela['Price'], errors='coerce')

tabela['Installs'] = tabela['Installs'].astype(str).str.replace('[+,]', '', regex=True)
tabela['Installs'] = pd.to_numeric(tabela['Installs'], errors='coerce')

app_mais_caro = tabela.sort_values(by='Price', ascending=False).iloc[0]

renda_estimada = app_mais_caro['Price'] * app_mais_caro['Installs']

print("App mais caro:")
print(app_mais_caro[['App', 'Price', 'Installs']])
print(f"\n Receita estimada: ${renda_estimada:,.2f}")
````

 **📸 Evidência:**

![amostra](/Sprint%202/Evidencias/Projeto/Etapa4.png)

---

#### 🔞 Apps classificados como "Mature 17+"

- Filtragem dos aplicativos com classificação indicativa específica  
- Análise de categorias e volume de instalações  
- Identificação dos principais apps desse grupo  

````python
mature_apps = tabela[tabela['Content Rating'] == 'Mature 17+']
display(mature_apps[['App', 'Category', 'Rating', 'Installs']].head(10))

print(f"\nTotal de apps classificados como 'Mature 17+': {len(mature_apps)}")

mature_ordenado = mature_apps.sort_values(by='Installs', ascending=False)
top5_mature_unicos = mature_ordenado.drop_duplicates(subset='App', keep='first').head(5)
display(top5_mature_unicos[['App', 'Installs']])

print(mature_apps['Category'].value_counts())
````

 **📸 Evidência:**

![amostra](/Sprint%202/Evidencias/Projeto/Etapa5.1.png)
![amostra](/Sprint%202/Evidencias/Projeto/Etapa5.2.png)
![amostra](/Sprint%202/Evidencias/Projeto/Etapa5.3.png)


---

#### ⭐ Top 10 Apps por Reviews

- Conversão da coluna de reviews para numérico  
- Ordenação por volume de avaliações  
- Seleção dos aplicativos com maior engajamento  

````python
tabela['Reviews'] = pd.to_numeric(tabela['Reviews'], errors='coerce')

ordenado_por_reviews = tabela.sort_values(by='Reviews', ascending=False)
top10_reviews_unicos = ordenado_por_reviews.drop_duplicates(subset='App', keep='first').head(10)

display(top10_reviews_unicos[['App', 'Reviews']])
````

 **📸 Evidência:**

![amostra](/Sprint%202/Evidencias/Projeto/Etapa6.png)

---

### 3. [Etapa III](/Sprint%202/Projeto/Projeto_Sprint2.ipynb)

Nesta etapa final, foram realizadas análises complementares com foco em geração de insights mais aprofundados.

---

#### 📊 App com Mais Reviews por Categoria

- Identificação do aplicativo com maior número de avaliações em cada categoria  
- Seleção das categorias com maior relevância  

````python
tabela['Reviews'] = pd.to_numeric(tabela['Reviews'], errors='coerce')

mais_reviews_por_categoria = tabela.sort_values(by='Reviews', ascending=False).dropna(subset=['Category'])
top_por_categoria = mais_reviews_por_categoria.drop_duplicates(subset='Category', keep='first')

top10 = top_por_categoria.sort_values(by='Reviews', ascending=False).head(10)

categorias = top10['Category']
reviews = top10['Reviews']
nomes_apps = top10['App']

plt.figure(figsize=(10, 6))
plt.barh(categorias, reviews, color='mediumslateblue')
plt.xlabel('Número de Reviews')
plt.title('App com Mais Reviews das Top 10 categorias')
plt.gca().invert_yaxis()

for i, (review, nome) in enumerate(zip(reviews, nomes_apps)):
    plt.text(review, i, f"{nome}", va='center', fontsize=8)

plt.tight_layout()
plt.show()
````

**📸 Evidência:**

![amostra](/Sprint%202/Evidencias/Projeto/Extra1.png)

---

#### 💰 Top 7 Categorias com Maior Lucro Médio

- Cálculo de receita estimada (preço × instalações)  
- Agrupamento por categoria  
- Identificação das categorias mais lucrativas  

````python
tabela['Price'] = tabela['Price'].astype(str).str.replace('$', '', regex=False)
tabela['Price'] = pd.to_numeric(tabela['Price'], errors='coerce')

tabela['Installs'] = tabela['Installs'].astype(str).str.replace('[+,]', '', regex=True)
tabela['Installs'] = pd.to_numeric(tabela['Installs'], errors='coerce')

tabela['Receita'] = tabela['Price'] * tabela['Installs']

media_receita_categoria = tabela.groupby('Category')['Receita'].mean().sort_values(ascending=False)

top7_lucro_medio = media_receita_categoria.head(7)

plt.figure(figsize=(10,6))
plt.barh(top7_lucro_medio.index, top7_lucro_medio.values, color='seagreen')
plt.xlabel('Lucro Médio Estimado (US$)')
plt.title('Top 7 Categorias com Maior Lucro Médio por App')
plt.gca().invert_yaxis()

for i, valor in enumerate(top7_lucro_medio.values):
    plt.text(valor, i, f"${valor:,.0f}", va='center', fontsize=9)

plt.tight_layout()
plt.show()
````

**📸 Evidência:**

![amostra](/Sprint%202/Evidencias/Projeto/Extra2.png)

---

#### 📈 Categorias com Mais Reviews vs Lucro

- Seleção das categorias com maior volume de reviews  
- Análise do lucro médio dessas categorias  
- Comparação entre popularidade e monetização  

````python
tabela['Price'] = tabela['Price'].astype(str).str.replace('$', '', regex=False)
tabela['Price'] = pd.to_numeric(tabela['Price'], errors='coerce')

tabela['Installs'] = tabela['Installs'].astype(str).str.replace('[+,]', '', regex=True)
tabela['Installs'] = pd.to_numeric(tabela['Installs'], errors='coerce')

tabela['Reviews'] = pd.to_numeric(tabela['Reviews'], errors='coerce')

tabela['Receita'] = tabela['Price'] * tabela['Installs']

top7_reviews = (
    tabela.groupby('Category')['Reviews']
    .sum()
    .sort_values(ascending=False)
    .head(7)
    .index
)

tabela_top7_reviews = tabela[tabela['Category'].isin(top7_reviews)]

lucro_medio_top7 = (
    tabela_top7_reviews.groupby('Category')['Receita']
    .mean()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))
plt.barh(lucro_medio_top7.index, lucro_medio_top7.values, color='orange')
plt.xlabel('Lucro Médio Estimado (US$)')
plt.title('Média de Lucro nas 7 Categorias com Mais Reviews')
plt.gca().invert_yaxis()

for i, valor in enumerate(lucro_medio_top7.values):
    plt.text(valor, i, f"${valor:,.0f}", va='center', fontsize=9)

plt.tight_layout()
plt.show()
````

**📸 Evidência:**

![amostra](/Sprint%202/Evidencias/Projeto/Extra3.png)

---

#### 🆓 Apps Gratuitos vs Pagos

- Comparação entre aplicativos gratuitos e pagos  
- Análise da média de reviews  
- Visualização da distribuição entre os tipos  

````python
plt.figure(figsize=(6, 6))
wedges, texts, autotexts = plt.pie(
    media_reviews,
    labels=media_reviews.index,
    autopct='%1.1f%%',
    startangle=90,
    colors=cores,
    pctdistance=0.85
)
centro = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centro)

plt.title('Média de Reviews: Apps Gratuitos vs Pagos \n')
plt.axis('equal')
plt.tight_layout()
plt.show()
````

**📸 Evidência:**

![amostra](/Sprint%202/Evidencias/Projeto/Extra4.png)

---

## 📊 Resultados

- Dados tratados e livres de duplicidade  
- Identificação de padrões de instalação e engajamento  
- Análises de categorias mais populares e lucrativas  
- Geração de insights sobre comportamento de usuários  

---

## 🧠 Aprendizados

- Manipulação e limpeza de dados com Pandas  
- Conversão e tratamento de tipos de dados  
- Criação de visualizações com Matplotlib  
- Análise exploratória de dados (EDA)  
- Interpretação de métricas de negócio  
