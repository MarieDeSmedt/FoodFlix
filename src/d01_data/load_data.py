import pandas as pd
import src.d00_utils.mysql_utils as ut
from conf import conf

# connect to mysql ad create database
db_connect = ut.connect_to_mysql()

# create a df from tsv
df_to_clean = pd.read_csv(conf.db_local_path, sep='\t', nrows=10000, low_memory=False)

print(ut.info_df(df_to_clean))


#save data to clean
df_name = "food_fact"
ut.save_to_mysql(db_connect, df_to_clean, df_name)





