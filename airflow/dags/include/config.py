import os
from urllib.parse import quote_plus
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'), override=True)

DB_USER = os.getenv('DB_USER')
DB_PASS = quote_plus(os.getenv('DB_PASS'))
DB_HOST = os.getenv('DB_HOST')
DB_PORT = 5432
DB_NAME ="postgres"

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}" # noqa E501
DATA_SOURCE = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTIBPRSnUp10oHj5fhnUTlUJn-W7DtjSRtXIhySqW_1nZak5u4b7bPc9gTcWPHM22JL0aZJJa5QakM1/pub?gid=0&single=true&output=csv" # noqa E501
DATA_PATH = "/opt/airflow/dags/include/data"
