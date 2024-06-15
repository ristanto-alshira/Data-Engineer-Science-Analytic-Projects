{{ config(materialized='view') }}

with source as (
    select * from {{ source('northwind', 'order_details') }}
)

select
    orderID,
    productID,
    unitPrice,
    quantity,
    discount       
from source
