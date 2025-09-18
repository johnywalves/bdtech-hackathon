import pandas as pd
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, '..')
sys.path.append(parent_dir)

from consts import transaction_featured_path, transaction_grouped_path

def transform_group():
    df_transactions = pd.read_parquet(transaction_featured_path, engine='fastparquet')
    df_grouped = df_transactions.groupby(['pdv', 'produto', 'date_week', 'date_month']).agg(
        gross_value_median=('gross_value', 'median'),
        net_value_median=('net_value', 'median'),
        gross_profit_median=('gross_profit', 'median'),
        discount_median=('discount', 'median'),
        taxes_median=('taxes', 'median'),
        quantity_sum=('quantity', 'sum'),
    ).reset_index()

    df_grouped.to_parquet(transaction_grouped_path)