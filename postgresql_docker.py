import psycopg2
import pandas as pd
from sqlalchemy import create_engine


df = pd.read_csv('wine.csv')


conn_string = "host='localhost' dbname='postgres' user='postgres'"

conn = psycopg2.connect(conn_string)

cursor = conn.cursor()

engine = create_engine('postgresql://postgres@localhost:5432/postgres')

df.to_sql('wine_test', engine)

df_pg = pd.read_sql_query('select * from wine_test',con=engine)

print(df_pg.head())
print(pd.read_sql_query('select count(*) from wine_test',con=engine))