import pandas as pd

pdv_path = './data/featured/pdvs.parquet'
transaction_path = './data/featured/transactions.parquet'
history_path = './data/featured/history.parquet'

def merge():
    df_pdvs = pd.read_parquet(pdv_path, engine='fastparquet')
    df_transactions = pd.read_parquet(transaction_path, engine='fastparquet')

    df_history = pd.concat([df_pdvs, df_transactions], keys=['pdv', 'internal_store_id'])
    df_history.to_parquet(history_path)

merge()