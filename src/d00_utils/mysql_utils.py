import mysql.connector
import pymysql
from sqlalchemy import create_engine


def connect_to_mysql():
    """
    connection to mysql and create database
    :return: db_connection
    """
    from conf.conf import mysql_user, mysql_host, mysql_password, database_name
    mydb = mysql.connector.connect(
        host=mysql_host,
        user=mysql_user,
        password=mysql_password)
    cursor = mydb.cursor()
    cursor.execute("""CREATE DATABASE IF NOT EXISTS """ + database_name)
    cursor.execute("""USE """ + database_name)
    db_connection = create_engine(
        'mysql+pymysql://{0}:{1}@localhost/{2}'.format(mysql_user, mysql_password, database_name))
    return db_connection


def save_to_mysql(db_connect, df_to_save, df_name):
    """
    save a dataframe in the sql database
    :param db_connect:
    :param df_to_save:
    :param df_name:
    :return:
    """
    df_to_save.to_sql(con=db_connect, name=df_name, if_exists='replace')


def info_df(df):
    """Function that returns size, datatype and length of a dataframe"""
    print("Nombre de lignes :", len(df.index))  # Display the number of rows
    print(df.head())  # Display the 5 first rows
    print(df.dtypes)  # Display column types
    # Display the column names and their maximum length
    print("max len: ",
          dict([(v, df[v].apply(lambda r: len(str(r)) if r != None else 0).max()) for v in df.columns.values]))
