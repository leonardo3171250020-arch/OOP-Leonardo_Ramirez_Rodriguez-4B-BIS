CREATE DATABASE IF NOT EXISTS lab8_login;
USE lab8_login;
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    password VARCHAR(10) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE
);

INSERT INTO users (nombre, password, email) VALUES
('admin', 'admin!123', 'chase@gmail.com');