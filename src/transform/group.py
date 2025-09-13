import pandas as pd
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, '..')
sys.path.append(parent_dir)

from consts import transaction_featured_path, transaction_grouped_path

def transform_group():
    df_transactions = pd.read_parquet(transaction_featured_path, engine='fastparquet')
    df_grouped = df_transactions.groupby(['pdv', 'produto', 'distributor_id', 'date_week', 'date_month']).agg(
        gross_value_mean=('gross_value', 'mean'),
        gross_value_median=('gross_value', 'median'),
        gross_value_min=('gross_value', 'min'),
        gross_value_max=('gross_value', 'max'),
        gross_value_std=('gross_value', 'std'),

        net_value_mean=('net_value', 'mean'),
        net_value_median=('net_value', 'median'),
        net_value_min=('net_value', 'min'),
        net_value_max=('net_value', 'max'),
        net_value_std=('net_value', 'std'),

        gross_profit_mean=('gross_profit', 'mean'),
        gross_profit_median=('gross_profit', 'median'),
        gross_profit_min=('gross_profit', 'min'),
        gross_profit_max=('gross_profit', 'max'),
        gross_profit_std=('gross_profit', 'std'),

        discount_mean=('discount', 'mean'),
        discount_median=('discount', 'median'),
        discount_min=('discount', 'min'),
        discount_max=('discount', 'max'),
        discount_std=('discount', 'std'),

        taxes_mean=('taxes', 'mean'),
        taxes_median=('taxes', 'median'),
        taxes_min=('taxes', 'min'),
        taxes_max=('taxes', 'max'),
        taxes_std=('taxes', 'std'),

        quantity_mean=('quantity', 'mean'),
        quantity_median=('quantity', 'median'),
        quantity_min=('quantity', 'min'),
        quantity_max=('quantity', 'max'),
        quantity_sum=('quantity', 'sum'),
    ).reset_index()

    df_grouped.to_parquet(transaction_grouped_path)