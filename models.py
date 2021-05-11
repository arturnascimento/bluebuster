from funcoesbd import insert, select, update, delete, selectupdate

#insert generos, filmes, usuarios e diretores
def insert_genero(nome):
    insert("generos", ["nome"], [nome])

def insert_filme(titulo, ano, classificacao, preco, diretores_id, generos_id):
    insert("filmes",["titulo", "ano", "classificacao", "preco", "diretores_id", "generos_id"],
           [titulo, ano, classificacao, preco, diretores_id, generos_id])

def insert_usuario(nome_completo, cpf):
    insert("usuarios", ["nome_completo", "cpf"], [nome_completo, cpf])

def insert_diretor(nome_completo):
    insert("diretores", ["nome_completo"], [nome_completo])

# update generos, filmes, usuarios e diretores
def update_genero(id, nome):
    return update("generos", "id", id, ["nome"], [nome])

def select_generoid(id):
    return selectupdate("filmes", "id", id)

def update_filme(id, titulo, ano, classificacao, preco, diretores_id, generos_id):
    return update("filmes","id", id,["titulo", "ano", "classificacao", "preco", "diretores_id", "generos_id"],
           [titulo, ano, classificacao, preco, diretores_id, generos_id])

def update_usuario(id,nome_completo, cpf):
    return update("usuarios", "id", id, ["nome_completo", "cpf"], [nome_completo, cpf])

def update_diretor(id, nome_completo):
    return update("diretores", "id", id, ["nome_completo"], [nome_completo])


# delete generos, filmes, usuarios e diretores

def delete_diretor(id):
    delete("diretores", "id", id)

def delete_genero(id):
    return delete("generos", "id", id)

def delete_filme(id):
    delete("filmes", "id", id)

def delete_usuario(id):
    delete("usuarios", "id", id)

# delete generos, filmes, usuarios e diretores
def select_genero(nome):
    return select("generos","nome", nome)

def select_filme(titulo):
    from decimal import Decimal
    return select("filmes", "titulo", titulo)

def select_usuario(nome_completo):
    return select("usuarios","nome_completo", nome_completo)

def select_diretor(nome_completo):
    return select("diretores", "nome_completo", nome_completo)








