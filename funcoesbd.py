from mysql.connector import connect

CONFIGURACOES_BD = {
    "host":"localhost",
    "user":"root",
    "password":"root",
    "database":"locadora"
}
def execute(sql, params=None):
    with connect(**CONFIGURACOES_BD) as conn: # conecta no banco
        with conn.cursor() as cursor: # abre uma página para executar coisas
            cursor.execute(sql, params) # executa o sql que está sendo passado por parametro
            conn.commit() # grava as coisas no banco de dados
            return cursor.lastrowid
def query(sql, params=None):
    with connect(**CONFIGURACOES_BD) as conn: # conecta no banco
        with conn.cursor(dictionary=True) as cursor: # abre uma página para executar coisas
            cursor.execute(sql, params) # executa o sql que está sendo passado por parametro
            return cursor.fetchall() # pega o resultado da consulta e retorna

# POST
def insert(tabela, coluna, valores):
    return execute(f"INSERT INTO {tabela} ({', '.join(coluna)}) VALUES ({', '.join(['%s' for valor in valores])})", valores)
#DELETE
def delete(tabela, coluna, valor):
    execute(f"""delete from  {tabela} WHERE {coluna} = %s""", (valor,))
#PUT / PATCH
def update(tabela, chave, valor_chave, colunas, valores):
    sets = [f"{coluna} = %s" for coluna in colunas]
    execute(f"""UPDATE {tabela} SET {",".join(sets)} WHERE {chave} = %s""", valores + [valor_chave])
#GETS
def select(tabela, chave, valor_chave):
    return query(f'''select * from {tabela} where {chave} = %s''', (valor_chave,))
def select2(tabela, chave = 1,valor_chave = 1, limit = 100, offset =0):
    return query(f"""SELECT * FROM {tabela} WHERE {chave} = %s LIMIT {limit} offset {offset}""", (valor_chave,))