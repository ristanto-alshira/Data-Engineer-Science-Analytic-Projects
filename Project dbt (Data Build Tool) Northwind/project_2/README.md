# learn_dbt



## How to run it?

create a virtual env of python first :
```
python3 -m venv /Users/lip13farhanpratama/venv_dskola
source /Users/lip13farhanpratama/venv_dskola/bin/activate
```
1. build the postgres image
```
docker build -t northwind -f Dockerfile.postgres .
```
2. run postgres container
if you want to check the result on local (uncomment first the EXPOSE command on dockerfile postgres)
```
docker run -d -p 5432:5432 --name postgres northwind
```
3. debug your dbt connection
```
dbt debug --profiles-dir ./ --project-dir northwind_project
```
4. run dbt model
```
dbt run --profiles-dir ./ --project-dir northwind_project
```
5. generate dbt docs
```
dbt docs generate --profiles-dir ./ --project-dir northwind_project
```
6. serve dbt docs
```
dbt docs serve --profiles-dir ./ --project-dir northwind_project
```