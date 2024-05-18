from dotenv import dotenv_values
from os import getenv

# load_dotenv()

# DB = getenv("DATABASE_NAME")

# print(f'{DB}')

config = dotenv_values(".env")
print(f"{config}")

for key,value in  config.items():
    print(f'{key}-->{value}')

DB = config["DATABASE_NAME"]
print(f'{DB}')