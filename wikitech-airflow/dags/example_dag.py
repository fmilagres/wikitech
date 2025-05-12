from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import requests

def fetch_data():
    url = "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/Main_Page/daily/20240101/20240107"
    response = requests.get(url)
    with open("/opt/airflow/dags/data/wikipedia_sample.json", "w") as f:
        f.write(response.text)

with DAG("wikipedia_fetch_dag", start_date=datetime(2023, 1, 1), schedule_interval="@daily", catchup=False) as dag:
    task = PythonOperator(
        task_id="fetch_wikipedia_data",
        python_callable=fetch_data
    )
