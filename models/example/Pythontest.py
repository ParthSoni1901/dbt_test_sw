import snowflake.snowpark.functions as f
from snowflake.snowpark.functions import col
import pandas as pd

def model(dbt,session):
    dbt.config(packages=["pandas"])
    df = dbt.ref("SQLTEST").to_pandas()
    # df = df.filter( 
    #  df.col("EVENT_DATE").like("2024%")
    # )
    df = df[df["EVENT_DATE"].str.startswith("2024")]
    return df

    
