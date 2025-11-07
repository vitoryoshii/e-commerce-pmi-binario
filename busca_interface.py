"""
===========================================================
COMPARATIVO DE ALGORITMOS DE BUSCA - LINEAR X BINÁRIA
Autor: Vitor Yoshii

Descrição:
    Este programa compara o desempenho entre dois algoritmos
    de busca Linear e Binária, utilizando dados fictícios de 
    um e-comerce armazenados em um banco de dados. 
    
    A interface gráfica (Tkinter) permite que o usuário:
        - Informe o ID de um produto (entre 10.000.000 e 20.000.000);
        - Veja o tempo de execução (ms);
        - Compara a quantidade de passos de cada algoritimo;
        - Visualize o nome e preço do produto encontrado.

Conceitos de aplicações abordados:
    - Estruturas de dados (listas, dicionários)
    - Busca Linear e Binária
    - Acesso a banco de dados SQLite
    - Interface gráfica com Tkinter
    - Medição de desempenho com time.perf_counter_ns()
===========================================================
"""


import sqlite3
import time
import tkinter as tk
from tkinter import messagebox # Exibe alerta e mensagens para o usuário


# ===========================================================
# FUNÇÕES DE BUSCA BINÁRIA E LINEAR
# ===========================================================
def busca_linear(lista, alvo):
    """
    Realiza uma busca linear (sequencial) em uma lista.
    
    Parâmetros:
        lista (list): lista de elementos a serem percorridos
        alvo (int): valor a ser encontrado

    Retorna:
        tuple(bool, int): 
            - True se o elemento for encontrado, False caso contrário
            - Quantidade de passos realizados até o término da busca
    """

    passos = 0
    for item in lista:
        passos += 1
        if item == alvo:
            return True, passos
    return False, passos


def busca_binaria(lista, alvo):
    """
    Realiza uma busca binária em uma lista ORDENADA.
    
    Parâmetros:
        lista (list): lista ordenada de elementos
        alvo (int): valor a ser encontrado

    Retorna:
        tuple(bool, int): 
            - True se o elemento for encontrado, False caso contrário
            - Quantidade de passos realizados até o término da busca

    Observação:
        A busca binária divide o problema pela metade a cada iteração,
        tornando uma busca muito mais eficiente que a busca linear.
    """

    esquerda = 0
    direita = len(lista) - 1
    passos = 0
    while esquerda <= direita:
        passos += 1
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return True, passos
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return False, passos


# ===========================================================
# FUNÇÕES DE BANCO DE DADOS
# ===========================================================
def carregar_dados(caminho_db="db/ecommerce.db"):
    """
    Carrega os dados do banco SQLite para a memória.

    Retorna:
        tuple(list, dict): 
            - Lista de IDs dos produtos
            - Dicionário com ID como chave e (nome, preço) como valor
    """
    print("🔄 Carregando dados do banco...")

    conn = sqlite3.connect(caminho_db)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id_produto, nome_produto, preco
        FROM produtos
    """)
    dados = cursor.fetchall()
    conn.close()

    ids = [linha[0] for linha in dados]
    produtos = {linha[0]: (linha[1], linha[2]) for linha in dados}

    print(f"✅ {len(ids)} produtos carregados.")
    return ids, produtos


# ===========================================================
# FUNÇÃO DE REALIZAR BUSCA
# ===========================================================
def realizar_busca():
    """
    Função responsável por:
        - Capturar o ID digitado pelo usuário;
        - Executar a busca linear e binária;
        - Medir o tempo e número de passos de cada algoritmo;
    """

    try:
        id_busca = int(entry_id.get())
    except ValueError:
        messagebox.showerror("Erro", "Digite um número inteiro válido.")
        return

    if id_busca < 10000000 or id_busca > 20000000:
        messagebox.showwarning("Aviso", "Digite um ID entre 10.000.000 e 20.000.000.")
        return

    # ---- BUSCA LINEAR ----
    inicio_linear = time.perf_counter_ns()
    encontrado_linear, passos_linear = busca_linear(ids, id_busca)
    fim_linear = time.perf_counter_ns()
    tempo_linear = (fim_linear - inicio_linear) / 1_000_000

    # ---- BUSCA BINÁRIA ----
    inicio_binaria = time.perf_counter_ns()
    encontrado_binaria, passos_binaria = busca_binaria(ids, id_busca)
    fim_binaria = time.perf_counter_ns()
    tempo_binaria = (fim_binaria - inicio_binaria) / 1_000_000

    # ---- EXIBIR RESULTADOS ----
    if encontrado_linear or encontrado_binaria:
        nome, preco = produtos[id_busca]
        resultado_text.set(f"Produto encontrado:\n📦 {nome}\n💰 R$ {preco:.2f}") 
    else:
        resultado_text.set("❌ Produto não encontrado.") 

    label_linear["text"] = f"🔹 Linear: {tempo_linear:.6f} ms | {passos_linear} passos"
    label_binaria["text"] = f"🔹 Binária: {tempo_binaria:.6f} ms | {passos_binaria} passos"


# ===========================================================
# INTERFACE GRÁFICA COM TKINTER
# ===========================================================
def criar_interface():
    """
    Cria a interface gráfica do programa.
    """
    global entry_id, resultado_text, label_linear, label_binaria

    janela = tk.Tk()
    janela.title("Comparativo de Busca Linear x Binária")
    janela.geometry("520x360")
    janela.config(bg="#f2f2f2")

    # ---- TÍTULO ----
    titulo = tk.Label(
        janela, 
        text="🧠 Comparativo de Algoritmos de Busca", 
        font=("Segoe UI", 14, "bold"), 
        bg="#f2f2f2"
    )
    titulo.pack(pady=15)

    # ---- ENTRADA DE DADOS ----
    frame_input = tk.Frame(janela, bg="#f2f2f2")
    frame_input.pack(pady=5)

    tk.Label(
        frame_input, 
        text="Digite o ID do produto:", 
        font=("Segoe UI", 11), bg="#f2f2f2"
    ).grid(row=0, column=0, padx=5)

    entry_id = tk.Entry(frame_input, font=("Segoe UI", 11), width=20)
    entry_id.grid(row=0, column=1, padx=5)

    # ---- BOTÃO DE BUSCA ----
    tk.Button(
        janela, 
        text="🔍 Buscar Produto", 
        font=("Segoe UI", 11, "bold"),
        bg="#4CAF50", fg="white", relief="flat", 
        command=realizar_busca
    ).pack(pady=10)

    # ---- RESULTADOS ----
    resultado_text = tk.StringVar()

    tk.Label(
        janela, 
        textvariable=resultado_text, 
        font=("Segoe UI", 11), bg="#f2f2f2", fg="#333", 
        justify="center"
    ).pack(pady=15)

    # ---- COMPARATIVO DE TEMPOS ----
    label_linear = tk.Label(janela, text="🔹 Linear: --", font=("Segoe UI", 10), bg="#f2f2f2")
    label_linear.pack(pady=2)

    label_binaria = tk.Label(janela, text="🔹 Binária: --", font=("Segoe UI", 10), bg="#f2f2f2")
    label_binaria.pack(pady=2)

    # ---- RODAPÉ ----
    tk.Label(
        janela, 
        text="Desenvolvido por Vitor Yoshii 🧠", 
        font=("Segoe UI", 9, "italic"), bg="#f2f2f2", fg="#666"
    ).pack(side="bottom", pady=10)

    janela.mainloop()

# ===========================================================
# EXECUÇÃO PRINCIPAL
# ===========================================================
if __name__ == "__main__":
    ids, produtos = carregar_dados()
    criar_interface()
