from pyspark.sql import SparkSession
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, '..')
sys.path.append(parent_dir)

from consts import transaction_transformed_path

spark = SparkSession.builder \
    .appName("BD_Tech_Hackathon") \
    .master("spark://127.0.0.1:7077") \
    .getOrCreate()

df = spark.read.parquet(transaction_transformed_path)

print(df.show())