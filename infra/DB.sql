CREATE DATABASE veterinaria;
USE veterinaria;

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


-- 1. Insertar Cuidadores
INSERT INTO cuidador (rut_cuidador, nombre, direccion, telefono, email) VALUES 
('12.345.678-9', 'Juan Pérez', 'Av. Siempre Viva 742', '+56911111111', 'juan@email.com'),
('9.876.543-2', 'María González', 'Calle Falsa 123', '+56922222222', 'maria@email.com'),
('15.555.444-K', 'Carlos Ruiz', 'Pasaje Los Aromos 45', '+56933333333', 'carlos@email.com');

-- 2. Insertar Veterinarios
INSERT INTO veterinario (rut_veterinario, nombre, especialidad, anios_experiencia, contacto) VALUES 
('10.111.222-3', 'Dra. Ana Silva', 'Medicina General', 5, '+56944444444'),
('14.222.333-4', 'Dr. Pedro Soto', 'Cirugía', 12, '+56955555555'),
('18.999.888-7', 'Dra. Laura Díaz', 'Dermatología', 8, '+56966666666');

-- 3. Insertar Mascotas (Se asocian a los RUTs de los cuidadores de arriba)
INSERT INTO mascota (nombre, especie, raza, edad, peso, sexo, rut_cuidador) VALUES 
('Bobby', 'Perro', 'Golden Retriever', 5, 30.5, 'M', '12.345.678-9'),
('Luna', 'Gato', 'Siamés', 3, 4.2, 'H', '9.876.543-2'),
('Rocky', 'Perro', 'Bulldog Francés', 2, 12.0, 'M', '15.555.444-K');

-- 4. Insertar Fichas Clínicas (Se asocian a los IDs de mascota 1, 2 y 3)
INSERT INTO ficha_clinica (id_mascota, diagnóstico, Tratamientos, Restricciones_alertas) VALUES 
(1, 'Otitis canina', 'Limpieza y gotas', 'Alergia a la penicilina'),
(2, 'Control sano', 'Vacuna triple felina', 'Ninguna'),
(3, 'Fractura leve pata', 'Vendaje y reposo', 'No correr por 2 semanas');

-- 5. Insertar Procedimientos (Se asocian a Fichas y Veterinarios)
INSERT INTO procedimiento (id_ficha, rut_veterinario, tipo_procedimiento, indicaciones, costo) VALUES 
(1, '10.111.222-3', 'Limpieza de oídos', 'Aplicar gotas cada 8 hrs', 25000),
(2, '10.111.222-3', 'Vacunación', 'Reposo por 24 hrs', 15000),
(3, '14.222.333-4', 'Radiografía', 'Volver a control en 1 semana', 45000);