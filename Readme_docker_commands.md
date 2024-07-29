
# Run main.py in container:
    docker exec -it 33b4c3b33288 python src_py/main.py --dbt_command "dbt deps"
    docker exec -it 9f482ad6193d python src_py/main.py --dbt_command "dbt run" --load_raw "y"

# Run all DBT commands: dbt deps, dbt run, dbt test
    docker exec -it 9f482ad6193d python src_py/main.py