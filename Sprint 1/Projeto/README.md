# Etapas


### 1. [Etapa I](/Sprint%201/Desafio/Etapa%20-%201/Diagrama%20sem%20nome%20imgem.jpg)

Na Primeira etapa houve a identificação do problema, que era o fato de so haver uma tabela no banco de dados e todos os campos estarem misturados nela. Tendo em vista a problematica e com o intuito de facilitar a visualização do sistema normalizado, a primeira coisa feita foi o Diagrama relacional, que permitiu uma visualização clara das tabelas, de onde cada campo deveria fica e como elas iriam se relacionar

![Diagrama](/Sprint%201/Desafio/Etapa%20-%201/Diagrama%20sem%20nome%20imgem.jpg)

---

### 2. [Etapa II](/Sprint%201/Desafio/Etapa%20-%202/CriancaoTabelas.sql)

Após ter feito o diagrama relacional, fica mais facil ir para a segunda etapa, que é a criação das novas Tabelas:

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

![amostra](/Sprint%201/Evidencias/Desafio%20-%20Sprint%201/Codigo1.png)

---

### 3. [Etapa III](/Sprint%201/Desafio/Etapa%20-%203/InsercaoDados.sql)

Após a criação das tabelas, o proximo passo foi a inserção de dados, da tabela locacao antiga para as novas tabelas e depois que os dados foram tranferidos, foi feita a exclusão da antiga tabela não normalizada:

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

![amostra2](/Sprint%201/Evidencias/Desafio%20-%20Sprint%201/Codigo2.png)

---

### 4. [Etapa IV](/Sprint%201/Desafio/Etapa%20-%204/CriacaoViews.sql)

Apos a criação do diagrama relacional, criação das tabelas e a passagem de dados, o ultimo passo é a dimencionalização por meio da criação de views:
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

![amostra2](/Sprint%201/Evidencias/Desafio%20-%20Sprint%201/Codigo3.png)