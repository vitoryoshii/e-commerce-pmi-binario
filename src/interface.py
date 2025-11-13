"""
===========================================================
INTERFACE GRÁFICA - COMPARATIVO DE BUSCA LINEAR X BINÁRIA

Descrição:
    módulo que  implementa a interface gráfica do projeto
    "Comparativo de Algoritmos de Busca" utilizando Tkinter.

    A aplicação permite:
        - Realizar busca de produtos por código (ID);
        - Comparar o desempenho entre busca linear e binária;
        - Pesquisar produtos por nome com paginação de resultados.

Módulos Importados:
    - tkinter: Interface gráfica
    - time: Medição de desempenho dos algoritmos
    - messagebox: Exibição de alertas e mensagens
    - src.buscas: Funções de busca_linear e busca_binaria

===========================================================
"""


import tkinter as tk
import tkinter.ttk as ttk
import time
from tkinter import messagebox
from src.buscas import busca_linear, busca_binaria


# ===========================================================
# VARIÁVEIS GLOBAIS DE PAGINAÇÃO
# ===========================================================


resultados_busca = []
pagina_atual = 0
resultados_por_pagina = 10


# ===========================================================
# FUNÇÃO DE REALIZAR BUSCA TEXTUAL
# ===========================================================


def realizar_busca_textual(entry_nome, resultado_text, botoes_paginacao, produtos_lista, btn_anterior, btn_proximo):
    """
    Executa a busca textual de produtos com base nas palavras digitadas.

    Parâmetros:
        entry_nome: Campo de entrada de texto
        resultado_text: Variável para exibir resultados
        botoes_paginacao: Container dos botões de navegação
        produtos_lista: Lista de produtos (nome, preço, código)
        btn_anterior: Botão de página anterior
        btn_proximo: Botão de próxima página
    """

    global resultados_busca, pagina_atual

    termo = entry_nome.get().strip().lower()
    if not termo:
        messagebox.showinfo("Aviso", "Digite uma palavra para pesquisar.")
        return
    
    palavras = termo.split()
    resultados_busca = [
        (nome, preco, codigo)
        for nome, preco, codigo in produtos_lista
        if all(p in nome.lower() for p in palavras)
    ]

    if not resultados_busca:
        resultado_text.set("❌ Nenhum produto encontrado.")
        botoes_paginacao.pack_forget()
        return

    pagina_atual = 0
    exibir_pagina(resultado_text, botoes_paginacao, btn_anterior, btn_proximo)


# ===========================================================
# FUNÇÕES DE PAGINAÇÃO
# ===========================================================


def exibir_pagina(resultado_text, botoes_paginacao, btn_anterior, btn_proximo):
    """
    Exibe a página atual de resultados da busca textual.
    """
     
    global pagina_atual

    total = len(resultados_busca)
    inicio = pagina_atual * resultados_por_pagina
    fim = inicio + resultados_por_pagina
    pagina_resultados = resultados_busca[inicio:fim]

    texto = f"🧾 Resultados {inicio+1}–{min(fim, total)} de {total}:\n\n"
    for nome, preco, codigo in pagina_resultados:
        texto += f"• {nome}\n   💰 R$ {preco:.2f} | 🔑 Código: {codigo}\n\n"

    resultado_text.set(texto)
    btn_anterior["state"] = tk.NORMAL if pagina_atual > 0 else tk.DISABLED
    btn_proximo["state"] = tk.NORMAL if fim < total else tk.DISABLED
    botoes_paginacao.pack(pady=(10, 0))


def proxima_pagina(resultado_text, botoes_paginacao, btn_anterior, btn_proximo):
    """
    Avança para a próxima página de resultados.
    """

    global pagina_atual

    pagina_atual += 1
    exibir_pagina(resultado_text, botoes_paginacao, btn_anterior, btn_proximo)


def pagina_anterior(resultado_text, botoes_paginacao, btn_anterior, btn_proximo):
    """
    Retorna para a página anterior de resultados.
    """

    global pagina_atual

    pagina_atual -= 1
    exibir_pagina(resultado_text, botoes_paginacao, btn_anterior, btn_proximo)


# ===========================================================
# FUNÇÃO DE REALIZAR BUSCA
# ===========================================================


def realizar_busca(entry_id, resultado_text, label_linear, label_binaria, cods_buscas, produtos):
    """
    Realiza busca de um produto pelo código e compara os algoritmos.

    Etapas:
        - Captura o código digitado;
        - Executa busca linear e binária;
        - Mede tempo e número de passos;
        - Exibe o produto e o desempenho.

    Parâmetros:
        entry_id: Campo de entrada do ID
        resultado_text: Exibição do resultado
        label_linear: Exibe o desempenho da busca linear
        label_binaria: Exibe o desempenho da busca binária
        cods_buscas: Lista de códigos ordenados
        produtos: Dicionário de produtos
    """

    try:
        cod_busca = int(entry_id.get())
    except ValueError:
        messagebox.showerror("Erro", "Digite um número inteiro válido.")
        return

    if cod_busca < 10000000 or cod_busca > 20000000:
        messagebox.showwarning("Aviso", "Digite um ID entre 10.000.000 e 20.000.000.")
        return

    inicio_linear = time.perf_counter_ns()
    encontrado_linear, passos_linear = busca_linear(cods_buscas, cod_busca)
    fim_linear = time.perf_counter_ns()
    tempo_linear = (fim_linear - inicio_linear) / 1_000_000

    inicio_binaria = time.perf_counter_ns()
    encontrado_binaria, passos_binaria = busca_binaria(cods_buscas, cod_busca)
    fim_binaria = time.perf_counter_ns()
    tempo_binaria = (fim_binaria - inicio_binaria) / 1_000_000

    if encontrado_linear or encontrado_binaria:
        nome, preco = produtos[cod_busca]
        resultado_text.set(f"Produto encontrado:\n📦 {nome}\n💰 R$ {preco:.2f}") 
    else:
        resultado_text.set("❌ Produto não encontrado.") 

    label_linear["text"] = f"🔹 Linear: {tempo_linear:.6f} ms | {passos_linear} passos"
    label_binaria["text"] = f"🔹 Binária: {tempo_binaria:.6f} ms | {passos_binaria} passos"


# ===========================================================
# INTERFACE GRÁFICA COM TKINTER
# ===========================================================


def criar_interface(cods_buscas, produtos, produtos_lista):
    """
    Cria e executa a interface gráfica do comparativo de buscas.

    Parâmetros:
        cods_buscas: Lista de códigos para busca
        produtos: Dicionário com informações dos produtos
        produtos_lista: Lista auxiliar para busca textual
    """

    janela = tk.Tk()
    janela.title("E-commerce Tech")
    janela.geometry("700x600")
    janela.configure(bg="#EDEDED")
    janela.eval('tk::PlaceWindow . center')

    style = ttk.Style()
    style.configure("TFrame", background="#FFFFFF")
    style.configure("TLabel", background="#FFFFFF", font=("Segoe UI", 11))
    style.configure("TButton", font=("Segoe UI", 10, "bold"))
    style.configure("Title.TLabel", font=("Segoe UI", 16, "bold"), background="#EDEDED")
    style.configure("Card.TFrame", background="#FFFFFF", relief="raised", borderwidth=1)

    titulo = ttk.Label(janela, text="Sistema de Buscar de Produto", style="Title.TLabel", anchor="center")
    titulo.pack(pady=(20, 10))

    card = ttk.Frame(janela, style="Card.TFrame")
    card.pack(padx=25, pady=10, fill="both", expand=True)
    card.config(padding=20)

    # ==== CAMPO DE ID ====
    frame_id = ttk.Frame(card)
    frame_id.pack(pady=(5, 10), fill="x")
    ttk.Label(frame_id, text="🔍 Digite o código do produto:", font=("Segoe UI", 11, "bold")).grid(row=0, column=0, padx=5, sticky="w")
    entry_id = ttk.Entry(frame_id, font=("Segoe UI", 11), width=25)
    entry_id.grid(row=0, column=1, padx=10)
    ttk.Button(frame_id, text="Buscar Produto",
               command=lambda: realizar_busca(entry_id, resultado_text, label_linear, label_binaria, cods_buscas, produtos),
               width=18, style="TButton").grid(row=0, column=2, padx=5)

    # ==== CAMPO DE TEXTO ====
    frame_nome = ttk.Frame(card)
    frame_nome.pack(pady=(10, 15), fill="x")
    ttk.Label(frame_nome, text="🧾 Buscar por nome:", font=("Segoe UI", 11, "bold")).grid(row=0, column=0, padx=40,sticky="w")
    entry_nome = ttk.Entry(frame_nome, font=("Segoe UI", 11), width=25)
    entry_nome.grid(row=0, column=1, padx=10)
    ttk.Button(frame_nome, text="Pesquisar",
               command=lambda: realizar_busca_textual(entry_nome, resultado_text, botoes_paginacao, produtos_lista, btn_anterior, btn_proximo),
               width=18).grid(row=0, column=2, padx=5)

    ttk.Separator(card, orient="horizontal").pack(fill="x", pady=5)

    # ==== PAGINAÇÃO ====
    botoes_paginacao = ttk.Frame(card)
    btn_anterior = ttk.Button(botoes_paginacao, text="⬅️ Anterior",
                              command=lambda: pagina_anterior(resultado_text, botoes_paginacao, btn_anterior, btn_proximo),
                              width=12)
    btn_anterior.pack(side="left", padx=5)
    btn_proximo = ttk.Button(botoes_paginacao, text="Próximo ➡️",
                             command=lambda: proxima_pagina(resultado_text, botoes_paginacao, btn_anterior, btn_proximo),
                             width=12)
    btn_proximo.pack(side="left", padx=5)
    botoes_paginacao.pack_forget()

    ttk.Label(card, text="📦 Resultados encontrados:", font=("Segoe UI", 12, "bold")).pack(anchor="w")
    frame_result = ttk.Frame(card)
    frame_result.pack(fill="both", expand=True, pady=(5, 10))

    resultado_text = tk.StringVar()
    ttk.Label(frame_result, textvariable=resultado_text, wraplength=620, justify="left", font=("Segoe UI", 10), background="#FFFFFF").pack(anchor="w", pady=5)

    ttk.Separator(card, orient="horizontal").pack(fill="x", pady=10)

    frame_comp = ttk.Frame(card)
    frame_comp.pack(pady=5, fill="x")
    label_linear = ttk.Label(frame_comp, text="• Linear: --", font=("Segoe UI", 10))
    label_linear.pack(anchor="w", pady=2)
    label_binaria = ttk.Label(frame_comp, text="• Binária: --", font=("Segoe UI", 10))
    label_binaria.pack(anchor="w", pady=2)

    ttk.Label(janela, text="Desenvolvido por Vitor Yoshii", background="#EDEDED", font=("Segoe UI", 9, "italic"), foreground="#555").pack(side="bottom", pady=8)

    janela.mainloop()