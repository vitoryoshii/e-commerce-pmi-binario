"""
===========================================================
Descrição:
    Módulo responsável por gerenciar o acesso ao banco
    de dados SQLite do sistema de e-commerce. Ele realiza a
    leitura dos produtos cadastrados e retorna as estruturas
    necessárias para execução dos algoritmos de busca
    (linear e binária), bem como a busca textual.

    O arquivo é projetado para funcionar de forma independente
    da localização do script principal, utilizando caminhos
    relativos com base na estrutura do projeto.
===========================================================
"""


import sqlite3
import os


# ===========================================================
# FUNÇÃO PARA CARREGAR DADOS DO BANCO PARA MEMÓRIA
# ===========================================================


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(BASE_DIR, "../db/ecommerce.db")
DB_FILE = os.path.normpath(DB_FILE)

    
def carregar_dados(caminho_db=DB_FILE):
    """
    Carrega os dados do banco SQLite para a memória.

    Retorna:
        tuple(list, dict, list): 
            - Lista de IDs dos produtos
            - Dicionário com ID como chave e (nome, preço) como valor
            - Lista de tuplas (nome, preço, ID) para busca textual
    """
    print("🔄 Carregando dados do banco...")

    conn = sqlite3.connect(caminho_db)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT codigo_busca, nome_produto, preco
        FROM produtos
        WHERE codigo_busca IS NOT NULL
    """)
    dados = cursor.fetchall()
    conn.close()

    cods_buscas = [linha[0] for linha in dados]
    cods_buscas.sort()  

    produtos = {linha[0]: (linha[1], linha[2]) for linha in dados}
    produtos_lista = [(linha[1], linha[2], linha[0]) for linha in dados] 

    print(f"✅ {len(cods_buscas)} produtos carregados.")
    return cods_buscas, produtos, produtos_lista