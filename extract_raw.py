import requests as rq
import pandas as pd
import duckdb
from dotenv import load_dotenv
import os

load_dotenv()
DB_NAME = os.getenv('DB_NAME')

def main():
    base_url = 'https://pokeapi.co/api/v2/'

    response = rq.get(base_url)
    endpoints = response.json()

    conn = duckdb.connect(DB_NAME)

    for table_name, endpoint in endpoints.items():
        print(f'Fetching data for table {table_name}')
        all_data = []
        while endpoint:
            print(endpoint)
            response = rq.get(endpoint)
            data = response.json()
            data['results']

            for item in data['results']:
                item_response = rq.get(item['url'])
                item_data = item_response.json()
                all_data.append(item_data)
            
            endpoint = data['next']
        
        print(len(all_data))
        df = pd.DataFrame(all_data)

        table_name = table_name.replace('-', '_')
        conn.execute(f"CREATE TABLE IF NOT EXISTS src_{table_name} AS SELECT * FROM df")

    conn.close()


if __name__ == '__main__':
    main()