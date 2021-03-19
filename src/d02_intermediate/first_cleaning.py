from src.d01_data.load_data import df_raw as df
from src.d01_data.load_data import db_connect
import src.d00_utils.mysql_utils as ut

# ---------------------------------------work on empties columns----------------------------------
print("how many columns in the df: ", df.shape)

# to drop the empty columns
df.dropna(how='all', axis=1, inplace=True)

print("how many columns stays after drop empties columns: ", df.shape)

# ----------------------------------------work on empties rows------------------------------------
print("how many rows in the df: ", df.shape)

# to drop the empty rows
df.dropna(how='all', axis=0, inplace=True)

print("how many rows stays after drop empties rows: ", df.shape)
print('there are no empties rows')

# ------------------------------------------delete meta data--------------------------------------


print("columns names :", list(df.columns))
df_nometa = df.drop(columns=['code', 'creator', 'created_t', 'created_datetime', 'last_modified_t', 'last_modified_datetime'])
print(list(df_nometa.columns))
print("how many columns stays after drop meta data: ", df_nometa.shape)

# -------------------------------------------keep only usefull columns--------------------------


df_nutri_score = df[['product_name', 'energy_100g', 'sugars_100g', 'fiber_100g', 'proteins_100g', 'sodium_100g',
                     'saturated-fat_100g', 'nutrition-score-fr_100g', 'nutrition_grade_fr']]

print("I keep the columns needed for Nutri-score 's calcul and the name :",
      list(df_nutri_score.columns))
print("how many columns stays: ", df_nutri_score.shape)

# ----------------------------------------work on empties rows------------------------------------
print("how many rows in the df: ", df_nutri_score.shape)
# to drop the empty rows
df_nutri_score_new = df_nutri_score.dropna(how='all', axis=0, inplace=False)

print("how many rows stays after drop empties rows: ", df_nutri_score_new.shape)

print(df_nutri_score_new.columns)
# -----------------------------------------save first cleaning------------------------------------

df_name = "food_fact"
ut.save_to_mysql(db_connect, df_nutri_score_new, df_name)