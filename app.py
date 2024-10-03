from flask import Flask, render_template, request, redirect

lista = []

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("Home.html", Titulo="Bem-vindo ao site de Pokemon")

@app.route('/pokemon')
def pokemon():
    return render_template("Pokemon.html", Banana="Melhores Pokemons")

@app.route('/sobre')
def sobre():
    return render_template("Sobre.html", Banana2="Sobre o nosso site")

@app.route('/cadastro')
def cadastro():
    return render_template("Cadastro.html", Titulo="Cadastro de Pokemon")

@app.route('/exibir')
def exibir():
    return render_template("Exibir.html", Titulo="Pokemons Cadastrados", lista=lista)

@app.route('/criar', methods=['POST'])
def criar():
    numero = request.form['numero']  # Corrigido 'Nuemro' para 'numero'
    nome = request.form['nome']
    tipo = request.form['tipo']
    altura = request.form['altura']
    peso = request.form['peso']
    pokemon = [numero, nome, tipo, altura, peso]
    lista.append(pokemon)
    return redirect("/exibir")

if __name__ == '__main__':
    app.run()
