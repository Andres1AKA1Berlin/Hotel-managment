CREATE DATABASE hotel;

USE hotel;

CREATE TABLE customer (
    customer_id INT PRIMARY KEY,
    name VARCHAR(30),
    phone VARCHAR(15),
    address VARCHAR(50)
);

CREATE TABLE rooms (
    room_no INT PRIMARY KEY,
    room_type VARCHAR(20),
    rate INT,
    status VARCHAR(15)
);

CREATE TABLE booking (
    booking_id INT PRIMARY KEY,
    customer_id INT,
    room_no INT,
    days INT,
    bill INT
);

INSERT INTO rooms VALUES
(101, 'Single', 1000, 'Available'),
(102, 'Single', 1000, 'Available'),
(201, 'Double', 1800, 'Available'),
(202, 'Double', 1800, 'Available'),
(301, 'Deluxe', 3000, 'Available');






This is table
