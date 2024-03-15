<?php

$dsn = 'mysql:host=localhost;dbname=PHP;charset=utf8mb4';
$username = 'root';
$password = '2005Joao_';

try {
    $pdo = new PDO($dsn, $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    echo 'Erro de conexão: ' . $e->getMessage();
    exit;
}

function atualizarEstoque($pdo, $produtos)
{
    $pdo->beginTransaction();
    try {
        foreach ($produtos as $produto) {
            $sql = "SELECT id, quantidade FROM estoque WHERE produto = ? AND cor = ? AND tamanho = ? AND deposito = ? AND data_disponibilidade = ?";
            $stmt = $pdo->prepare($sql);
            $stmt->execute([$produto['produto'], $produto['cor'], $produto['tamanho'], $produto['deposito'], $produto['data_disponibilidade']]);
            $row = $stmt->fetch(PDO::FETCH_ASSOC);

            if ($row) {
                $novaQuantidade = $row['quantidade'] + $produto['quantidade'];
                $sql = "UPDATE estoque SET quantidade = ? WHERE id = ?";
                $stmt = $pdo->prepare($sql);
                $stmt->execute([$novaQuantidade, $row['id']]);
            } else {
                $sql = "INSERT INTO estoque (produto, cor, tamanho, deposito, data_disponibilidade, quantidade) VALUES (?, ?, ?, ?, ?, ?)";
                $stmt = $pdo->prepare($sql);
                $stmt->execute([$produto['produto'], $produto['cor'], $produto['tamanho'], $produto['deposito'], $produto['data_disponibilidade'], $produto['quantidade']]);
            }
        }
        $pdo->commit();
        echo "Estoque atualizado com sucesso!";
    } catch (PDOException $e) {
        $pdo->rollBack();
        echo "Erro ao atualizar o estoque: " . $e->getMessage();
    }
}

$json = '[
    {
        "produto": "10.01.0419",
        "cor": "00",
        "tamanho": "P",
        "deposito": "DEP1",
        "data_disponibilidade": "2023-05-01",
        "quantidade": 15
    },
    {
        "produto": "11.01.0568",
        "cor": "08",
        "tamanho": "P",
        "deposito": "DEP1",
        "data_disponibilidade": "2023-05-01",
        "quantidade": 2
    },
    {
        "produto": "11.01.0568",
        "cor": "08",
        "tamanho": "M",
        "deposito": "DEP1",
        "data_disponibilidade": "2023-05-01",
        "quantidade": 4
    },
    {
        "produto": "11.01.0568",
        "cor": "08",
        "tamanho": "G",
        "deposito": "1",
        "data_disponibilidade": "2023-05-01",
        "quantidade": 6
    },
    {
        "produto": "11.01.0568",
        "cor": "08",
        "tamanho": "P",
        "deposito": "DEP1",
        "data_disponibilidade": "2023-06-01",
        "quantidade": 8
    }
]';

$produtos = json_decode($json, true);

atualizarEstoque($pdo, $produtos);

?>
