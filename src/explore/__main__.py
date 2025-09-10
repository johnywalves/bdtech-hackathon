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
overview_dataframe('./data/raw/part-00000-tid-2779033056155408584-f6316110-4c9a-4061-ae48-69b77c7c8c36-4-1-c000.snappy.parquet')

# Transações: Data, PDV, Produto, Quantidade, Faturamento.
file.write("## Transações\n\n")
overview_dataframe('./data/raw/part-00000-tid-5196563791502273604-c90d3a24-52f2-4955-b4ec-fb143aae74d8-4-1-c000.snappy.parquet')

# Cadastro de produtos: Produto, Categoria, Descrição, + até 4 atributos.
file.write("## Cadastro de produtos\n\n")
overview_dataframe('./data/raw/part-00000-tid-6364321654468257203-dc13a5d6-36ae-48c6-a018-37d8cfe34cf6-263-1-c000.snappy.parquet')
