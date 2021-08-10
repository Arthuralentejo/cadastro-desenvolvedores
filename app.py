import sqlite3
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/send_data', methods = ['POST'])
def send_data():
    connection = sqlite3.connect('devs.db')
    nome = request.form['nome']
    habilidade = request.form['habilidade']
    c = connection.cursor()
    c.execute("INSERT INTO devs (nome, habilidades) VALUES (?,?)", (nome, habilidade))
    connection.commit()
    return render_template("index.html")

@app.route('/show_data', methods = ['GET'])
def show_data():
    connection = sqlite3.connect('devs.db')
    c = connection.cursor()
    c.execute("SELECT nome, habilidades FROM devs")
    nomes = c.fetchall()

    connection.commit()
    return render_template("index.html", nomes = nomes)

@app.route('/del_data', methods = ['POST'])
def del_data():
    connection = sqlite3.connect('devs.db')
    c = connection.cursor()
    dev = request.form['delnome']
    c.execute("DELETE FROM devs WHERE nome = ?",(dev,))
    c.fetchall()
    connection.commit()
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)



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

