from main import *

def ver_estoque():
    conn = sqlite3.connect('estoque.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM estoque")
    rows = cursor.fetchall()

    if rows:
        print("ID | Produto | Cor | Tamanho | Depósito | Data Disponibilidade | Quantidade")
        print("-" * 80)
        for row in rows:
            print(f"{row[0]:2} | {row[1]:<7} | {row[2]:<3} | {row[3]:<7} | {row[4]:<9} | {row[5]:<19} | {row[6]:<9}")
    else:
        print("O estoque está vazio.")

    conn.close()

def menu():
    print("""
        [1] - Ver estoque  
        [2] - Criar Estoque
        [3] - Atualizar estoque
        [4] - Sair    
""")
    op = int(input("Digite a Opcao"))
    if op == 1:
        ver_estoque()
    elif op == 2:
        criar_tabela()  
    elif op == 3:
        atualizar_estoque(data)
    elif op == 4:
        pass
    else:
        print("erro")
        menu()

menu()
