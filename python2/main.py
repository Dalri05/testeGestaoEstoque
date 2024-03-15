import sqlite3
import json

def criar_tabela():
    conn = sqlite3.connect('estoque.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS estoque (
        id INTEGER PRIMARY KEY,
        produto TEXT NOT NULL,
        cor TEXT NOT NULL,
        tamanho TEXT NOT NULL,
        deposito TEXT NOT NULL,
        data_disponibilidade DATE NOT NULL,
        quantidade INTEGER NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

def atualizar_estoque(data):
    conn = sqlite3.connect('estoque.db')
    cursor = conn.cursor()

    try:
        for item in data:
            cursor.execute("SELECT * FROM estoque WHERE produto = ? AND cor = ? AND tamanho = ? AND deposito = ? AND data_disponibilidade = ?",
                           (item['produto'], item['cor'], item['tamanho'], item['deposito'], item['data_disponibilidade']))
            row = cursor.fetchone()

            if row:
                nova_quantidade = row[6] + item['quantidade']
                cursor.execute("UPDATE estoque SET quantidade = ? WHERE id = ?", (nova_quantidade, row[0]))
            else:
                cursor.execute("INSERT INTO estoque (produto, cor, tamanho, deposito, data_disponibilidade, quantidade) VALUES (?, ?, ?, ?, ?, ?)",
                               (item['produto'], item['cor'], item['tamanho'], item['deposito'], item['data_disponibilidade'], item['quantidade']))

        conn.commit()
        print("Atualização do estoque concluída com sucesso.")

    except Exception as e:
        conn.rollback()
        print("Ocorreu um erro durante a atualização do estoque:", str(e))

    finally:
        conn.close()

estoque_json = "estoque.json"

with open(estoque_json) as file:
    data = json.load(file)

criar_tabela()

atualizar_estoque(data)
