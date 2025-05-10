import pandas as pd
import sqlite3

def extract():
    # Ejemplo: Extraer datos de un CSV
    data = pd.read_csv('https://example.com/sample_data.csv')
    data.to_csv('/tmp/raw_data.csv', index=False)
    print("Datos extraídos")

def transform():
    # Ejemplo: Transformar datos
    data = pd.read_csv('/tmp/raw_data.csv')
    data['new_column'] = data['some_column'].apply(lambda x: x * 2)
    data.to_csv('/tmp/transformed_data.csv', index=False)
    print("Datos transformados")

def load():
    # Ejemplo: Cargar datos en SQLite
    conn = sqlite3.connect('/tmp/database.db')
    data = pd.read_csv('/tmp/transformed_data.csv')
    data.to_sql('processed_data', conn, if_exists='replace', index=False)
    conn.close()
    print("Datos cargados")
