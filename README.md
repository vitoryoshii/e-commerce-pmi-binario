# 🧠 Comparativo de Algoritmos de Busca: Linear vs Binária

Este projeto visa demonstrar e comparar visualmente a eficiência dos algoritmos de **Busca Linear** e **Busca Binária** (Binary Search) na recuperação de dados em uma base de produtos de E-commerce.

O projeto utiliza a biblioteca **Tkinter** para criar uma interface gráfica simples (GUI) que permite ao usuário inserir um ID de produto e observar em tempo real o tempo de execução e o número de passos (comparações) de cada algoritmo.

## 🌟 Destaques do Projeto

* **Comparação de Performance:** Medição precisa do tempo de execução em nanossegundos e contagem exata de passos para ambos os métodos de busca.
* **Interface Gráfica (Tkinter):** Permite uma interação amigável para o input de dados e visualização dos resultados.
* **Simulação de Dados:** O código é estruturado para carregar dados de um banco de dados SQLite simulado (IDs de produtos ordenados) para realizar as buscas.

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **Tkinter:** Para a interface gráfica.
* **SQLite3:** Para simular o carregamento de dados do banco de dados (o arquivo `.db` não está incluído no repositório devido ao seu tamanho, mas o código de criação do banco de dados está presente).
* **Módulos Padrão:** `time` e `messagebox`.

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

2.  **Preparar o Banco de Dados (Opcional - Simulação):**
    > **Atenção:** O arquivo `db/ecommerce.db` não está incluído no repositório. Para que o código funcione, é necessário criar um banco de dados com a estrutura esperada.
    >
    > **Estrutura Esperada:** O código espera que o banco de dados `db/ecommerce.db` contenha a tabela `produtos` com as colunas `id_produto`, `nome_produto` e `preco`.
    >
    > **Alternativa Simples:** Executar o código `db/setup_database.py`, esse scrit executa a criação de um banco de dados com valores aleatórios**.

3.  **Executar o Script:**
    ```bash
    python db/setup_databese.py # Cria o banco de dados com 10.000.000 de valores aleatórios para o ecommerce
    
    python busca_interface.py # Execução do código principal
    ```

## 🔍 Como Usar a Interface

1.  O aplicativo será aberto com a interface Tkinter.
2.  No campo **"Digite o ID do produto:"**, insira um número inteiro (o código espera um ID entre 10.000.000 e 20.000.000, conforme a simulação do DB).
3.  Clique no botão **"🔍 Buscar Produto"**.
4.  Os resultados serão exibidos abaixo, mostrando:
    * O nome e preço do produto encontrado.
    * O tempo de execução em milissegundos (ms) para a Busca Linear.
    * O número de passos (comparações) para a Busca Linear.
    * O tempo de execução em milissegundos (ms) para a Busca Binária.
    * O número de passos (comparações) para a Busca Binária.

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
