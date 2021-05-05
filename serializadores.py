#generos
def genero_from_web(**kwargs):
    return {
        "nome": kwargs["nome"] if kwargs["nome"] else ""
    }
def genero_from_db(*args):
    return {
        "nome": args[0]
    }


#filmes
def filme_from_web(**kwargs):
    return {
        "titulo": kwargs["titulo"] if kwargs["titulo"] else "",
        "ano": kwargs["ano"] if kwargs["ano"] else "",
        "classificacao": kwargs["classificacao"] if kwargs["classificacao"] else "",
        "preco": kwargs["preco"] if kwargs["preco"] else "",
        "diretores_id": kwargs["diretores_id"] if kwargs["diretores_id"] else "",
        "generos_id": kwargs["generos_id"] if kwargs["generos_id"] else ""
    }
def filme_from_db(*args):
    return {
        "titulo": args[0],
        "ano": args[0],
        "classificacao": args[0],
        "preco": args[0],
        "diretores_id": args[0],
        "generos_id": args[0]
    }


#usuarios
def usuario_from_web(**kwargs):
    return {
        "nome_completo": kwargs["nome_completo"] if kwargs["nome_completo"] else "",
        "cpf": kwargs["cpf"] if kwargs["cpf"] else ""
    }
def usuario_from_db(*args):
    return {
        "nome_completo": args[0],
        "cpf": args[0]
    }


#diretores
def diretor_from_web(**kwargs):
    return {
        "nome_completo": kwargs["nome_completo"] if kwargs["nome_completo"] else ""
    }
def diretor_from_db(*args):
    return {
        "nome_completo": args[0]

    }