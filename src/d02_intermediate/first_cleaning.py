from src.d01_data.load_data import df_to_clean as df


# ---------------------------------------work on empties columns----------------------------------
# to look how many columns in the df
print(df.shape)

# to drop the empty columns
df.dropna(how='all', axis=1, inplace=True)

# to see how many columns stays
print(df.shape)

# ----------------------------------------work on empties rows------------------------------------





# -----------------------------------------save first cleaning------------------------------------
# df_name = "food_fact"
# ut.save_to_mysql(db_connect, df_to_clean, df_name)
