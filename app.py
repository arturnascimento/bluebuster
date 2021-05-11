from flask import Flask, jsonify, request
from models import insert_genero, insert_filme, insert_usuario, insert_diretor
from models import update_genero, update_filme, update_usuario, update_diretor
from models import delete_genero, delete_filme, delete_usuario, delete_diretor
from models import select_genero, select_filme, select_usuario, select_diretor, select_generoid
from validacao import valida_genero, valida_filme, valida_usuario, valida_diretor
from serializadores import *

app = Flask (__name__)


# Criando genero, filme, usuário e diretor
@app.route("/generos", methods=["POST"])
def addgenero():
    genero = genero_from_web(**request.json)
    if valida_genero(**genero):
        insert_genero(**genero)
        return jsonify(genero_from_db(genero))
    else:
        return jsonify({"Gênero inválido!!"})


@app.route("/filmes", methods=["POST"])
def addfilme():
    filme = filme_from_web(**request.json)
    if valida_filme(**filme):
        insert_filme(**filme)
        return jsonify(filme_from_db (filme))
    else:
        return jsonify({"Filme inválido!!"})


@app.route ("/usuarios", methods=["POST"])
def addusuario():
    usuario = usuario_from_web(**request.json)
    if valida_usuario(**usuario):
        insert_usuario(**usuario)
        return jsonify(usuario_from_db (usuario))
    else:
        return jsonify({"Usuário inválido!!"})

@app.route ("/diretores", methods=["POST"])
def adddiretor():
    diretor = diretor_from_web(**request.json)
    if valida_diretor(diretor):
        insert_diretor(diretor)
        return jsonify(diretor_from_db (diretor))
    else:
        return jsonify({"Nome de diretor inválido!!"})



# update genero, filme, usuário e diretor
@app.route("/generos/<int:id>", methods=["PUT", "PATCH"])
def updategenero(id):
    genero = getu_genero_from_web(**request.json)

    if valida_genero(**genero):
        update_genero(id, **genero)
        alter_genero = select_generoid(id)
        return jsonify(genero_from_db(alter_genero))
    else:
        return jsonify({"Gênero inválido!!"})









#buscando dados da base

@app.route("/generos", methods=["GET"])
def findgenero():
    genero = get_genero_from_web(**request.json)
    gen_db = select_genero(genero)
    generos_db = genero_from_db(gen_db)
    return jsonify(generos_db)

@app.route("/filmes", methods=["GET"])
def findfilme():
    titulo = nomefilme_from_web(**request.json)
    filmes = select_filme(titulo)
    filmes_db = nomefilme_from_db(filmes)
    return jsonify(filmes_db)

@app.route("/diretores", methods=["GET"])
def finddiretor():
    diretor = diretor_from_web(**request.json)
    dir_db = select_diretor(diretor)
    diretores_db = diretor_from_db(dir_db)
    return jsonify(diretores_db)

@app.route("/usuarios", methods=["GET"])
def finduser():
     usuario = get_usuario_from_web(**request.json)
     usuario_db = select_usuario(usuario[0])
     print(usuario_db)
     usuarios_db = usuario_from_db(usuario_db)
     return jsonify(usuarios_db)

#deletando genero, diretores, usuarios e filmes
# consegui executar todos os deletes by id, mas nao consegui retornar as mensagens de sucesso ou erro

@app.route("/generos/<int:id>", methods=["DELETE"])
def apagar_genero(id):
    try:
        delete_genero(id)
        return {"message":"Genero deletado com sucesso"}, 204
    except:
        return jsonify({"erro":"Não foi possivel excluir este genero"})

@app.route("/diretores/<int:id>", methods=["DELETE"])
def apagar_diretor(id):
    try:
        delete_diretor(id)
        return {"message":"Diretor deletado com sucesso"}, 204
    except:
        return jsonify({"erro":"Não foi possivel excluir este Diretor"})

@app.route("/filmes/<int:id>", methods=["DELETE"])
def apagar_filme(id):
    try:
        delete_filme(id)
        return {"message":"Filme deletado com sucesso"}, 204
    except:
        return jsonify({"erro":"Não foi possivel excluir este Filme"})

@app.route("/usuarios/<int:id>", methods=["DELETE"])
def apagar_usuario(id):
    try:
        delete_usuario(id)
        return {"message":"Usuario deletado com sucesso"}, 204
    except:
        return jsonify({"erro":"Não foi possivel excluir este usuario"})







if __name__ == "__main__":
    app.run (host="127.0.0.1", debug=True)
