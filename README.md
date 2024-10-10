# Pokèmon insights
Graduate project 2 - Data driven

1. Clone repository:
```bash
git clone https://github.com/coffeeBeansz/pokemon_insights.git
```

2. Install requirements:
```bash
pip install -r requirements.txt
```

3. Put a file named profiles.yml in the folder ~/.dbt/ conatining the following:
```bash
dbt_project:
  outputs:
    dev:
      type: duckdb
      path: <path_to_repo>/pokeapi_database.duckdb
      threads: 1

    prod:
      type: duckdb
      path: <path_to_repo>/pokeapi_database.duckdb
      threads: 4

  target: dev
  ```
  where <path_to_repo> should be replaced by the path to the github repo on your computer.

4. To fetch raw data from pokeapi, cd to repo and run:
```bash
python3 extract_raw.py
```

5. To prepare the data, cd to the dbt_project folder and run:
```bash
dbt run
```

6. To create the insights, cd to repo and run:
```bash
python3 main.py
```