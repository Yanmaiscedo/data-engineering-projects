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