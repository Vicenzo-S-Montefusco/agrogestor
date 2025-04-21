import oracledb

def get_connection():
    try:
        conn = oracledb.connect(
            user='RM561332', 
            password='111001', 
            dsn='oracle.fiap.com.br:1521/ORCL'
        )
        return conn
    except Exception as e:
        print("Erro ao conectar com o banco:", e)
        return None