{{ config(materialized='view') }}

with source as (
    select * from {{ source('northwind', 'suppliers') }}
)

select
    supplierID,
    companyName,
    contactName,
    contactTitle,
    address,
    city,
    region,
    postalCode,
    country,
    phone,
    fax,
    homePage    
from source