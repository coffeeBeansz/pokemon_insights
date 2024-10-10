import requests as rq
import pandas as pd
import duckdb

table_names = {
    'ability': 'src_ability',
    'berry': 'src_berry',
    'berry-firmness': 'src_berry_firmness',
    'berry-flavor': 'src_berry_flavor',
    'characteristic': 'src_characteristic',
    'contest-effect': 'src_contest_effect',
    'contest-type': 'src_contest_type',
    'egg-group': 'src_egg_group',
    'encounter-condition': 'src_encounter_condition',
    'encounter-condition-value': 'src_encounter_condition_value',
    'encounter-method': 'src_encounter_method',
    'evolution-chain': 'src_evolution_chain',
    'evolution-trigger': 'src_evolution_trigger',
    'gender': 'src_gender',
    'generation': 'src_generation',
    'growth-rate': 'src_growth_rate',
    'item': 'src_item',
    'item-attribute': 'src_item_attribute',
    'item-category': 'src_item_category',
    'item-fling-effect': 'src_item_fling_effect',
    'item-pocket': 'src_item_pocket',
    'language': 'src_language',
    'location': 'src_location',
    'location-area': 'src_location_area',
    'machine': 'src_machine',
    'move': 'src_move',
    'move-ailment': 'src_move_ailment',
    'move-battle-style': 'src_move_battle_style',
    'move-category': 'src_move_category',
    'move-damage-class': 'src_move_damage_class',
    'move-learn-method': 'src_move_learn_method',
    'move-target': 'src_move_target',
    'nature': 'src_nature',
    'pal-park-area': 'src_pal_park_area',
    'pokeathlon-stat': 'src_pokeathlon_stat',
    'pokedex': 'src_pokedex',
    'pokemon': 'src_pokemon',
    'pokemon-color': 'src_pokemon_color',
    'pokemon-form': 'src_pokemon_form',
    'pokemon-habitat': 'src_pokemon_habitat',
    'pokemon-shape': 'src_pokemon_shape',
    'pokemon-species': 'src_pokemon_species',
    'region': 'src_region',
    'stat': 'src_stat',
    'super-contest-effect': 'src_super_contest_effect',
    'type': 'src_type',
    'version': 'src_version',
    'version-group': 'src_version_group',
}


def main():
    base_url = 'https://pokeapi.co/api/v2/'

    response = rq.get(base_url)
    endpoints = response.json()

    conn = duckdb.connect("pokeapi_database.duckdb")

    for table_name, endpoint in endpoints.items():
        print(f'Fetching data for table {table_name}')
        all_data = []
        while endpoint:
            print(endpoint)
            response = rq.get(endpoint)
            data = response.json()
            data['results']

            for item in data['results']:
                item_response = rq.get(item['url'])
                item_data = item_response.json()
                all_data.append(item_data)
            
            endpoint = data['next']
        
        print(len(all_data))
        df = pd.DataFrame(all_data)

        conn.execute(f"CREATE TABLE IF NOT EXISTS {table_names[table_name]} AS SELECT * FROM df")

    conn.close()


if __name__ == '__main__':
    main()