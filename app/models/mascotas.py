
class Mascota():
#personajes= db.personaje.find().sort('name',-1)
    def __init__(self,nombre_mascota,fecha_nacimiento,raza,propietario,dni) :
        
        self.nombre_mascota=nombre_mascota
        self.fecha_nacimiento=fecha_nacimiento
        self.raza=raza
        self.propietario=propietario
        self.dni=dni