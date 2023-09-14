from functools import lru_cache
import pandas as pd

@lru_cache(maxsize=None)  
def fetch_data_from_source(parquet_file):
    df = pd.read_parquet(f"https://data3001-racing.s3.ap-southeast-2.amazonaws.com/{parquet_file}")
    return df

# Call the decorated function to fetch data
df = fetch_data_from_source('f1sim-data-2022.parquet')

# fetch_data_from_source.cache_clear()  # Clears the cache

