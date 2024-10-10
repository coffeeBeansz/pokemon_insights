-- models/int/int_pokeapi__pokemons.sql

with source as (
    select pokemon_name, type_name, species_name
    from {{ ref('stg_pokeapi__pokemons') }}
)

select *
from source