import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, '..')
sys.path.append(parent_dir)

from consts import pdv_raw_path, products_raw_path, transaction_raw_path 

import pandas as pd

file = open("EXPLORE.md", "w")
file.write("# Resumo da Análise Exploratória\n\n")

def overview_dataframe(path):
    dataframe = pd.read_parquet(path, engine='fastparquet')

    file.write(f"Formato linhas **{dataframe.shape[0]}** colunas **{dataframe.shape[1]}**")
    file.write("\n\n")

    file.write("```bash\n")
    file.write(str(dataframe.head()))
    file.write("\n```")
    file.write("\n\n")

    del dataframe

# Cadastro de PDVs: PDV, On/Off Prem, Categoria (c-store, g-store, liquor etc.), Zipcode.
file.write("## Cadastro de PDVs\n\n")
overview_dataframe(pdv_raw_path)

# Transações: Data, PDV, Produto, Quantidade, Faturamento.
file.write("## Transações\n\n")
overview_dataframe(products_raw_path)

# Cadastro de produtos: Produto, Categoria, Descrição, + até 4 atributos.
file.write("## Cadastro de produtos\n\n")
overview_dataframe(transaction_raw_path)
