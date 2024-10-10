-- models/stg/stg_pokeapi__pokemons.sql

with source as (
    select name, species, types
    from {{ ref('src_pokeapi__pokemons') }}
),
unnested_species as ( -- First unnest the species, which is unique for each pokemon (not adding more rows)
    select
        name as pokemon_name,
        json_extract(species, '$.name') as species_name,
        json_extract(species, '$.url') as species_url,
        types
    from source
),
unnested_types as ( -- The unnest the types, which is not unique for each pokemon (adding more rows)
    select
        pokemon_name,
        species_name,
        species_url,
        json_extract(t.value, '$.slot') as slot,
        json_extract(t.value, '$.type.name') as type_name,
        json_extract(t.value, '$.type.url') as type_url
    from unnested_species, unnest(types) as t(value)
),
cast_dtypes as ( -- Make sure the dtypes are correct
    select
        pokemon_name::VARCHAR as pokemon_name,
        species_name::VARCHAR as species_name,
        species_url::VARCHAR as species_url,
        slot::INT as slot,
        type_name::VARCHAR as type_name,
        type_url::VARCHAR as type_url
    from unnested_types
),
removed_quotes as ( -- Remove quotes from the json extaction
    select
        pokemon_name,
        REPLACE(species_name, '"', '') as species_name,
        REPLACE(species_url, '"', '') as species_url,
        slot,
        REPLACE(type_name, '"', '') as type_name,
        REPLACE(type_url, '"', '') as type_url
    from cast_dtypes
)


select *
from removed_quotes