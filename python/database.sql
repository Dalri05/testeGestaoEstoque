USE `PHP`;

CREATE TABLE IF NOT EXISTS estoque (
    `id` INT UNSIGNED AUTO_INCREMENT NOT NULL,
    `produto` VARCHAR(100) NOT NULL,
    `cor` VARCHAR(100) NOT NULL,
    `tamanho` VARCHAR(100) NOT NULL,
    `deposito` VARCHAR(100) NOT NULL,
    `data_disponibilidade` DATE NOT NULL,
    `quantidade` INT UNSIGNED NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `estoque_un` (`produto`, `cor`, `tamanho`, `deposito`, `data_disponibilidade`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

