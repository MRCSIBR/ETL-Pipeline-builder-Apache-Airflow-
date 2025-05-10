from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from scripts.transform_data import extract, transform, load

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

with DAG(
    'etl_pipeline',
    default_args=default_args,
    description='Pipeline ETL básico',
    schedule_interval='@daily',
    start_date=datetime(2025, 5, 1),
    catchup=False,
) as dag:
    
    extract_task = PythonOperator(
        task_id='extract',
        python_callable=extract,
    )

    transform_task = PythonOperator(
        task_id='transform',
        python_callable=transform,
    )

    load_task = PythonOperator(
        task_id='load',
        python_callable=load,
    )

    extract_task >> transform_task >> load_task
