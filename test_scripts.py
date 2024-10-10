import duckdb
from dotenv import load_dotenv
import os


load_dotenv()
DB_NAME = os.getenv('DB_NAME')


def get_table(table_name):
    conn = duckdb.connect(DB_NAME)
    query = f"SELECT * FROM {table_name}"
    df = conn.execute(query).fetchdf()
    conn.close()
    return df


def test__stg_pokeapi__pokemon():
    table_name = 'stg_pokeapi__pokemons'
    df = get_table(table_name)
    print(df['species_name'].iloc[0])
    print(df)


def test__stg_pokeapi__pokemon_species():
    table_name = 'stg_pokeapi__pokemon_species'
    df = get_table(table_name)
    print(df)


def test__int_pokeapi__pokemons():
    table_name = 'int_pokeapi__pokemons'
    df = get_table(table_name)
    print(df)


def test__int_pokeapi__pokemon_species():
    table_name = 'int_pokeapi__pokemon_species'
    df = get_table(table_name)
    print(df)


def test__core_pokeapi__type_and_color():
    table_name = 'core_pokeapi__type_and_color'
    df = get_table(table_name)
    print(df)