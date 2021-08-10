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