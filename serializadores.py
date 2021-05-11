#generos
def genero_from_web(**kwargs):
    return {"nome": kwargs["nome"] if "nome" in kwargs else ""}

def genero_from_db(*args):
    return {
        "genero":  args[0]
    }

def get_genero_from_web(**kwargs):
    return kwargs["nome"] if "nome" in kwargs else ""


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

def filme_from_db(*args):
    return {
        "Filme": args[0]
    }

def nomefilme_from_web(**kwargs):
    return kwargs["titulo"] if "titulo" in kwargs else ""


#usuarios
def usuario_from_web(**kwargs):
    return {
        "nome_completo": kwargs["nome_completo"] if "nome_completo" in kwargs else "",
        "cpf": kwargs["cpf"] if "cpf" in kwargs else ""
    }
def usuario_from_db(*args):
    return {
    "usuario": args[0]
    }
def get_usuario_from_web(**kwargs):
    return kwargs["nome_completo"] if "nome_completo" in kwargs else "", kwargs["cpf"] if "cpf" in kwargs else ""

#diretores
def diretor_from_web(**kwargs):
    return kwargs["nome_completo"] if "nome_completo" in kwargs else ""

def diretor_from_db(*args):
    return {
        "nome diretor":  args[0]
    }



