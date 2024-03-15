import pymysql
import json

database_sql = "database.sql"

def criar_tabela_estoque():
    conexao = pymysql.connect(
        host='localhost',
        user='root',
        password='2005Joao_',
        database='PHP',  
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        with open(database_sql, "r") as file:
            script_sql = file.read()  # Correção aqui

        with conexao.cursor() as cursor:
            cursor.execute(script_sql)
        
        conexao.commit()
        print("Tabela 'estoque' criada com sucesso!")  

    except Exception as e:
        print(f"Erro ao criar tabela: {str(e)}")
    
    finally:
        conexao.close()

def atualizar_estoque_from_json(arquivo_json):
    with open(arquivo_json, 'r') as arquivo:
        dados_json = json.load(arquivo)

    conexao = pymysql.connect(
        host='localhost',
        user='root',
        password='2005Joao_',
        database='PHP', 
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        with conexao.cursor() as cursor:
            for produto in dados_json:
                cursor.execute("SELECT * FROM estoque WHERE produto = %s AND cor = %s AND tamanho = %s AND deposito = %s AND data_disponibilidade = %s",
                               (produto['produto'], produto['cor'], produto['tamanho'], produto['deposito'], produto['data_disponibilidade']))
                resultado = cursor.fetchone()

                if resultado:
                    cursor.execute("UPDATE estoque SET quantidade = %s WHERE id = %s",
                                   (produto['quantidade'], resultado['id']))
                else:
                    cursor.execute("INSERT INTO estoque (produto, cor, tamanho, deposito, data_disponibilidade, quantidade) VALUES (%s, %s, %s, %s, %s, %s)",
                                   (produto['produto'], produto['cor'], produto['tamanho'], produto['deposito'], produto['data_disponibilidade'], produto['quantidade']))
            
            conexao.commit()
            print("Estoque atualizado com sucesso!")

    finally:
        conexao.close()

criar_tabela_estoque()

arquivo_json = "estoque.json"
atualizar_estoque_from_json(arquivo_json)
