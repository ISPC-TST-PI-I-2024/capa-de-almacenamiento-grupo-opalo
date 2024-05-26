create database estructura;

use estructura; 

create table Paciente (
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    sexo CHAR(1) NOT NULL,
    peso DECIMAL(5, 2) NOT NULL,
    edad INT NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    altura DECIMAL(4, 2) NOT NULL,
    diabetes BOOLEAN NOT NULL,
    dni CHAR(8) PRIMARY KEY
    ) ; 

CREATE TABLE Contacto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    dni CHAR(8) NOT NULL,
    nro_contacto VARCHAR(15),
    direccion TEXT,
    email VARCHAR(100),
    calle VARCHAR(100),
    altura INT,
    departamento VARCHAR(10),
    provincia VARCHAR(50),
    localidad VARCHAR(50),
    codigo_postal VARCHAR(10),
    barrio VARCHAR(50),
    FOREIGN KEY (dni) REFERENCES Paciente(dni)
    );
    
CREATE TABLE ContactoEmergencia (
    id INT AUTO_INCREMENT PRIMARY KEY,
    dni CHAR(8) NOT NULL,
    nro_contacto VARCHAR(15),
    email VARCHAR(100),
    relacion VARCHAR(50),
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    FOREIGN KEY (dni) REFERENCES Paciente(dni)
    );
    
CREATE TABLE Dispositivo (
    mac CHAR(17) PRIMARY KEY,
    modelo VARCHAR(50) NOT NULL,
    fabricante VARCHAR(50) NOT NULL,
    fecha_colocacion DATE NOT NULL,
    fecha_fabricacion DATE NOT NULL,
    dni CHAR(8) NOT NULL,
    FOREIGN KEY (dni) REFERENCES Paciente(dni)
    );
    
CREATE TABLE Medicion (
    id INT AUTO_INCREMENT PRIMARY KEY,
    mac CHAR(17) NOT NULL,
    fecha_medicion DATE NOT NULL,
    glucemia DECIMAL(5, 2) NOT NULL,
    unidad VARCHAR(10) NOT NULL,
    FOREIGN KEY (mac) REFERENCES Dispositivo(mac)
    );

show tables;



