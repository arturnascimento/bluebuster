#generos
def genero_from_web(**kwargs):
    return{
       "nome": kwargs["nome"] if "nome" in kwargs else ""
    }
def nome_genero_from_web(**kwargs):
    return kwargs["nome"] if "nome" in kwargs else ""
def genero_from_db(args):
    return {
        "id": args["id"],
        "nome": args["nome"],
    }
#filmes
def filme_from_web(**kwargs):
    return {
        "titulo": kwargs["titulo"] if "titulo" in kwargs else "",
        "ano": kwargs["ano"] if "ano" in kwargs else "",
        "classificacao": kwargs["classificacao"] if "classificacao" in kwargs else "",
        "preco": kwargs["preco"] if "preco" in kwargs else "",
        "diretores_id": kwargs["diretores_id"] if "diretores_id" in kwargs else "",
        "generos_id": kwargs["generos_id"] if "generos_id" in kwargs else "",
    }
def filme_from_db(args):
    return{
        "id": args["id"],
        "titulo": args["titulo"],
        "ano": args["ano"],
        "classificacao": args["classificacao"],
        "preco": str(args["preco"]),
        "diretores_id": args["diretores_id"],
        "generos_id": args["generos_id"],
    }
def titulo_filme_from_web(**kwargs):
    return kwargs["titulo"] if "titulo" in kwargs else ""

#usuarios
def usuario_from_web(**kwargs):
    return {
        "nome_completo": kwargs["nome_completo"] if "nome_completo" in kwargs else "",
        "CPF": kwargs["CPF"] if "CPF" in kwargs else ""
    }
def usuario_from_db(args):
    return {
        "id": args["id"],
        "nome_completo": args["nome_completo"],
        "CPF": args["CPF"],
    }
def nome_usuario_from_web(**kwargs):
    return kwargs["nome_completo"] if "nome_completo" in kwargs else ""

#diretores
def diretor_from_web(**kwargs):
    return {
        "nome_completo": kwargs["nome_completo"] if "nome_completo" in kwargs else ""
    }
def diretor_from_db(args):
    return {
        "id": args["id"],
        "nome_completo": args["nome_completo"],
            }
def nome_diretor_from_web(**kwargs):
    return kwargs["nome_completo"] if "nome_completo" in kwargs else ""







