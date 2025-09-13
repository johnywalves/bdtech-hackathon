import pandas as pd
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, '..')
sys.path.append(parent_dir)

from consts import pdv_featured_path, products_featured_path, transaction_grouped_path, transaction_transformed_path

def transform_merge():
    df_transactions = pd.read_parquet(transaction_grouped_path, engine='fastparquet')

    df_pdvs = pd.read_parquet(pdv_featured_path, engine='fastparquet')
    df_transaction_pdvs = pd.merge(df_transactions, df_pdvs, on=['pdv'], how='inner', validate='m:1')

    df_products = pd.read_parquet(products_featured_path, engine='fastparquet')
    df_transaction_pdvs_products = pd.merge(df_transaction_pdvs, df_products, on=['produto'], how='inner', validate='m:1')

    df_transaction_pdvs_products.to_parquet(transaction_transformed_path)