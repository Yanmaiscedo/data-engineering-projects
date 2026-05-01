# 📌 Introdução

Este projeto tem como objetivo aplicar conceitos de **modelagem de dados relacional** e **normalização de banco de dados**, a partir de um cenário real onde os dados estavam originalmente concentrados em uma única tabela não estruturada.

A partir desse problema inicial, foi realizado um processo completo de reestruturação dos dados, incluindo:

* Identificação de inconsistências e redundâncias
* Criação de um **diagrama relacional**
* Separação dos dados em entidades normalizadas
* Definição de chaves primárias e estrangeiras
* Migração dos dados para o novo modelo
* Criação de **views** para facilitar consultas analíticas

O projeto simula uma base de dados de **locação de veículos**, envolvendo entidades como clientes, carros, vendedores e combustíveis, permitindo explorar tanto conceitos de modelagem transacional quanto preparação para análises.

Ao final, a estrutura criada possibilita uma melhor organização dos dados, redução de redundâncias e maior eficiência na realização de consultas.

---

### 🎯 Objetivos Técnicos

- Aplicar normalização (1FN, 2FN e 3FN)
- Estruturar um modelo relacional consistente
- Garantir integridade referencial
- Preparar os dados para análises futuras (camada analítica)

---

## 🔄 Etapas

### 1. [Etapa I](/Sprint%201/Projeto/Etapa%20-%201/Diagrama%20sem%20nome%20imgem.jpg)

Nesta etapa, foi realizada a análise da tabela original (`tb_locacao`), onde todos os dados estavam centralizados, gerando redundâncias e dificultando a manutenção.

A partir disso, foi criado um **diagrama relacional**, com o objetivo de:

- Identificar entidades principais  
- Definir atributos  
- Estabelecer relacionamentos  
- Preparar a normalização dos dados  

![Diagrama](/Sprint%201/Projeto/Etapa%20-%201/Diagrama%20sem%20nome%20imgem.jpg)

---

### 2. [Etapa II](/Sprint%201/Projeto/Etapa%20-%202/CriancaoTabelas.sql)

Com base no modelo relacional, foram criadas as tabelas normalizadas, separando os dados em entidades distintas.

Foram aplicados conceitos como:

- **PRIMARY KEY** para identificação única  
- **FOREIGN KEY** para relacionamentos  
- Organização conforme boas práticas

````sql
CREATE TABLE combustiveis (
    idCombustivel INTEGER PRIMARY KEY,
    tipoCombustivel TEXT
)

CREATE TABLE clientes (
    idCliente INTEGER PRIMARY KEY,
    nomeCliente TEXT,
    cidadeCliente TEXT,
    estadoCliente TEXT,
    paisCliente TEXT
)

CREATE TABLE vendedores (
    idVendedor INTEGER PRIMARY KEY,
    nomeVendedor TEXT,
    sexoVendedor INTEGER,
    estadoVendedor TEXT
)

CREATE TABLE carros (
    idCarro INTEGER PRIMARY KEY,
    kmCarro INTEGER,
    chassiCarro TEXT,
    marcaCarro TEXT,
    modeloCarro TEXT,
    anoCarro INTEGER,
    idCombustivel INTEGER,
    FOREIGN KEY (idCombustivel) REFERENCES combustiveis(idCombustivel)
)

CREATE TABLE locacoes (
    idLocacao INTEGER PRIMARY KEY,
    idCliente INTEGER,
    idCarro INTEGER,
    idVendedor INTEGER,
    dataLocacao TEXT,
    horaLocacao TEXT,
    qtdDiaria INTEGER,
    vlrDiaria REAL,
    dataEntrega TEXT,
    horaEntrega TEXT,
    FOREIGN KEY (idCliente) REFERENCES clientes(idCliente),
    FOREIGN KEY (idCarro) REFERENCES carros(idCarro),
    FOREIGN KEY (idVendedor) REFERENCES vendedores(idVendedor)
)
````

### Evidencias do codigo

![amostra](/Sprint%201/Evidencias/Projeto%20-%20Sprint%201/Codigo1.png)
![amostra](/Sprint%201/Evidencias/Projeto%20-%20Sprint%201/Diagrama_Tabelas.png)

---

### 3. [Etapa III](/Sprint%201/Projeto/Etapa%20-%203/InsercaoDados.sql)

Nesta etapa, foi realizada a migração dos dados da tabela original para as novas tabelas.

O processo incluiu:

- Uso de `SELECT DISTINCT` para evitar duplicidades  
- Separação dos dados por entidade  
- Garantia de consistência dos dados  
- Validação com consultas SQL  

Após a validação, a tabela original foi removida.

 ```sql
INSERT INTO combustiveis (idCombustivel, tipoCombustivel)
SELECT DISTINCT idcombustivel, tipoCombustivel
FROM tb_locacao

INSERT INTO clientes (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT DISTINCT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM tb_locacao

INSERT INTO vendedores (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
SELECT DISTINCT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM tb_locacao

INSERT INTO carros (idCarro, kmCarro, chassiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel)
SELECT idCarro, kmCarro, chassiCarro, marcaCarro, modeloCarro, anoCarro, idcombustivel
FROM tb_locacao
WHERE idLocacao IN (
    SELECT MIN(idLocacao)
    FROM tb_locacao
    GROUP BY idCarro
)

INSERT INTO locacoes (
    idLocacao, idCliente, idCarro, idVendedor,
    dataLocacao, horaLocacao, qtdDiaria, vlrDiaria,
    dataEntrega, horaEntrega
)
SELECT DISTINCT
    idLocacao, idCliente, idCarro, idVendedor,
    dataLocacao, horaLocacao, qtdDiaria, vlrDiaria,
    dataEntrega, horaEntrega
FROM tb_locacao


SELECT * FROM locacoes
SELECT * FROM clientes
SELECT * FROM carros
SELECT * FROM combustiveis
SELECT * FROM vendedores

PRAGMA table_info(locacoes)
PRAGMA table_info(clientes)
PRAGMA table_info(carros)
PRAGMA table_info(combustiveis)
PRAGMA table_info(vendedores)

DROP TABLE  tb_locacao 
 ```
### Evidencias do codigo

![amostra2](/Sprint%201/Evidencias/Projeto%20-%20Sprint%201/Codigo2.png)

---

### 4. [Etapa IV](/Sprint%201/Projeto/Etapa%20-%204/CriacaoViews.sql)

Nesta etapa final, foram criadas **views analíticas** para facilitar consultas e análises.

As views permitem:

- Visualização simplificada dos dados  
- Cálculo de métricas  
- Análise de desempenho (clientes, vendedores, carros)  
- Preparação para consumo analítico
 ```sql
CREATE VIEW vw_Locacao_Detalhada AS
SELECT
    l.idLocacao AS "ID Locacao",
    l.idCliente AS Cliente,
    l.idCarro AS Carro,
    l.idVendedor AS Vendedor,
    l.dataLocacao AS "Data Locacao",
    l.horaLocacao AS "Hora Locacao",
    l.qtdDiaria AS "Quantidade Diaria",
    l.vlrDiaria AS "Valor Diaria",
    l.dataEntrega AS "Data Entrega",
    l.horaEntrega AS "Hora Entrega"
FROM locacoes l;

CREATE VIEW vw_Especificacoes_Carro AS
SELECT 
    ca.idCarro AS "Id Carro",
    ca.kmCarro AS "Kilometragem Carro",
    ca.chassiCarro AS Chassi,
    ca.marcaCarro AS Marca,
    ca.modeloCarro AS Modelo,
    ca.anoCarro AS Ano,
    cb.tipoCombustivel AS "Tipo Combustivel"
FROM carros ca
JOIN combustiveis cb ON ca.idCombustivel = cb.idCombustivel;

CREATE VIEW vw_Locacao_ValorTotal AS
SELECT 
    idLocacao AS "ID Locacao",
    qtdDiaria AS "Quntidade diaria",
    vlrDiaria AS "Valor diaria",
    (qtdDiaria * vlrDiaria) AS valorTotal
FROM locacoes;

CREATE VIEW vw_Cliente_Detalhado AS
SELECT 
    idCliente AS "ID Cliente",
    nomeCliente AS Nome,
    cidadeCliente AS Cidade,
    estadoCliente AS Estado,
    paisCliente AS Pais
FROM clientes;

CREATE VIEW vw_Vendedor_Detalhado AS
SELECT 
    idVendedor AS "ID Vendedor",
    nomeVendedor AS Nome,
    sexoVendedor AS Sexo,
    estadoVendedor AS Estado
FROM vendedores;

CREATE VIEW vw_Geografia_Cliente AS
SELECT DISTINCT
    estadoCliente AS Estado,
    cidadeCliente AS Cidade,
    paisCliente AS Pais
FROM clientes;

CREATE VIEW vw_Utilizacao_Carro AS
SELECT 
    idCarro AS "ID Carro",
    COUNT(*) AS "Locacoes total",
    SUM(qtdDiaria) AS "Dias Locados total"
FROM locacoes
GROUP BY idCarro;

CREATE VIEW vw_Performance_Vendedor AS
SELECT 
    idVendedor AS "ID Vendedor",
    COUNT(*) AS "Locacoes total",
    SUM(qtdDiaria * vlrDiaria) AS "Faturamento total"
FROM locacoes
GROUP BY idVendedor;

CREATE VIEW vw_Fidelidade_Cliente AS
SELECT 
    idCliente AS "ID Cliente",
    COUNT(*) AS "Locacoes total",
    SUM(qtdDiaria * vlrDiaria) AS "Total Gasto"
FROM locacoes
GROUP BY idCliente;

```
### Evidencias do codigo

![amostra2](/Sprint%201/Evidencias/Projeto%20-%20Sprint%201/Codigo3.png)
![amostra](/Sprint%201/Evidencias/Projeto%20-%20Sprint%201/Diagrama_Views.png)