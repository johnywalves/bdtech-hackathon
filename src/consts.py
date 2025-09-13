pdv_raw_path = './data/raw/part-00000-tid-2779033056155408584-f6316110-4c9a-4061-ae48-69b77c7c8c36-4-1-c000.snappy.parquet'
products_raw_path = './data/raw/part-00000-tid-7173294866425216458-eae53fbf-d19e-4130-ba74-78f96b9675f1-4-1-c000.snappy.parquet'
transaction_raw_path = './data/raw/part-00000-tid-5196563791502273604-c90d3a24-52f2-4955-b4ec-fb143aae74d8-4-1-c000.snappy.parquet'

pdv_featured_path = './data/featured/pdvs.parquet'
products_featured_path = './data/featured/products.parquet'
transaction_featured_path = './data/featured/transactions.parquet'

transaction_grouped_path = './data/transformed/grouped.parquet'
transaction_transformed_path = './data/transformed/transactions.parquet'

columns_categorical = [
    'premise', 
    'categoria_pdv', 
    'zipcode_national', 
    'zipcode_sectional', 
    'categoria_produto',
    'tipos_produto',
    'label_produto',
    'subcategoria_produto',
    'marca_produto',
    'fabricante_produto',
]