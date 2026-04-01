from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
import sys
sys.path.append("/opt/airflow/scripts")

import ingest, transform, load

with DAG(
    dag_id="openmeteo_etl",
    start_date=datetime(2025, 1, 1),
    schedule_interval="0 6 * * *",
    catchup=False,
    tags=["etl","meteo"]
):
    t1 = PythonOperator(task_id="ingest", python_callable=ingest.main)
    t2 = PythonOperator(task_id="transform", python_callable=transform.main)
    t3 = PythonOperator(task_id="load", python_callable=load.main)
    t1 >> t2 >> t3
