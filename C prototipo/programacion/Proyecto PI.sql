CREATE DATABASE IF NOT EXISTS PROYECTO_IP;
USE PROYECTO_IP;

CREATE TABLE IF NOT EXISTS Paciente (
    paciente_id INT PRIMARY KEY,
    nombre VARCHAR(255),
    apellido VARCHAR(255),
    fecha_nacimiento DATE,
    sexo ENUM('M','F'),
    direccion VARCHAR(255),
    peso DECIMAL,
    altura DECIMAL,
    correo VARCHAR(255),
    telefono VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS Contacto_Emergencia (
    contacto_id INT PRIMARY KEY,
    paciente_id INT,
    nombre VARCHAR(255),
    apellido VARCHAR(255),
    parentesco ENUM('Padre','Madre','Hermano','Hermana','Otro'),
    direccion VARCHAR(255),
    FOREIGN KEY (paciente_id) REFERENCES Paciente(paciente_id)
);

CREATE TABLE IF NOT EXISTS Historial_Medico (
    historial_id INT PRIMARY KEY,
    diagnostico TEXT,
    tratamiento TEXT,
    notas TEXT,
    paciente_id INT,
    FOREIGN KEY (paciente_id) REFERENCES Paciente(paciente_id)
);

CREATE TABLE IF NOT EXISTS Dispositivo (
    dispositivo_id INT PRIMARY KEY, 
    modelo VARCHAR(255), 
    fecha_fabricacion DATETIME, 
    fecha_colocacion DATETIME, 
    paciente_id INT, 
    FOREIGN KEY (paciente_id) REFERENCES Paciente(paciente_id)
);

CREATE TABLE IF NOT EXISTS Medicion (
    medicion_id INT PRIMARY KEY,
    fecha DATETIME,
    glucemia DECIMAL(10, 2),
    fabricante VARCHAR(255),
    dispositivo_id INT,
    FOREIGN KEY (dispositivo_id) REFERENCES Dispositivo(dispositivo_id)
);


INSERT INTO Paciente (paciente_id, nombre, apellido, fecha_nacimiento, sexo, direccion, peso, altura, correo, telefono)
VALUES
    (1, 'Juan', 'Pérez', '1990-05-15', 'M', 'Calle Principal 123', 70.5, 1.75, 'juan@example.com', '+54 9 351 1234567'),
    (2, 'María', 'Rodríguez', '1985-08-20', 'F', 'Avenida Central 456', 60.2, 1.60, 'maria@example.com', '+54 9 351 9876543');

INSERT INTO Contacto_Emergencia (contacto_id, paciente_id, nombre, apellido, parentesco, direccion)
VALUES
    (1, 1, 'Ana', 'Pérez', 'Madre', 'Calle Principal 123'),
    (2, 2, 'Carlos', 'Rodríguez', 'Padre', 'Avenida Central 456');

INSERT INTO Historial_Medico (historial_id, diagnostico, tratamiento, notas, paciente_id)
VALUES
    (1, 'Hipertensión', 'Medicación y dieta', 'Controlar la presión arterial regularmente', 1),
    (2, 'Diabetes tipo 2', 'Insulina y seguimiento dietético', 'Evitar alimentos con alto índice glucémico', 2);

INSERT INTO Dispositivo (dispositivo_id, modelo, fecha_fabricacion, fecha_colocacion, paciente_id)
VALUES
    (1, 'Glucómetro A1', '2022-03-10 09:00:00', '2022-03-15 10:30:00', 1),
    (2, 'Glucómetro B2', '2022-04-20 14:00:00', '2022-04-25 15:45:00', 2);

INSERT INTO Medicion (medicion_id, fecha, glucemia, fabricante, dispositivo_id)
VALUES
    (1, '2022-05-01 08:00:00', 120.5, 'Empresa X', 1),
    (2, '2022-05-02 09:30:00', 140.2, 'Empresa Y', 2);
