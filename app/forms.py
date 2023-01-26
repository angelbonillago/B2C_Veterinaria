from flask_wtf import FlaskForm
from wtforms import StringField,DateField,IntegerField,SubmitField
from wtforms.validators import DataRequired,Length

class AgregarMascotaForm(FlaskForm):
    
    nombre_mascota=StringField('Nombre de Mascota',validators=[DataRequired(),Length(max=50)])
    fecha_nacimiento=DateField("Fecha de nacimiento")
    raza=StringField('Raza de Mascota',validators=[DataRequired(),Length(max=50)])
    propietario=StringField('Nombre de Propietario',validators=[DataRequired(),Length(max=50)])
    dni=StringField('DNI',validators=[DataRequired(),Length(max=50)])
    boton = SubmitField("Guardar")
