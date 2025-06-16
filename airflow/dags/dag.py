# dags/simple_python_dag.py
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys


sys.path.append("/home/robert/construo/airflow")  # Update this path

from ..app.py import quick_sort

main_run = quick_sort

default_args = {
    "start_date": datetime(2025, 6, 16),
}

with DAG(
    "dag_numero_1",
    schedule_interval="@daily",
    catchup=False,
    default_args=default_args,
    description="Run a simple Python script with Airflow",
) as dag:

    run_python_app = PythonOperator(
        task_id='run_my_script',
        python_callable=main_run,
        op_args=['in_array', [12, 47, 3, 89, 25, 61, 34, 78, 56, 90, 11, 42, 67, 8, 29, 73, 5, 38, 94, 21]]  # fmt: skip
    )
