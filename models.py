from main import insert, select, update, delete

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
    update("generos", "id", id, ["nome"], [nome])

def update_filme(id, titulo, ano, classificacao, preco, diretores_id, generos_id):
    update("filmes","id", id,["titulo", "ano", "classificacao", "preco", "diretores_id", "generos_id"],
           [titulo, ano, classificacao, preco, diretores_id, generos_id])

def update_usuario(id,nome_completo, cpf):
    update("usuarios", "id", id, ["nome_completo", "cpf"], [nome_completo, cpf])

def update_diretor(id, nome_completo):
    update("diretores", "id", id, ["nome_completo"], [nome_completo])


# delete generos, filmes, usuarios e diretores
def delete_genero(id, nome):
    delete("generos", "id", id)

def delete_filme(id, titulo, ano, classificacao, preco, diretores_id, generos_id):
    delete("filmes","id", id)

def delete_usuario(id,nome_completo, cpf):
    delete("usuarios", "id", id)

def delete_diretor(id, nome_completo):
    delete("diretores", "id", id)

# delete generos, filmes, usuarios e diretores
def select_genero(nome):
    select("generos","nome", nome)

def select_filme(titulo, ano, classificacao, preco, diretores_id, generos_id):
    select("filmes", "titulo", titulo, "ano", ano, "classificacao", classificacao, "preco", preco, "diretores_id", diretores_id, "generos_id", generos_id)

def select_usuario(nome_completo, cpf):
    select("usuarios","nome_completo", nome_completo, "cpf", cpf)

def select_diretor(nome_completo):
    select("diretores", "nome_completo", nome_completo)








