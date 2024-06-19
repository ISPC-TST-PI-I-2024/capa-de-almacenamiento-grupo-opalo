from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración de la conexión a la base de datos
db_uri = "mysql://root:Contrasena09081994@127.0.0.1:3306/proyecto_ip"
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Desactiva el seguimiento de modificaciones

db = SQLAlchemy(app)

# Define el modelo para la tabla Paciente
class Paciente(db.Model):
    __tablename__ = 'Paciente'
    paciente_id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255))
    apellido = db.Column(db.String(255))
    fecha_nacimiento = db.Column(db.Date)
    sexo = db.Column(db.Enum('M', 'F'))
    direccion = db.Column(db.String(255))
    peso = db.Column(db.Numeric(5, 2))
    altura = db.Column(db.Numeric(5, 2))
    correo = db.Column(db.String(255))
    telefono = db.Column(db.String(20))

# Define el modelo para la tabla Contacto_Emergencia
class ContactoEmergencia(db.Model):
    __tablename__ = 'Contacto_Emergencia'
    contacto_id = db.Column(db.Integer, primary_key=True)
    paciente_id = db.Column(db.Integer, db.ForeignKey('Paciente.paciente_id'))
    nombre = db.Column(db.String(255))
    apellido = db.Column(db.String(255))
    parentesco = db.Column(db.Enum('Padre', 'Madre', 'Hermano', 'Hermana', 'Otro'))
    direccion = db.Column(db.String(255))
    telefono = db.Column(db.String(20))
    paciente = db.relationship('Paciente', backref='contactos')

# Define el modelo para la tabla Historial_Medico
class HistorialMedico(db.Model):
    __tablename__ = 'Historial_Medico'
    historial_id = db.Column(db.Integer, primary_key=True)
    diagnostico = db.Column(db.Text)
    tratamiento = db.Column(db.Text)
    notas = db.Column(db.Text)
    paciente_id = db.Column(db.Integer, db.ForeignKey('Paciente.paciente_id'))
    paciente = db.relationship('Paciente', backref='historiales')

# Define el modelo para la tabla Dispositivo
class Dispositivo(db.Model):
    __tablename__ = 'Dispositivo'
    dispositivo_id = db.Column(db.Integer, primary_key=True)
    modelo = db.Column(db.String(255))
    fecha_fabricacion = db.Column(db.DateTime)
    fecha_colocacion = db.Column(db.DateTime)
    paciente_id = db.Column(db.Integer, db.ForeignKey('Paciente.paciente_id'))
    fabricante = db.Column(db.String(255))
    paciente = db.relationship('Paciente', backref='dispositivos')

# Define el modelo para la tabla Medicion
class Medicion(db.Model):
    __tablename__ = 'Medicion'
    medicion_id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime)
    glucemia = db.Column(db.Numeric(10, 2))
    fabricante = db.Column(db.String(255))
    dispositivo_id = db.Column(db.Integer, db.ForeignKey('Dispositivo.dispositivo_id'))
    dispositivo = db.relationship('Dispositivo', backref='mediciones')

# Rutas para la aplicación Flask
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pacientes')
def listar_pacientes():
    pacientes = Paciente.query.all()
    return render_template('lista_pacientes.html', pacientes=pacientes)

@app.route('/historiales')
def listar_historiales():
    historiales = HistorialMedico.query.all()
    return render_template('lista_historiales.html', historiales=historiales)

@app.route('/dispositivos')
def listar_dispositivos():
    dispositivos = Dispositivo.query.all()
    return render_template('lista_dispositivos.html', dispositivos=dispositivos)

@app.route('/mediciones')
def listar_mediciones():
    mediciones = Medicion.query.all()
    return render_template('lista_mediciones.html', mediciones=mediciones)

@app.route('/contactos')
def listar_contactos():
    contactos = ContactoEmergencia.query.all()
    return render_template('lista_contactos.html', contactos=contactos)

if __name__ == '__main__':
    app.run(debug=True)
