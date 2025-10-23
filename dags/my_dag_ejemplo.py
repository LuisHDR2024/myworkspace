from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import requests

# ----------------------------------------------------------------------
# Definir las funciones de las tareas
# ----------------------------------------------------------------------

def print_welcome():
    print('Welcome to Airflow!')

def print_date():
    print('Today is {}'.format(datetime.today().date()))

def print_random_quote():
    url = 'https://zenquotes.io/api/random'

    response = requests.get(url)
    response.raise_for_status()
    data = response.json()   # Esto es una lista
    quote = data[0]['q']     # Accedemos al primer elemento de la lista
    author = data[0]['a']
    print(f'Quote of the day: "{quote}" — {author}')


# ----------------------------------------------------------------------
# Definir el DAG
# ----------------------------------------------------------------------

dag = DAG(
    'Dag_LuisDominguez',
    default_args = {'start_date': datetime.now() - timedelta(days=1)},  # reemplazo de days_ago(1)
    schedule     = timedelta(minutes=4),  # antes schedule_interval
    catchup      = False
)

# ----------------------------------------------------------------------
# Definir las instancias de tareas
# ----------------------------------------------------------------------

print_welcome_task = PythonOperator(
    task_id='print_welcome',
    python_callable=print_welcome,
    dag=dag
)

print_date_task = PythonOperator(
    task_id='print_date',
    python_callable=print_date,
    dag=dag
)

print_random_quote_task = PythonOperator(
    task_id='print_random_quote',
    python_callable=print_random_quote,
    dag=dag
)

# ----------------------------------------------------------------------
# Definir la secuencia de tareas
# ----------------------------------------------------------------------

print_welcome_task >> print_date_task >> print_random_quote_task
