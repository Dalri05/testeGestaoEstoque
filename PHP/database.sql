DROP TABLE IF EXISTS estoque;

CREATE TABLE estoque (
    id INT UNSIGNED AUTO_INCREMENT NOT NULL,
    produto VARCHAR(100) NOT NULL,
    cor VARCHAR(100) NOT NULL,
    tamanho VARCHAR(100) NOT NULL,
    deposito VARCHAR(100) NOT NULL,
    data_disponibilidade DATE NOT NULL,
    quantidade INT UNSIGNED NOT NULL,
    CONSTRAINT estoque_pk PRIMARY KEY (id),
    CONSTRAINT estoque_un UNIQUE KEY (produto, cor, tamanho, deposito, data_disponibilidade)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

INSERT INTO estoque (produto, cor, tamanho, deposito, data_disponibilidade, quantidade)
VALUES
    ('10.01.0419', '00', 'P', 'DEP1', '2023-05-01', 15),
    ('11.01.0568', '08', 'P', 'DEP1', '2023-05-01', 2),
    ('11.01.0568', '08', 'M', 'DEP1', '2023-05-01', 4),
    ('11.01.0568', '08', 'G', '1', '2023-05-01', 6),
    ('11.01.0568', '08', 'P', 'DEP1', '2023-06-01', 8);
