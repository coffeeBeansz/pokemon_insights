-- models/int/int_pokeapi__pokemons.sql

with source as (
    select species_name, color_name
    from {{ ref('stg_pokeapi__pokemon_species') }}
)

select *
from source