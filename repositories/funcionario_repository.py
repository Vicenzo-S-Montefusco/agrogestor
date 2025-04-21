from db import get_connection
import oracledb

conn = get_connection()
cursor = conn.cursor()

def post_funcionario(nome, funcao):
    try:
        script = """INSERT INTO funcionarios (nome, funcao) VALUES (:nome, :funcao)"""
        
        cursor.execute(script, {'nome': nome, 'funcao': funcao})
        conn.commit()

    except oracledb.DatabaseError as e:
        print("Erro na transação do BD:", e)
        conn.rollback()

def get_funcionario_por_id(id):
    try:
        script = """SELECT * FROM funcionarios WHERE id = :id"""
        
        cursor.execute(script, {'id': id})
        resultado = cursor.fetchall()

        return resultado

    except oracledb.DatabaseError as e:
        print("Erro na consulta por id:", e)
        return None

def get_funcionario_por_nome(nome):
    try:
        script = """SELECT * FROM funcionarios WHERE nome = :nome"""
        
        cursor.execute(script, {'nome': nome})
        resultado = cursor.fetchall()
        
        return resultado

    except oracledb.DatabaseError as e:
        print("Erro na consulta por nome:", e)
        return None
    
def get_funcionarios_por_funcao(funcao):
    try:
        script = """SELECT * FROM funcionarios WHERE funcao = :funcao"""
        
        cursor.execute(script, {'funcao': funcao})
        resultado = cursor.fetchall()
        
        return resultado

    except oracledb.DatabaseError as e:
        print("Erro na consulta por funcao:", e)
        return None
    
def update_funcionario(id_funcionario, campo, novo_valor):
    try:
        if campo.lower() not in ['nome', 'funcao']:
            print("Campo inválido. Só é permitido atualizar 'nome' ou 'funcao'.")
            return

        script = f"""UPDATE funcionarios SET {campo} = :valor WHERE id = :id"""
        
        cursor.execute(script, {'valor': novo_valor, 'id': id_funcionario})
        conn.commit()

        if cursor.rowcount > 0:
            print(f"{campo.capitalize()} atualizado com sucesso!")
        else:
            print("Nenhum funcionário encontrado com o ID informado.")

    except oracledb.DatabaseError as e:
        print("Erro ao atualizar funcionário:", e)
        conn.rollback()

def delete_funcionario(campo, valor):
    try:
        if campo.lower() not in ['id', 'nome', 'funcao']:
            print("Campo inválido. Use apenas 'id', 'nome' ou 'funcao'.")
            return

        script = f"""DELETE FROM funcionarios WHERE {campo} = :valor"""

        cursor.execute(script, {'valor': valor})
        conn.commit()

        if cursor.rowcount > 0:
            print(f"Funcionário(s) com {campo} = '{valor}' deletado(s) com sucesso!")
        else:
            print(f"Nenhum funcionário encontrado com {campo} = '{valor}'.")

    except oracledb.DatabaseError as e:
        print("Erro ao deletar funcionário:", e)
        conn.rollback()