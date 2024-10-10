-- models/stg/stg_pokeapi__pokemon_colors.sql

with source as (
    select *
    from {{ ref('src_pokeapi__pokemon_colors') }}
)

select *
from source