import sqlite3
import random
import time

# PRODUTOS PARA POPULAÇÃO DO BANCO - ECOMMERCE TECH
nomes_base = ["Smartphone", "Notebook", "Teclado", "Mouse", "Monitor", "Cadeira Gamer", "Fone de Ouvido"]
marcas = ["Tech", "Hyper", "Quantum", "Future", "Eco", "Stellar"]
DB_FILE = "db/ecommerce.db"

def popular_banco():
    print(f"Conectando ao banco de dados '{DB_FILE}'...")
    # CRIAÇÃO DO BANCO DE DADOS E TABELA - SE NÃO EXISTIR
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    print("Criando tabela 'produtos' (se não existir)...")
    
    cursor.execute("DROP TABLE IF EXISTS produtos")
    cursor.execute('''
        CREATE TABLE produtos (
            id_produto INTEGER PRIMARY KEY,
            nome_produto TEXT NOT NULL,
            preco REAL NOT NULL
        )
    ''')

    # CRIAÇÃO DE 10.000.000 PRODUTOS. NÚMERO GRANDE O SUFICIENTE PARA TESTES.
    num_produtos = 10000000
    print(f"Gerando e inserindo {num_produtos} produtos... (Isso pode levar um momento)")
    start_time = time.time()

    ids_gerados = random.sample(range(10000000, 20000000), num_produtos)

    for product_id in ids_gerados:
        nome = f"{random.choice(nomes_base)} {random.choice(marcas)} X{random.randint(100, 999)}"
        preco = round(random.uniform(50.0, 5000.0), 2)
        cursor.execute("INSERT INTO produtos (id_produto, nome_produto, preco) VALUES (?, ?, ?)", (product_id, nome, preco))

    conn.commit() 
    conn.close()
    
    end_time = time.time()
    print(f"Banco de dados populado com sucesso em {end_time - start_time:.2f} segundos!")

if __name__ == '__main__':
    popular_banco()