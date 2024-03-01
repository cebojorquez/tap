from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')

def base():
    return render_template('base.html')

@app.route('/', methods=['POST'])
def index():
    nombre = request.form['name']
    return render_template('inicio.html', nombre=nombre)

@app.route('/Datos')
def datos():
    return render_template('datos.html')

@app.route('/Habilidades')
def habilidades():
    return render_template('habilidades.html')

app.run(debug=True)