{{ config(materialized='view') }}

with source as (
    select * from {{ source('northwind', 'categories') }}
)

select
    categoryID,
    categoryName,
    description,
    picture    
from source
