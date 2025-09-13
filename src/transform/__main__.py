import pandas as pd

pdv_featured_path = './data/featured/pdvs.parquet'
products_featured_path = './data/featured/products.parquet'
transaction_featured_path = './data/featured/transactions.parquet'

transaction_transformed_path = './data/transformed/transactions.parquet'

def transactions():
    df_transactions = pd.read_parquet(transaction_featured_path, engine='fastparquet')
    df_grouped = df_transactions.groupby(['pdv', 'produto', 'distributor_id']).agg(
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

    df_pdvs = pd.read_parquet(pdv_featured_path, engine='fastparquet')
    df_transaction_pdvs = pd.merge(df_grouped, df_pdvs, on=['pdv'], how='inner', validate='m:1')

    df_products = pd.read_parquet(products_featured_path, engine='fastparquet')
    df_transaction_pdvs_products = pd.merge(df_transaction_pdvs, df_products, on=['produto'], how='inner', validate='m:1')

    df_transaction_pdvs_products.to_parquet(transaction_transformed_path)

transactions()



