"""
===========================================================
SCRIPT: setup_database.py
Autor: Vitor Yoshii / GitHub: @vitoryoshii
Autor: Beatriz Silva 
Data: 2025-11-11

Descrição:
    Cria e popula o banco de dados 'ecommerce.db' com 
    10.000.000 produtos fictícios e gera códigos de busca
    aleatórios ("codigo_busca") embaralhados, simulando
    um ambiente de e-commerce com milhões de registros.

Estrutura da tabela:
    - id_produto (INTEGER PRIMARY KEY)
    - nome_produto (TEXT)
    - preco (REAL)
    - codigo_busca (INTEGER)

Recursos implementados:
    - Inserção em lotes
    - Geração de códigos únicos e aleatórios
    - Mensagens de progresso otimizadas
    - Totalmente compatível com o sistema de busca Tkinter

===========================================================
"""

import sqlite3
import random
import time
import os


# ===========================================================
# CONFIGURAÇÕES GERAIS
# ===========================================================
NOMES_PRODUTOS = [
    "Smartphone", "Notebook", "Teclado", "Mouse", 
    "Monitor", "Cadeira Gamer", "Fone de Ouvido", 
    "Carregador", "Webcam", "Headset"
]
MARCAS = ["Tech", "Hyper", "Quantum", "Future", "Eco", "Stellar", "Prime", "Next"]

DB_DIR = "db"
DB_FILE = os.path.join(DB_DIR, "ecommerce.db")


# ===========================================================
# FUNÇÃO: criar_banco
# ===========================================================
def criar_banco():
    """Cria a pasta e o banco de dados com a tabela 'produtos'."""
    if not os.path.exists(DB_DIR):
        os.makedirs(DB_DIR)

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS produtos")
    cursor.execute("""
        CREATE TABLE produtos (
            id_produto INTEGER PRIMARY KEY,
            nome_produto TEXT NOT NULL,
            preco REAL NOT NULL,
            codigo_busca INTEGER
        )
    """)

    conn.commit()
    conn.close()
    print("✅ Banco criado com sucesso!")


# ===========================================================
# FUNÇÃO: popular_banco
# ===========================================================
def popular_banco():
    """
    Popula o banco de dados com 10 milhões de produtos fictícios.

    - IDs: variam de 10.000.000 a 19.999.999 (únicos)
    - Nome e preço gerados aleatoriamente
    - Inserção em blocos de 50.000 registros para eficiência
    """
    print(f"🔗 Conectando ao banco: {DB_FILE}")
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    total_produtos = 10_000_000
    batch_size = 50_000

    print(f"⚙️  Gerando {total_produtos:,} produtos fictícios...")
    start_time = time.time()

    ids_embaralhados = random.sample(range(10_000_000, 20_000_000), total_produtos)
    produtos = []

    for i, pid in enumerate(ids_embaralhados, 1):
        nome = f"{random.choice(NOMES_PRODUTOS)} {random.choice(MARCAS)} X{random.randint(100, 999)}"
        preco = round(random.uniform(50.0, 5000.0), 2)
        produtos.append((pid, nome, preco, None)) 

        if len(produtos) == batch_size:
            cursor.executemany(
                "INSERT INTO produtos (id_produto, nome_produto, preco, codigo_busca) VALUES (?, ?, ?, ?)",
                produtos
            )
            conn.commit()
            produtos.clear()
            print(f"🧱 Inseridos {i:,}/{total_produtos:,} registros...")

    # Inserir o restante
    if produtos:
        cursor.executemany(
            "INSERT INTO produtos (id_produto, nome_produto, preco, codigo_busca) VALUES (?, ?, ?, ?)",
            produtos
        )
        conn.commit()

    conn.close()
    end_time = time.time()
    print(f"✅ Banco populado com sucesso em {end_time - start_time:.2f} segundos!")


# ===========================================================
# FUNÇÃO: gerar_codigo_busca
# ===========================================================
def gerar_codigo_busca():
    """
    Gera e preenche a coluna 'codigo_busca' com valores únicos e aleatórios.
    """
    print("\n🎲 Iniciando geração dos códigos de busca...")
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Verifica se a coluna já existe
    cursor.execute("PRAGMA table_info(produtos);")
    colunas = [info[1] for info in cursor.fetchall()]
    if "codigo_busca" not in colunas:
        print("🆕 Adicionando coluna 'codigo_busca'...")
        cursor.execute("ALTER TABLE produtos ADD COLUMN codigo_busca INTEGER;")
        conn.commit()

    # Pega todos os IDs
    cursor.execute("SELECT id_produto FROM produtos;")
    ids = [linha[0] for linha in cursor.fetchall()]
    total = len(ids)
    print(f"📦 Total de produtos: {total:,}")

    # Gera códigos únicos e embaralhados
    codigos = list(range(10_000_000, 10_000_000 + total))
    random.shuffle(codigos)

    # Atualiza em lotes
    print("💾 Atualizando banco (pode demorar alguns minutos)...")
    lotes = 50_000
    for i in range(0, total, lotes):
        batch = [(codigos[j], ids[j]) for j in range(i, min(i + lotes, total))]
        cursor.executemany("UPDATE produtos SET codigo_busca = ? WHERE id_produto = ?;", batch)
        conn.commit()
        print(f"✔️  {min(i + lotes, total):,}/{total:,} registros atualizados")

    conn.close()
    print("✅ Coluna 'codigo_busca' preenchida com sucesso!")


# ===========================================================
# EXECUÇÃO PRINCIPAL
# ===========================================================
if __name__ == "__main__":
    criar_banco()
    popular_banco()
    gerar_codigo_busca()
    print("\n🚀 Processo finalizado com sucesso!")
