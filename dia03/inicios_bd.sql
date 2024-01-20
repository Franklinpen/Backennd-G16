-- SQL > Structured Query Language

-- DML 
-- Data Manipulation Language (Lenguaje de manupilación de Datos)

-- DDL
-- Data Definition Language (Lemguaje de Definición de Datos)
-- Sirve para indicar como se almaceran los datos, para definir las columnas
-- Tablas, entre otros
-- Los comandos en SQL tienen que finalizar con el ';' de manera obligatoria
-- IF NOT EXISTS sirve para comandos de CREACION (BD, TABLAS, COLUMNAS)
CREATE DATABASE IF NOT EXISTS pruebas; 

-- Seleccionamos en que base de datos vamos a trabajar
USE pruebas;

CREATE TABLE personas (
id 					INT AUTO_INCREMENT PRIMARY KEY,
nombre				TEXT NULL,
apellido			VARCHAR(50),
fecha_nacimiento	DATE,
nacionalidad		VARCHAR(100) DEFAULT 'PERUANO'
);

-- Agregar informacion a la tabla
INSERT INTO personas 	(id, nombre, apellido, fecha_nacimiento) VALUES
						(DEFAULT, 'Franklin', 'Peña', '1995-09-08');

-- Si no declaro las columnas que voy a insertar me veo en la obligacion 
-- de insertar valores a todas las columnas y siguiendo el mismo orden que usé al 
-- momento de crear la tabla

INSERT INTO personas VALUES (DEFAULT, 'Juana', 'Martinez', '2004-02-10', 'URUGUAYO');

INSERT INTO personas 	(nombre, apellido, fecha_nacimiento, nacionalidad) VALUES
						('Bryan', 'Urquizo', '1995-02-14', 'PERUANO'),
                        ('Maria', 'Retamozo', '1989-06-14', 'SALVADOREÑA');
                        
SELECT id, nombre FROM personas;

SELECT * FROM personas;

SELECT * -- columnas
FROM personas -- tabla
WHERE nombre = 'Franklin'; -- condicional

SELECT * FROM personas WHERE nacionalidad = 'PERUANO' and id = 1;

-- % no interesa donde se ubica el caracter
SELECT * FROM personas WHERE nombre LIKE '__a%'; -- '__a%' indica que en la tercera letra contiene la leta 'a'

SELECT * FROM personas WHERE nombre LIKE '%r%' OR apellido LIKE '%a%';

SELECT * FROM personas WHERE id IN (1, 2, 3);
-- SELECT * FROM personas WHERE id = 1 OR id = 2 OR id = 3;

SELECT * FROM personas 
LIMIT 2 -- 2 Elementos por pagina
OFFSET 4; -- Offset sirve para indicar cuantos se tiene que saltar 

-- Actualizaciones
UPDATE personas
SET nombre = 'Rodrigo', apellido = 'Flores'
WHERE id = 1;

SELECT * FROM personas WHERE id = 1;

-- Eliminar > DELETE
DELETE FROM personas WHERE id = 4;

SELECT * FROM personas;

-- DIRECCIONES > TABLA











