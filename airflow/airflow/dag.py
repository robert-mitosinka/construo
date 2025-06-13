from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from my_script import create_test_data

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 6, 12),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'product_data_generator',
    default_args=default_args,
    schedule_interval='@hourly',
    catchup=False
)

task = PythonOperator(
    task_id='generate_test_data',
    python_callable=create_test_data,
    dag=dag
)
