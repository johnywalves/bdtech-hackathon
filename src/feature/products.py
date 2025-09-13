import pandas as pd
import numpy as np
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, '..')
sys.path.append(parent_dir)

from consts import products_raw_path, products_featured_path

def feature_products():
    dataframe = pd.read_parquet(products_raw_path, engine='fastparquet')

    dataframe.rename(columns={
        'categoria': 'categoria_produto',
        'tipos': 'tipos_produto',
        'label': 'label_produto',
        'subcategoria': 'subcategoria_produto',
        'marca': 'marca_produto',
        'fabricante': 'fabricante_produto',
        }, inplace=True)
    
    dataframe.pop('descricao')
    
    dataframe.to_parquet(products_featured_path)
    del dataframe
