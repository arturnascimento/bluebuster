from flask import Flask, jsonify, request
from models import insert_genero, insert_diretor, insert_filme, insert_usuario
from models import select_genero, select_diretor, select_filme, select_usuario
from models import delete_genero, delete_diretor, delete_filme, delete_usuario
from models import update_genero, update_diretor, update_filme, update_usuario
from models import get_genero, get_diretor, get_filme, get_usuario
from validacao import valida_genero, valida_diretor, valida_filme, valida_usuario
from serializadores import *
app = Flask(__name__)

#criando genero, filme, usuário e diretor
@app.route("/generos", methods=["POST"])
def add_genero():
    genero = genero_from_web(**request.json)
    if valida_genero(**genero):
        id_genero = insert_genero(**genero)
        genero_cadastrado = get_genero(id_genero)
        return genero_from_db(genero_cadastrado)
    else:
        return jsonify({"Genero inválido!!"})
@app.route("/diretores", methods=["POST"])
def add_diretor():
    diretor = diretor_from_web(**request.json)
    if valida_diretor(**diretor):
        id_diretor = insert_diretor(**diretor)
        diretor_cadastrado = get_diretor(id_diretor)
        return diretor_from_db(diretor_cadastrado)
    else:
        return jsonify({"Nome do diretor inválido!!"})
@app.route("/filmes", methods=["POST"])
def add_filme():
    filme = filme_from_web(**request.json)
    if valida_filme(**filme):
        id_filme = insert_filme(**filme)
        filme_cadastrado = get_filme(id_filme)
        return filme_from_db(filme_cadastrado)
    else:
        return jsonify({"Filme inválido!!"})
@app.route("/usuarios", methods=["POST"])
def add_usuario():
    usuario = usuario_from_web(**request.json)
    print(usuario)
    if valida_usuario(**usuario):
        # print(valida_usuario(**usuario))
        id_usuario = insert_usuario(**usuario)
        # print(id_usuario)
        usuario_cadastrado = get_usuario(id_usuario)
        # print(usuario_cadastrado)
        return usuario_from_db(usuario_cadastrado)
    else:
        return jsonify({"Usuário inválido!!"})


#buscando dados da base
@app.route("/generos", methods=["GET"])
def find_genero():
    nome_genero = nome_genero_from_web(**request.json)
    generos = select_genero(nome_genero)
    generos_from_db = [genero_from_db(genero) for genero in generos]
    return jsonify(generos_from_db)
@app.route("/usuarios", methods=["GET"])
def find_user():
    nome_completo_usuario = nome_usuario_from_web(**request.json)
    usuarios = select_usuario(nome_completo_usuario)
    usuarios_from_db = [usuario_from_db(usuario) for usuario in usuarios]
    return jsonify(usuarios_from_db)
@app.route("/diretores", methods=["GET"])
def find_diretor():
    nome_completo_diretor = nome_diretor_from_web(**request.json)
    diretores = select_diretor(nome_completo_diretor)
    diretores_from_db = [diretor_from_db(diretor) for diretor in diretores]
    return jsonify(diretores_from_db)
@app.route("/filmes", methods=["GET"])
def find_filmes():
    titulo = titulo_filme_from_web(**request.json)
    filmes = select_filme(titulo)
    filmes_from_db = [filme_from_db(filme) for filme in filmes]
    return jsonify(filmes_from_db)

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
@app.route("/usuarios/<int:id>", methods=["DELETE"])
def apagar_usuario(id):
    try:
        delete_usuario(id)
        return {"message":"Usuario deletado com sucesso"}, 204
    except:
        return jsonify({"erro":"Não foi possivel excluir este usuario"})
@app.route("/filmes/<int:id>", methods=["DELETE"])
def apagar_filme(id):
    try:
        delete_filme(id)
        return {"message":"Filme deletado com sucesso"}, 204
    except:
        return jsonify({"erro":"Não foi possivel excluir este Filme"})


# update genero, filme, usuário e diretor
@app.route("/generos/<int:id>", methods=["PATCH", "PUT"])
def alterar_genero(id):
    genero = genero_from_web(**request.json)
    if valida_genero(**genero):
        update_genero(id, **genero)
        genero_cadastrado = get_genero(id)
        return jsonify(genero_from_db(genero_cadastrado))
    else:
        return jsonify({"Genero inválido."})
@app.route("/diretores/<int:id>", methods=["PATCH", "PUT"])
def alterar_diretor(id):
    diretor = diretor_from_web(**request.json)
    if valida_diretor(**diretor):
        update_diretor(id, **diretor)
        diretor_cadastrado = get_diretor(id)
        return jsonify(diretor_from_db(diretor_cadastrado))
    else:
        return jsonify({"Nome do diretor inválido."})
@app.route("/usuarios/<int:id>", methods=["PATCH", "PUT"])
def alterar_usuario(id):
    usuario = usuario_from_web(**request.json)
    if valida_usuario(**usuario):
        update_usuario(id, **usuario)
        usuario_cadastrado = get_usuario(id)
        return jsonify(usuario_from_db(usuario_cadastrado))
    else:
        return jsonify({" Usuário inválido."})

@app.route("/filmes/<int:id>",methods=["PATCH", "PUT"])
def alterar_filme(id):
    filme = filme_from_web(**request.json)
    if valida_filme(**filme):
        update_filme(id, **filme)
        filme_cadastrado = get_filme(id)
        return jsonify(filme_from_db(filme_cadastrado))
    else:
        return jsonify({"Filme inválido."})


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)