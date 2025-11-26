CREATE DATABASE veterinaria;
USE veterinaria;
CREATE TABLE usuario(
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(50) NOT NULL
);
CREATE TABLE cuidador(
    rut_cuidador VARCHAR (12) PRIMARY KEY,
    nombre VARCHAR(50),
    direccion VARCHAR(80),
    telefono VARCHAR(12),
    email VARCHAR(80)
);
CREATE TABLE veterinario(
    rut_veterinario VARCHAR (12) PRIMARY KEY,
    nombre VARCHAR(50),
    especialidad VARCHAR(80),
    anios_experiencia INT,
    contacto VARCHAR(12)
);
CREATE TABLE mascota(
    id_mascota INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    especie VARCHAR(50),
    raza VARCHAR(50),
    edad INT,
    peso FLOAT,
    sexo VARCHAR(1),
    rut_cuidador VARCHAR (12),
    FOREIGN KEY (rut_cuidador) REFERENCES cuidador (rut_cuidador)
);
CREATE TABLE ficha_clinica(
    id_ficha INT AUTO_INCREMENT PRIMARY KEY,
    id_mascota INT,
    fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    diagnóstico VARCHAR(50),
    Tratamientos VARCHAR(30),
    Restricciones_alertas VARCHAR(80),
    FOREIGN KEY (id_mascota) REFERENCES mascota(id_mascota) ON DELETE CASCADE
);
CREATE TABLE procedimiento(
    id_procedimiento INT AUTO_INCREMENT PRIMARY KEY,
    id_ficha INT NOT NULL,
    rut_veterinario VARCHAR(12), #FK
    fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    tipo_procedimiento VARCHAR(50),
    indicaciones VARCHAR(100),
    costo INT,
    FOREIGN KEY (id_ficha) REFERENCES ficha_clinica (id_ficha),
    FOREIGN KEY (rut_veterinario) REFERENCES veterinario (rut_veterinario)
);