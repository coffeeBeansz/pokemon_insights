import duckdb
import matplotlib.pyplot as plt
from test_scripts import *
from dotenv import load_dotenv
import os


load_dotenv()
DB_NAME = os.getenv('DB_NAME')


def get_number_of_pokemons():
    conn = duckdb.connect(DB_NAME)
    table_name = 'core_pokeapi__type_and_color'
    query = f"SELECT DISTINCT pokemon_name FROM {table_name}"
    unique_pokemons_df = conn.execute(query).fetchdf()
    conn.close()
    return unique_pokemons_df.shape[0]


def get_list_of_types():
    conn = duckdb.connect(DB_NAME)
    table_name = 'core_pokeapi__type_and_color'
    query = f"SELECT DISTINCT type_name FROM {table_name}"
    unique_colors_series = conn.execute(query).fetchdf()
    conn.close()
    return list(unique_colors_series['type_name'])


def get_pokemons_of_type(type_name):
    conn = duckdb.connect(DB_NAME)
    table_name = 'core_pokeapi__type_and_color'
    query = f"SELECT DISTINCT pokemon_name, color_name FROM {table_name} WHERE type_name = '{type_name}'"
    pokemons_of_type_df = conn.execute(query).fetchdf()
    conn.close()
    return pokemons_of_type_df


def compute_color_percentages_for_type(type_pokemons_df):
    color_percentages = type_pokemons_df.groupby('color_name').size()
    return color_percentages


def plot_and_save_pie_charts():
    pokemon_types = get_list_of_types()
    for pokemon_type in pokemon_types:
        fire_pokemons_df = get_pokemons_of_type(pokemon_type)
        color_percentages = compute_color_percentages_for_type(fire_pokemons_df)
        color_percentages = color_percentages.sort_values(ascending=False)

        current_directory = os.path.dirname(os.path.abspath(__file__))
        save_folder_path = os.path.join(current_directory, 'result_figures')
        
        if not os.path.exists(save_folder_path):
            os.makedirs(save_folder_path)

        figure_name = f'{pokemon_type}_pokemons.png'
        figure_path = os.path.join(save_folder_path, figure_name)

        plt.figure()
        plt.pie(color_percentages, labels=color_percentages.index, autopct='%1.1f%%', colors=color_percentages.keys())
        plt.title(f'Pokemon type: {pokemon_type}')
        plt.savefig(figure_path)


def main():
    plot_and_save_pie_charts()


if __name__ == '__main__':
    main()