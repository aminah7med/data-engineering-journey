CREATE DATABASE IF NOT EXISTS data_engineering_shop;
USE data_engineering_shop;

CREATE TABLE IF NOT EXISTS customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(120) NULL,
    city VARCHAR(60) NULL,
    region VARCHAR(50) NULL,
    signup_date DATE NOT NULL,
    is_active TINYINT(1) NOT NULL DEFAULT 1,
    customer_segment VARCHAR(30) NOT NULL DEFAULT 'new'
);

CREATE TABLE IF NOT EXISTS departments (
    department_id INT PRIMARY KEY AUTO_INCREMENT,
    department_name VARCHAR(80) NOT NULL UNIQUE,
    budget DECIMAL(12,2) NULL,
    manager_employee_id INT NULL
);

CREATE TABLE IF NOT EXISTS employees (
    employee_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(120) NULL UNIQUE,
    department_id INT NULL,
    manager_id INT NULL,
    hire_date DATE NOT NULL,
    salary DECIMAL(12,2) NOT NULL,
    CONSTRAINT fk_employees_dept
        FOREIGN KEY (department_id) REFERENCES departments(department_id),
    CONSTRAINT fk_employees_manager
        FOREIGN KEY (manager_id) REFERENCES employees(employee_id)
);

CREATE TABLE IF NOT EXISTS products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(120) NOT NULL,
    category VARCHAR(60) NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    is_discontinued TINYINT(1) NOT NULL DEFAULT 0,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS orders (
    order_id BIGINT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    order_date DATETIME NOT NULL,
    status ENUM('pending', 'paid', 'shipped', 'cancelled') NOT NULL DEFAULT 'pending',
    shipping_city VARCHAR(60) NULL,
    total_amount DECIMAL(12,2) NOT NULL DEFAULT 0.00,
    CONSTRAINT fk_orders_customer
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE IF NOT EXISTS order_items (
    order_item_id BIGINT PRIMARY KEY AUTO_INCREMENT,
    order_id BIGINT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    discount_pct DECIMAL(5,2) NOT NULL DEFAULT 0.00,
    item_status ENUM('active', 'returned', 'cancelled') NOT NULL DEFAULT 'active',
    CONSTRAINT fk_order_items_order
        FOREIGN KEY (order_id) REFERENCES orders(order_id),
    CONSTRAINT fk_order_items_product
        FOREIGN KEY (product_id) REFERENCES products(product_id)
);

CREATE TABLE IF NOT EXISTS customer_email_history (
    record_id BIGINT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    email VARCHAR(120) NULL,
    source_system VARCHAR(30) NOT NULL,
    captured_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_customer_email_history_customer
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

INSERT INTO departments (department_name, budget, manager_employee_id) VALUES
    ('Engineering', 250000.00, NULL),
    ('Sales', 160000.00, NULL),
    ('Operations', 120000.00, NULL),
    ('Finance', 110000.00, NULL);

INSERT INTO employees (first_name, last_name, email, department_id, manager_id, hire_date, salary) VALUES
    ('Alice', 'Chen', 'alice.chen@example.com', 1, NULL, '2020-02-15', 120000.00),
    ('Omar', 'Hassan', 'omar.hassan@example.com', 1, 1, '2021-05-10', 95000.00),
    ('Priya', 'Shah', 'priya.shah@example.com', 2, 1, '2021-07-01', 88000.00),
    ('Linda', 'Gomez', 'linda.gomez@example.com', 3, 1, '2019-11-28', 82000.00),
    ('Ben', 'Ross', NULL, NULL, 3, '2022-06-12', 67000.00),
    ('Carla', 'Woods', 'carla.woods@example.com', 4, 1, '2020-09-05', 93000.00),
    ('Derek', 'Liu', 'derek.liu@example.com', 2, 3, '2023-01-18', 76000.00);

UPDATE departments
SET manager_employee_id = 1
WHERE department_name = 'Engineering';

UPDATE departments
SET manager_employee_id = 3
WHERE department_name = 'Sales';

UPDATE departments
SET manager_employee_id = 4
WHERE department_name = 'Operations';

UPDATE departments
SET manager_employee_id = 6
WHERE department_name = 'Finance';

ALTER TABLE departments
    ADD CONSTRAINT fk_departments_manager
    FOREIGN KEY (manager_employee_id) REFERENCES employees(employee_id);
