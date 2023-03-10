from app import create_app #importar esa fx
from flask import render_template,request,url_for,redirect,jsonify
from app.forms import AgregarMascotaForm,ActualizarMascotaForm
import datetime
from app.db import db
app = create_app()

@app.route("/") #raiz -> localhost:500
def index():
    #traer todas las mascotas registradas 
    #mascotas = db.mascotasC.find() #consulta a mongodb
    return render_template('index.html')


@app.route("/mascotas",methods=['GET']) #me va a cargar todas las mascotas que existan y luego en el Jquery se llama a este metodo
def mascotas():
    #traer todas las mascotas registradas 
    mascotas = db.mascotasC.find() #
    lista=[]
    for mascota in mascotas:
        diccionario={}

        diccionario['nombre']=mascota['nombre']
        diccionario['fecha_nacimiento']=mascota['fecha_nacimiento']
        diccionario['raza']=mascota['raza']
        diccionario['propietario']=mascota['propietario']
        diccionario['dni']=mascota['dni']
        lista.append(diccionario)

    return jsonify({"mascotas":lista})




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
        #return render_template('index.html',mascotas = {}) #ver que funcion remplaza a ese render_template y me llame a la fx index()
        return redirect(url_for('index'))

    #GET -> LE MANDAMOS EL FORMULARIO VACIO
    
    return render_template('agregar_mascota.html',form = formulario)


@app.route('/ver-mascota/<string:nombre>',methods=['GET'])
def ver_mascota(nombre):
    #consultar la informacion de la mascota y mostrarlo en un perfil
    
    mascota_seleccionada= db.mascotasC.find({'nombre':nombre})
    return render_template('ver_mascota.html',mascota = mascota_seleccionada)


@app.route('/actualizar-mascota/<string:nombre>',methods=['GET','POST'])
def actualizar_mascota(nombre):
    #consultar la informacion de la mascota y mostrarlo en un perfil
    #creamos el formulario
    formulario = ActualizarMascotaForm()
    
    if request.method=='POST' and formulario.validate_on_submit() :
        #post
        print('llege aqui!')
        #return (redirect(url_for('ver_mascota', nombre =str(nombre))))

    
    return render_template('actualizar_mascota.html',form = formulario)


if __name__ == "__main__":
    app.run(debug=True)
