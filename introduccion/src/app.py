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

app.run(debug=True) #es para correr la aplicación o sea nuestro sitio web en el servidor virtual
    
    
    #recuerda que para verlo solo debemos entrar a la dirección 127.0.0.1:5000 en cualquier navegador
    #es importante crear la carpeta templates porque ahi va flask a intentar buscar el archivo de la plantilla.