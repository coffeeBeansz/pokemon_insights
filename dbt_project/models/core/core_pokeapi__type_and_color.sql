-- models/core/core_pokeapi__type_and_color.sql

with pokemons as (
    select *
    from {{ ref('int_pokeapi__pokemons') }}
),
pokemon_species as (
    select *
    from {{ ref('int_pokeapi__pokemon_species') }}
)

select 
    p.pokemon_name,
    p.type_name,
    ps.color_name
from pokemons p
left join pokemon_species ps
    on p.species_name = ps.species_name