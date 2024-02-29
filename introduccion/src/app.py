from flask import Flask, render_template #Es para importar flask

app = Flask(__name__) #creamos una instancia de flask en una variable llamada app(se puede llamar como sea)

@app.route('/')#usamos un decorador(@) para crear una respuesta a la ruta / que es el index o página principal

def index():
    return render_template('index.html')

@app.route('/saludo/<name>')
def saludo(name):
    return render_template('saludo.html',nombre=name)

@app.route('/saludo1/<name1>/<edad>')
def saludo1(name1,edad):
    return render_template('saludo1.html',nombre=name1,edad=edad)
app.run(debug=True) #es para correr la aplicación o sea nuestro sitio web en el servidor virtual
    
    
    #recuerda que para verlo solo debemos entrar a la dirección 127.0.0.1:5000 en cualquier navegador
    #es importante crear la carpeta templates porque ahi va flask a intentar buscar el archivo de la plantilla.