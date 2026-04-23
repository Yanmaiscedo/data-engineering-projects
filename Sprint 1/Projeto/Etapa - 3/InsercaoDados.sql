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