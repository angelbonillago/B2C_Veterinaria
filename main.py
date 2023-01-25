from app import create_app #importar esa fx
from flask import render_template
from app.forms import AgregarMascotaForm

app = create_app()

@app.route("/") #raiz -> localhost:500
def index():
    return render_template('index.html',content={})

@app.route('/add-mascotas')
def agregar_mascota():
    formulario = AgregarMascotaForm()
    return render_template('agregar_mascota.html',form = formulario)


if __name__ == "__main__":
    app.run(debug=True)
