from flask import Flask, jsonify, request
from models import insert_genero, insert_filme, insert_usuario, insert_diretor
from models import  update_genero, update_filme, update_usuario, update_diretor
from models import delete_genero, delete_filme, delete_usuario, delete_diretor
from models import select_genero, select_filme, select_usuario, select_diretor
from validacao import valida_genero, valida_filme, valida_usuario, valida_diretor
from serializadores import genero_from_db, genero_from_web, filme_from_db, filme_from_web, usuario_from_db, usuario_from_web, diretor_from_db, diretor_from_web, nomefilme_from_web, get_genero_from_web, get_usuario_from_web

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
    filmes_db = filme_from_db(filmes)
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
     usuarios_db = usuario_from_db(usuario_db)
     return jsonify(usuarios_db)


if __name__ == "__main__":
    app.run (host="127.0.0.1", debug=True)
