from dotenv import load_dotenv
import os
import oracledb

load_dotenv()

db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_service = os.getenv("DB_SERVICE")

conn = None
cursor = None

def get_connection():
    try:
        conn = oracledb.connect(
            user='RM561332', 
            password='111001', 
            dsn=f"{db_host}:{db_port}/{db_service}"
        )
        cursor = conn.cursor()
        return conn, cursor
    except Exception as e:
        print("Erro ao conectar com o banco:", e)
        return None