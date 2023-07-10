/*
    Title: outdoors.sql
    Author: Group 2
    Date: 8 July 2022
    Description: Outdoors Database initialization script.
*/

-- drop database if exists;
DROP DATABASE outdoors;

CREATE DATABASE outdoors;

-- drop outdoors user if exists 
DROP USER IF EXISTS 'outdoors_user'@'localhost';


-- create movies_user and grant them all privileges to the movies database 
CREATE USER 'outdoors_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'nature';

-- grant all privileges to the movies database to user movies_user on localhost 
GRANT ALL PRIVILEGES ON outdoors.* TO 'outdoors_user'@'localhost';

