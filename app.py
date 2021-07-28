#!/usr/bin/python

import sqlite3

from flask import Flask, jsonify, request, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("cadastro.html")
@app.route('/send_data', methods = ['POST'])
def send_data():
    con = sqlite3.connect('example.db')
    nome = request.form['nome']
    habilidade = request.form['habilidade']
    print(nome)
    cur = con.cursor()
    cur.execute("INSERT INTO users (nome, habilidades) VALUES (?,?)", (nome, habilidade))
    con.commit()
    cur.execute("SELECT nome, habilidades from users")
    devs = cur.fetchall()
    con.close()
    return render_template("cadastro.html", **{'devs':devs})

if __name__ == '__main__':
    app.run(debug=True)















# desenvolvedores = [
#     {
#         'nome':'Arthur',
#         'habilidades': ['Python', 'Flask']
#      },
#     {
#         'nome':'Alex',
#         'habilidades': ['Python', 'Django']}
# ]

# devolve um desenvolvedor pelo ID, também altera e deleta um desenvolvedor


















# def desenvolvedor(id):
#     if request.method == 'GET':
#         try:
#             response = desenvolvedores[id]
#         except IndexError:
#             msg = 'Desenvolvedor de ID {} não existe'.format(id)
#             response = {'status':'erro','mensagem':msg}
#         except Exception:
#             msg = 'Erro desconhecido. Procure o administrador da API'
#             response = {'status':'erro','mensagem':msg}
#         return jsonify(response)
#     elif request.method == 'PUT':
#         dados = json.loads(request.data)
#         desenvolvedores[id] = dados
#         return jsonify(dados)
#     elif request.method == "DELETE":
#         desenvolvedores.pop(id)
#         return jsonify(status = "sucesso", mensagem = "registro excluido")
#
#
# # Lista todos os desenvolvedores e permite registrar um novo desenvolvedor
# @app.route('/dev/', methods= ['POST', 'GET'])
# def list_desenvolvedores():
#     if request.method == 'POST':
#         dados = json.loads(request.data)
#         desenvolvedores.append(dados)
#         return jsonify(status="Sucesso", mensagem="Registro inserido na posição {}".format(len(desenvolvedores)-1))
#     elif request.method == 'GET':
#         return jsonify(desenvolvedores)

