from dotenv import dotenv_values
from faker import Faker
import sqlite3 as SQ

MAX_RANGE = 5
config = dotenv_values(".env")
faker = Faker()

def SQL_query(db_name,SQL_text):
    with SQ.connect(db_name) as conn:
        conn.execute(SQL_text)
        conn.commit()

def SQL_insert(db_name,SQL_text,insert_values):
    with SQ.connect(db_name) as conn:
        conn.executemany(SQL_text,insert_values)
        conn.commit()

def read_table(db_name,table_name):
    with SQ.connect(db_name) as conn:
        curr = conn.cursor()
        SQL_text = {"sql":f'SELECT * FROM {config["TABLE1"]}'}
        return curr.execute(SQL_text["sql"])
    
SQL_text = F'''DROP TABLE IF EXISTS {config["TABLE1"]};'''
SQL_query(db_name=config["DATABASE_NAME"],SQL_text=SQL_text)

SQL_text = F'''CREATE TABLE IF NOT EXISTS {config["TABLE1"]} ( \
    {config["TABLE_COLUMN1"]} INTEGER PRIMARY KEY AUTOINCREMENT, \
        {config["TABLE_COLUMN2"]} VARCHAR(100) NOT NULL UNIQUE \
        );'''
SQL_query(db_name=config["DATABASE_NAME"],SQL_text=SQL_text)
a_user = [(faker.unique.first_name(),) for each in range(MAX_RANGE)]
SQL_text = F'''INSERT into {config["TABLE1"]} ({config["TABLE_COLUMN2"]}) \
                            VALUES (?);'''
SQL_insert(db_name=config["DATABASE_NAME"],SQL_text=SQL_text,insert_values=a_user)
rows=read_table(db_name=config["DATABASE_NAME"],table_name=config["TABLE1"])
for row in rows:
    print(f'{row}')





# print(f"{config}")

# for key,value in  config.items():
#     print(f'{key}-->{value}')

# DB = config["DATABASE_NAME"]
# print(f'{DB}')
# from os import getenv

# load_dotenv()

# DB = getenv("DATABASE_NAME")

# print(f'{DB}')

#read the config vars
