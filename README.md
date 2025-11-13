# 🧠 Comparativo de Algoritmos de Busca: Linear vs Binária

Este projeto demonstra e compara **a eficiência dos algoritmos de busca Linear e Binária** na recuperação de dados de uma base de produtos de E-commerce, utilizando uma interface gráfica em **Tkinter**.

O objetivo é mostrar de forma prática a diferença entre as duas abordagens, evidenciando a performance e o número de passos necessários para encontrar um item dentro de grandes volumes de dados.

## 🌟 Destaques do Projeto

- ⚡ **Comparação de performance:** Mede com precisão o tempo de execução (em nanossegundos) e o número de passos de cada algoritmo.  
- 🖥️ **Interface Gráfica (Tkinter):** Permite ao usuário inserir um código de busca e visualizar os resultados em tempo real.  
- 🧩 **Integração com Banco SQLite:** Os produtos são carregados diretamente de um banco de dados local.  
- 🌀 **Códigos embaralhados (`codigo_busca`):** Cada produto recebe um código aleatório, simulando buscas não sequenciais e realistas.

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Tkinter** — Interface gráfica do usuário.
- **SQLite3** — Banco de dados local (o arquivo `.db` não está incluído no repositório devido ao seu tamanho, mas o código de criação do banco de dados está presente).
- **Módulos padrão:** `time`, `os`, `random`, `sqlite3`, `tkinter.messagebox`.

## 🗂️ Estrutura do Projeto

```bash
e-commerce-pmi-binario/
│
├── db/
│   └── ecommerce.db              # Banco de dados SQLite (gerado pelo script)
│
├── src/
│   ├── __init__.py               # Define o pacote src
│   ├── main.py                   # Ponto de entrada do sistema
│   ├── database.py               # Conexão e carregamento dos dados do banco
│   ├── buscas.py                 # Implementação dos algoritmos de busca (Linear e Binária)
│   ├── interface.py              # Interface gráfica em Tkinter (comparativo de desempenho)
│   └── popular_database.py       # Criação do banco e geração de dados aleatórios
│
├── .gitignore                    # Arquivos ignorados pelo Git
└── README.md                     # Documentação do projeto
```

## ⚙️ Como Executar o Projeto

Para executar este projeto, você precisará de um ambiente Python configurado.

### Pré-requisitos

1.  **Python 3.x** instalado.

### Configuração e Execução

1.  **Clone o Repositório:**
    ```bash
    git clone https://github.com/vitoryoshii/e-commerce-pmi-binario.git
    cd e-commerce-pmi-binario
    ```

2.  **Preparar o Banco de Dados:**
    > **Atenção:** O arquivo `db/ecommerce.db` não está incluído no repositório. Para que o código funcione, é necessário criar um banco de dados com a estrutura esperada.
    >
    > **Estrutura Esperada:** O código espera que o banco de dados `db/ecommerce.db` contenha a tabela `produtos` com as colunas `id_produto`, `nome_produto`, `preco` e `codigo_busca`.
    >
    > **Alternativa Simples:** Executar o código `src/popular_database.py`, esse scrit executa a criação de um banco de dados com valores aleatórios.

3.  **Executar o Script:**
    ```bash
    python src/popular_databese.py # Cria o banco de dados com 10.000.000 de valores aleatórios para o ecommerce
    
    python -m src.main # Execução do código principal
    ```

## 🧾 Como Usar a Interface

A interface foi criada com **Tkinter** e possui duas formas principais de busca:  
🔹 **Busca por código do produto (comparativo de algoritmos)**  
🔹 **Busca textual (por nome do produto, com paginação)**

---

### 🔍 1. Busca por Código do Produto

1. No campo **"🔍 Digite o código do produto:"**, insira um número inteiro.  
   - O código deve estar entre **10.000.000 e 20.000.000** (intervalo usado na simulação).
2. Clique no botão **"Buscar Produto"**.
3. O sistema fará duas buscas:
   - **Busca Linear:** percorre a lista inteira.
   - **Busca Binária:** utiliza divisão e comparação otimizada.
4. O resultado exibirá:
   - Nome e preço do produto encontrado.  
   - Tempo de execução e número de passos para cada algoritmo.
  
---

### 🧠 2. Busca Textual (por nome)

1. No campo **"🧾 Buscar por nome (rejaques):"**, digite parte do nome de um produto.  
   - Você pode digitar várias palavras (exemplo: `smartphone tech`).
2. Clique em **"Pesquisar"**.
3. O sistema exibirá todos os produtos que contêm as palavras digitadas.
4. Use os botões **⬅️ Anterior** e **➡️ Próximo** para navegar entre os resultados.

## 📝 Algoritmos Implementados

O projeto implementa duas funções de busca:

### 1. Busca Linear (`busca_linear`)

* Percorre a lista elemento por elemento.
* **Complexidade:** $O(n)$
* Ideal para listas pequenas ou não ordenadas.

### 2. Busca Binária (`busca_binaria`)

* Divide o espaço de busca pela metade a cada passo. **Requer que a lista esteja ordenada.**
* **Complexidade:** $O(\log n)$
* Ideal para listas grandes e ordenadas.

## 🧑‍💻 Autor
[Vitor Yoshii](https://github.com/vitoryoshii)
