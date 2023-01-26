from app import create_app #importar esa fx
from flask import render_template,request
from app.forms import AgregarMascotaForm
import datetime
from app.db import db
app = create_app()

@app.route("/") #raiz -> localhost:500
def index():
    #traer todas las mascotas registradas 
    mascotas = db.mascotasC.find() #consulta a mongodb
    #print('mascotas -> ',mascotas)
    return render_template('index.html',mascotas=mascotas)

@app.route('/add-mascotas',methods=['POST','GET'])
def agregar_mascota():

    formulario = AgregarMascotaForm()
    if request.method=='POST' and formulario.validate_on_submit() : #get
        #RECIBIR LA INFO DE ESE FORMULARIO - INSERTARLO EN MONGODB
        print('data -> ',formulario)
        nombre_mascota= formulario.nombre_mascota.data
        fecha_nacimiento= formulario.fecha_nacimiento.data
        time = datetime.datetime.min.time()

        final_fechaNacimiento = datetime.datetime.combine(fecha_nacimiento, time)


        raza= formulario.raza.data
        propietario= formulario.propietario.data
        dni= formulario.dni.data

        db.mascotasC.insert_one({ #Insertando a MONGODB
            'nombre': nombre_mascota, 
            'fecha_nacimiento': final_fechaNacimiento, 
            'raza': raza, 
            'propietario': propietario, 
            'dni': dni
            })
        return render_template('index.html',mascotas = {}) #ver que funcion remplaza a ese render_template y me llame a la fx index()

    #GET -> LE MANDAMOS EL FORMULARIO VACIO
    
    return render_template('agregar_mascota.html',form = formulario)




if __name__ == "__main__":
    app.run(debug=True)
