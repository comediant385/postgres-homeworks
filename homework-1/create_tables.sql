-- SQL-команды для создания таблиц
CREATE TABLE employees
(
	employee_id int PRIMARY KEY,
	first_name varchar(100) NOT NULL,
	last_name varchar(100) NOT NULL,
	title varchar(100) NOT NULL,
	birth_date varchar(100) NOT NULL,
	notes text
);

CREATE TABLE customer
(
	customer_id varchar(100) PRIMARY KEY,
	company_name varchar(100) NOT NULL,
	contact_name varchar(100) NOT NULL

);

CREATE TABLE orders
(
	order_id int PRIMARY KEY,
	customer_id varchar(100) REFERENCES customer(customer_id) NOT NULL,
	contact_name varchar(100) NOT NULL,
	employee_id int REFERENCES employees(employee_id) NOT NULL,
	order_date date NOT NULL,
	ship_city varchar(100) NOT NULL
)