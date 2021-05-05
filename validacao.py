
#validacao do tabela gênero.
def valida_genero(nome):
    if len(nome) == 0:
        return False
    else:
        return True

#validacao tabela filmes

def valida_filme(titulo, ano, classificacao, preco, diretores_id, generos_id):
    if len(titulo) == 0:
        return False
    elif ano == 0:
        return False
    elif int(classificacao) < 0 or int(classificacao) > 18:
        return False
    elif preco == 0:
        return False
    elif diretores_id == 0:
        return False
    elif generos_id == 0:
        return False
    else:
        return True

#validação tabela usuários
def valida_usuario(nome_completo, cpf):
    if len(nome_completo) == 0:
        return False
    elif len(cpf) != 14:
        return False
    else:
        return True

#validação tabela diretores
def valida_diretor(nome_completo):
    if len(nome_completo) == 0:
        return False
    else:
        return True


