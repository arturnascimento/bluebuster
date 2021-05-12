from funcoesbd import insert, select, update, delete, select2

#insert generos, filmes, usuarios e diretores
def insert_genero(nome):
    return insert("generos", ["nome",], [nome,])
def insert_filme(titulo, ano, classificacao, preco, diretores_id, generos_id):
    return insert("filmes", ["titulo", "ano", "classificacao", "preco", "diretores_id", "generos_id"],
                  [titulo, ano, classificacao, preco, diretores_id, generos_id])
def insert_diretor(nome_completo):
    return insert("diretores", ["nome_completo",], [nome_completo,])
def insert_usuario(nome_completo, CPF):
    return insert("usuarios", ["nome_completo", "CPF"], [nome_completo, CPF])

# update generos, filmes, usuarios e diretores
def update_genero(id_genero, nome):
    update("generos", "id", id_genero, ["nome",],[nome,])
def update_filme(id, titulo, ano, classificacao, preco, diretores_id, generos_id):
    update("filmes", "id", id, ["titulo", "ano", "classificacao", "preco", "diretores_id", "generos_id"],
           [titulo, ano, classificacao, preco, diretores_id, generos_id])
def update_usuario(id_usuario, nome_completo, CPF):
    update("usuarios", "id", id_usuario, ["nome_completo", "CPF"], [nome_completo, CPF])
def update_diretor(id_diretor, nome_completo):
        update ("diretores", "id", id_diretor, ["nome_completo", ], [nome_completo, ])

# delete generos, filmes, usuarios e diretores
def delete_genero(id):
    delete("generos", "id", id)
def delete_filme(id):
    delete("filmes", "id", id)
def delete_usuario(id):
    delete("usuarios", "id", id)
def delete_diretor(id):
    delete("diretores", "id", id)

#select generos, filmes, usuarios e diretores
def get_usuario(id_usuario):
    return select2("usuarios", "id", id_usuario)[0]
def select_usuario(nome_completo):
    return select("usuarios", "nome_completo", nome_completo)
def get_diretor(id_diretor):
    return select2("diretores", "id", id_diretor)[0]
def select_diretor(nome_completo):
    return select("diretores", "nome_completo", nome_completo)
def get_genero(id_genero):
    return select2("generos", "id", id_genero)[0]
def select_genero(nome):
    return select("generos", "nome", nome)
def get_filme(id_filme):
    return select2("filmes", "id", id_filme)[0]
def select_filme(titulo):
    return select("filmes", "titulo", titulo)






