import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import warnings
warnings.filterwarnings('ignore')

import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, '..')
sys.path.append(parent_dir)

from consts import \
    transaction_transformed_path, \
    columns_categorical, \
    columns_numerical, \
    transaction_transformed_X_path, \
    transaction_transformed_Y_path

def transform_preprocessor():
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), columns_numerical),
            ('cat', OneHotEncoder(handle_unknown='ignore'), columns_categorical)
        ])
    
    df = pd.read_parquet(transaction_transformed_path, engine='fastparquet')
    X = df.drop('quantity_sum', axis=1)
    y = df['quantity_sum']

    x_transformed = preprocessor.fit_transform(X)

    pd.DataFrame(x_transformed).to_parquet(transaction_transformed_X_path)
    pd.DataFrame(y).to_parquet(transaction_transformed_Y_path)
