{{ config(materialized='view') }}

with source as (
    select * from {{ source('northwind', 'employees') }}
)

select
    employeeID,
    lastName,
    firstName,
    title,
    titleOfCourtesy,
    birthDate,
    hireDate,
    address,
    city,
    region,
    postalCode,
    country,
    homePhone,
    extension,
    photo,
    notes,
    reportsTo,
    photoPath       
from source
