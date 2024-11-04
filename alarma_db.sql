CREATE DATABASE alarma_db;
USE alarma_db;
CREATE TABLE estado (
id INT AUTO_INCREMENT PRIMARY KEY,
 movimiento varchar(45),
timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

insert INTO estado (movimiento)
value('alarma activada');
SELECT * FROM estado;