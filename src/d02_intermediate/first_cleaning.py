from src.d01_data.load_data import df_to_clean as df

# ---------------------------------------work on empties columns----------------------------------
# to look how many columns in the df
print(df.shape)

# to drop the empty columns
df.dropna(how='all', axis=1, inplace=True)

# to see how many columns stays
print(df.shape)

# ----------------------------------------work on empties rows------------------------------------
# to look how many rows in the df
print(df.shape)

# to drop the empty rows
df.dropna(how='all', axis=0, inplace=True)

# to see how many columns stays
print(df.shape)

# there is no empty rows

# ------------------------------------------delete meta data--------------------------------------

# show columns names
print(list(df.columns))
df_nometa = df.drop(columns=['code', 'creator', 'created_t', 'created_datetime', 'last_modified_t', 'last_modified_datetime'])
print(list(df_nometa.columns))
# to see how many columns stays
print(df_nometa.shape)

# -------------------------------------------keep only usefull columns--------------------------

#i keep name prody=uct and everything needed for th e nutri-score calcul
df_nutri_score = df[['product_name', 'energy_100g', 'sugars_100g', 'fiber_100g', 'proteins_100g', 'sodium_100g', 'saturated-fat_100g', 'nutrition-score-fr_100g', 'nutrition_grade_fr']]
print(list(df_nutri_score.columns))
# to see how many columns stays
print(df_nutri_score.shape)

# -----------------------------------------save first cleaning------------------------------------
# df_name = "food_fact"
# ut.save_to_mysql(db_connect, df_to_clean, df_name)