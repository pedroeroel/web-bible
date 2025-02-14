DROP DATABASE IF EXISTS RoelTemplate;
CREATE DATABASE RoelTemplate;

USE RoelTemplate;

CREATE TABLE user (
    IDuser INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(30) NOT NULL,
    password VARCHAR(40) NOT NULL,
    email VARCHAR(100) NOT NULL
);

CREATE USER 'RoelNotetaker'@'%' IDENTIFIED BY 'notesaccess16as2';
GRANT ALL PRIVILEGES ON RoelTemplate.* TO 'RoelNotetaker'@'%';
FLUSH PRIVILEGES;
