import pandas as pd
import src.d00_utils.mysql_utils as ut
from conf import conf

# connect to mysql ad create database
db_connect = ut.connect_to_mysql()

# create a df from tsv
df = pd.read_csv(conf.db_local_path, sep='\t', low_memory=False)
df_raw = df.sample(n=100000)

# save in mysql
df_name = "raw_data"
#ut.save_to_mysql(db_connect, df_raw, df_name)

