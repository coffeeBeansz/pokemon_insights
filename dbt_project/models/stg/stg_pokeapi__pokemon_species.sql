-- models/stg/stg_pokeapi__pokemon_species.sql

with source as (
    select name, color
    from {{ ref('src_pokeapi__pokemon_species') }}
),
unnest_color as (
    select
        name as species_name,
        json_extract(color, '$.name') as color_name,
        json_extract(color, '$.url') as color_url,
    from source
),
cast_dtypes as (
    select
        species_name::VARCHAR as species_name,
        color_name::VARCHAR as color_name,
        color_url::VARCHAR as color_url
    from unnest_color
),
removed_quotes as ( -- Remove quotes from the json extaction
    select
        species_name,
        REPLACE(color_name, '"', '') as color_name,
        REPLACE(color_url, '"', '') as color_url
    from cast_dtypes
)

select *
from removed_quotes


-- old but gold
-- unnest_varieties as (
--     select
--         color_name,
--         color_url,
--         json_extract(v.value, '$.is_default') as is_default,
--         json_extract(v.value, '$.pokemon.name') as pokemon_name,
--         json_extract(v.value, '$.pokemon.url') as pokemon_url
--     from unnest_color, unnest(varieties) as v(value)
-- ),
-- final as (
--     select
--         color_name::VARCHAR as color_name,
--         color_url::VARCHAR as color_url,
--         is_default::BOOLEAN as is_default,
--         pokemon_name::VARCHAR as pokemon_name,
--         pokemon_url::VARCHAR as pokemon_url
--     from unnest_varieties
-- )