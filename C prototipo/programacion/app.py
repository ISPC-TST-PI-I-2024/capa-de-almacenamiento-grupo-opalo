from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db_uri = f"mysql://root:Contrasena09081994@127.0.0.1:3306/proyecto_ip"
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri

db = SQLAlchemy(app)

###############################################################

# Define el modelo para la tabla Paciente
class Paciente(db.Model):
    paciente_id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255))
    apellido = db.Column(db.String(255))
    fecha_nacimiento = db.Column(db.Date)
    sexo = db.Column(db.Enum('M', 'F'))
    direccion = db.Column(db.String(255))
    peso = db.Column(db.Float)
    altura = db.Column(db.Float)
    correo = db.Column(db.String(255))
    telefono = db.Column(db.String(255))

# Define el modelo para la tabla Contacto_Emergencia
class ContactoEmergencia(db.Model):
    contacto_id = db.Column(db.Integer, primary_key=True)
    paciente_id = db.Column(db.Integer, db.ForeignKey('paciente.paciente_id'))
    nombre = db.Column(db.String(255))
    apellido = db.Column(db.String(255))
    parentesco = db.Column(db.Enum('Padre', 'Madre', 'Hermano', 'Hermana', 'Otro'))
    direccion = db.Column(db.String(255))
    paciente = db.relationship('Paciente', backref='contactos')

# Define el modelo para la tabla Historial_Medico
class HistorialMedico(db.Model):
    historial_id = db.Column(db.Integer, primary_key=True)
    diagnostico = db.Column(db.Text)
    tratamiento = db.Column(db.Text)
    notas = db.Column(db.Text)
    paciente_id = db.Column(db.Integer, db.ForeignKey('paciente.paciente_id'))
    paciente = db.relationship('Paciente', backref='historiales')

# Define el modelo para la tabla Dispositivo
class Dispositivo(db.Model):
    dispositivo_id = db.Column(db.Integer, primary_key=True)
    modelo = db.Column(db.String(255))
    fecha_fabricacion = db.Column(db.DateTime)
    fecha_colocacion = db.Column(db.DateTime)
    paciente_id = db.Column(db.Integer, db.ForeignKey('paciente.paciente_id'))
    paciente = db.relationship('Paciente', backref='dispositivos')

class Medicion(db.Model):
    medicion_id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime)
    glucemia = db.Column(db.Float)
    fabricante = db.Column(db.String(255))
    dispositivo_id = db.Column(db.Integer, db.ForeignKey('dispositivo.dispositivo_id'))
    dispositivo = db.relationship('Dispositivo', backref='mediciones')

###############################################################

# Ruta para la página principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para mostrar la lista de pacientes
@app.route('/pacientes')
def listar_pacientes():
    pacientes = Paciente.query.all()
    return render_template('lista_pacientes.html', pacientes=pacientes)

# Ruta para mostrar la lista de historiales médicos
@app.route('/historiales')
def listar_historiales():
    historiales = HistorialMedico.query.all()
    return render_template('lista_historiales.html', historiales=historiales)

# Ruta para mostrar la lista de dispositivos
@app.route('/dispositivos')
def listar_dispositivos():
    dispositivos = Dispositivo.query.all()
    return render_template('lista_dispositivos.html', dispositivos=dispositivos)

# Ruta para mostrar la lista de mediciones
@app.route('/mediciones')
def listar_mediciones():
    mediciones = Medicion.query.all()
    return render_template('lista_mediciones.html', mediciones=mediciones)

###############################################################

if __name__ == '__main__':
    app.run(debug=True)
