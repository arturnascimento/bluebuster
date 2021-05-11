from mysql.connector import connect

CONFIGURACOES_BD = {
    "host":"localhost",
    "user":"root",
    "password":"root",
    "database":"locadora"
}
def execute(sql, params=None):
    """ Executa um comando no mysql e salva os valores
        Serve para: insert, update, delete, create, alter, drop
    """
    with connect(**CONFIGURACOES_BD) as conn: # conecta no banco
        with conn.cursor() as cursor: # abre uma página para executar coisas
            cursor.execute(sql, params) # executa o sql que está sendo passado por parametro
            conn.commit() # grava as coisas no banco de dados


def query(sql, params=None):
    """ Executa um comando no mysql e retorna o resultado
        Serve para: Select, SHOW """
    with connect(**CONFIGURACOES_BD) as conn: #conecta no banco
        with conn.cursor(dictionary=True) as cursor: # abre uma página para executar coisas
            cursor.execute(sql, params) # executa o sql que está sendo passado por parametro
            return cursor.fetchall() # pega o resultado da consulta e retorna


def insert(tabela, colunas, valores):
    execute(f"INSERT INTO {tabela} ({','.join(colunas)}) VALUES ({','.join(['%s' for valor in valores])})", valores)


def delete(tabela, coluna, valor):
    execute(f"DELETE FROM {tabela} WHERE {coluna} = %s", (valor,))


def update(tabela, chave, valor_chave, colunas, valores):
    sets = [f"{coluna} = %s" for coluna in colunas]
    execute(f"""UPDATE {tabela} SET {",".join(sets)} WHERE {chave} = %s""", valores + [valor_chave])

def select(tabela, chave, valor_chave):
    return query(f"select * from {tabela} where {chave} = '{valor_chave}'")
    # return query(f"select * from {tabela} where {chave} = 'r' or '' = ''")
