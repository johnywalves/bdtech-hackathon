import pandas as pd
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, '..')
sys.path.append(parent_dir)

from consts import pdv_raw_path, pdv_featured_path

def feature_pdvs():
    dataframe = pd.read_parquet(pdv_raw_path, engine='fastparquet')

    dataframe['zipcode'] = dataframe.zipcode.astype(str)
    dataframe['zipcode_national'] = dataframe.zipcode.str[0:1]
    dataframe['zipcode_sectional'] = dataframe.zipcode.str[0:3]

    dataframe.pop('zipcode')

    dataframe.to_parquet(pdv_featured_path) 
    del dataframe
