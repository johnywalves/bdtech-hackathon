import pandas as pd
import numpy as np
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, '..')
sys.path.append(parent_dir)

from consts import transaction_raw_path, transaction_featured_path

def feature_transactions():
    dataframe = pd.read_parquet(transaction_raw_path, engine='fastparquet')

    dataframe.rename(columns={'internal_store_id': 'pdv', 'internal_product_id': 'produto'}, inplace=True)

    dataframe['date_week'] = np.ceil(dataframe['transaction_date'].dt.day / 7).astype(int)
    dataframe['date_month'] = dataframe['transaction_date'].dt.month

    fifth_week_index = dataframe[dataframe['date_week'] == 5].index
    dataframe.drop(fifth_week_index, inplace=True)

    dataframe.pop('transaction_date')
    dataframe.pop('reference_date')

    dataframe.to_parquet(transaction_featured_path)
    del dataframe
