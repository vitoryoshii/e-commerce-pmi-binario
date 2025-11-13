"""
===========================================================
MÓDULO PRINCIPAL - E-COMMERCE (Busca Linear x Binária)

Descrição:
    Módulo inicializador do sistema de comparação entre os
    algoritmos de busca Linear e Binária. Ele é responsável
    por carregar os dados do banco SQLite e iniciar a 
    interface gráfica (Tkinter) que permite interação com o 
    usuário.

Estrutura:
    - Importa funções principais do projeto
    - Carrega dados do banco de dados para memória interna
    - Inicializa a interface de pesquisa

Módulos importados:
    - src.database: contém a função `carregar_dados` 
      responsável por extrair os produtos do banco SQLite.
    - src.interface: contém a função `criar_interface` 
      responsável por renderizar a interface Tkinter.
===========================================================
"""


from src.database import carregar_dados
from src.interface import criar_interface

if __name__ == "__main__":
    cods_buscas, produtos, produtos_lista = carregar_dados()
    criar_interface(cods_buscas, produtos, produtos_lista)
