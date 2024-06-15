{{ config(materialized='view') }}

with source as (
    select * from {{ source('northwind', 'orders') }}
)

select
    orderID,
    customerID,
    employeeID,
    orderDate,
    requiredDate,
    shippedDate,
    shipVia,
    freight,
    shipName,
    shipAddress,
    shipCity,
    shipRegion,
    shipPostalCode,
    shipCountry      
from source