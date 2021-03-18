import pandas as pd
import src.d00_utils.mysql_utils as ut
from conf import conf

# connect to mysql ad create database
db_connect = ut.connect_to_mysql()

# create a df from tsv
df = pd.read_csv(conf.db_local_path, sep='\t',  low_memory=False)
df_to_clean = df.sample(n=10000)

# how many columns?
print(df_to_clean)
#163 columns

# show empties columns (if sum=10000)
print(df_to_clean.isnull().sum())

#dataframe.drop(columns=['nomdelacolonne', 'nomdelacolonne'])


# save data to clean
df_name = "food_fact"
ut.save_to_mysql(db_connect, df_to_clean, df_name)
