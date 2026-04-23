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
