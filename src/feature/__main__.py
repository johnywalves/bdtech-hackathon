import pandas as pd
import numpy as np

pdv_path = './data/featured/pdvs.parquet'
products_path = './data/featured/products.parquet'
transaction_path = './data/featured/transactions.parquet'

def pdvs():
    path = './data/raw/part-00000-tid-2779033056155408584-f6316110-4c9a-4061-ae48-69b77c7c8c36-4-1-c000.snappy.parquet'
    dataframe = pd.read_parquet(path, engine='fastparquet')

    dataframe['zipcode'] = dataframe.zipcode.astype(str)
    dataframe['zipcode_national'] = dataframe.zipcode.str[0:1]
    dataframe['zipcode_sectional'] = dataframe.zipcode.str[1:3]
    dataframe['zipcode_delivery'] = dataframe.zipcode.str[3:5]

    dataframe.pop('zipcode')

    dataframe.to_parquet(pdv_path) 
    del dataframe

def products():
    path = './data/raw/part-00000-tid-7173294866425216458-eae53fbf-d19e-4130-ba74-78f96b9675f1-4-1-c000.snappy.parquet'
    dataframe = pd.read_parquet(path, engine='fastparquet')
    
    dataframe.to_parquet(products_path)
    del dataframe    

def transactions():
    path = './data/raw/part-00000-tid-5196563791502273604-c90d3a24-52f2-4955-b4ec-fb143aae74d8-4-1-c000.snappy.parquet'
    dataframe = pd.read_parquet(path, engine='fastparquet')

    dataframe.rename(columns={'internal_store_id': 'pdv', 'internal_product_id': 'produto'}, inplace=True)

    dataframe['date_week'] = np.ceil(dataframe['transaction_date'].dt.day / 7).astype(int)
    dataframe['date_month'] = dataframe['transaction_date'].dt.month

    dataframe.pop('transaction_date')
    dataframe.pop('reference_date')

    dataframe.to_parquet(transaction_path)
    del dataframe

pdvs()
products()
transactions()
