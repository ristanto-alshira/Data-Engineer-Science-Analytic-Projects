{{ config(materialized='view') }}

with source as (
    select * from {{ source('northwind', 'products') }}
)

select
    productID,
    productName,
    supplierID,
    categoryID,
    quantityPerUnit,
    unitPrice,
    unitsInStock,
    unitsOnOrder,
    reorderLevel,
    discontinued     
from source