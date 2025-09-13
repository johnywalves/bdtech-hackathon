import pandas as pd
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, '..')
sys.path.append(parent_dir)

from consts import transaction_transformed_path, columns_categorical

snippet_bash_start = "```bash\n"
snippet_bash_end = "\n```\n\n"

def transform_report():
    file = open("PREPARED.md", "w")
    file.write("# Resumo da base preparada\n\n")
 
    dataframe = pd.read_parquet(transaction_transformed_path, engine='fastparquet')

    file.write(f"Formato linhas **{dataframe.shape[0]}** colunas **{dataframe.shape[1]}**")
    file.write("\n\n")

    file.write("## Nome das colunas\n\n")

    file.write(snippet_bash_start)
    file.write(str(dataframe.columns))
    file.write(snippet_bash_end)

    file.write("## Primeiros registros\n\n")

    file.write(snippet_bash_start)
    file.write(str(dataframe.head()))
    file.write(snippet_bash_end)

    file.write("## Exploração dos campos categóricos\n\n")

    for field in columns_categorical:
        file.write(f"**Campo**: {field}\n\n")
        file.write(snippet_bash_start)
        file.write(str(dataframe[field].value_counts()))
        file.write(snippet_bash_end)
