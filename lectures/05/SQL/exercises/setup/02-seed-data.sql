USE data_engineering_shop;

INSERT INTO customers (first_name, last_name, email, city, region, signup_date, is_active, customer_segment) VALUES
    ('Alice', 'Johnson', 'alice.johnson@example.com', 'Seattle', 'West', '2022-01-14', 1, 'vip'),
    ('Mark', 'Taylor', 'mark.taylor@example.com', 'Austin', 'South', '2023-02-18', 1, 'new'),
    ('Sofia', 'Martinez', 'sofia.martinez@example.com', 'Chicago', 'Midwest', '2021-10-06', 1, 'returning'),
    ('Drew', 'Price', NULL, NULL, NULL, '2023-05-10', 0, 'new'),
    ('Nina', 'Patel', 'nina.patel@example.com', 'Boston', 'East', '2022-11-30', 1, 'returning'),
    ('Leo', 'Kim', 'leo.kim@example.com', 'Denver', 'West', '2023-07-19', 1, 'new'),
    ('Tara', 'Wilson', 'tara.wilson@example.com', 'Atlanta', 'South', '2024-01-03', 1, 'new');

INSERT INTO products (product_name, category, unit_price, is_discontinued, created_at) VALUES
    ('Laptop Pro 14', 'Electronics', 1499.99, 0, '2023-01-10 08:00:00'),
    ('Mechanical Keyboard', 'Electronics', 129.00, 0, '2023-02-11 09:15:00'),
    ('Wireless Mouse', 'Electronics', 49.99, 0, '2023-02-11 09:20:00'),
    ('4K Monitor', 'Electronics', 399.99, 0, '2023-03-08 10:45:00'),
    ('Office Chair', 'Furniture', 249.00, 0, '2023-04-02 12:00:00'),
    ('Notebook Set', 'Office Supplies', 18.50, 0, '2023-04-30 06:00:00'),
    ('USB-C Cable', 'Accessories', 12.99, 0, '2023-05-12 07:00:00'),
    ('Webcam HD', 'Electronics', 89.99, 0, '2023-06-19 14:10:00'),
    ('Coffee Mug', 'Office Supplies', 15.00, 0, '2023-07-01 11:45:00');

INSERT INTO orders (customer_id, order_date, status, shipping_city, total_amount) VALUES
    (1, '2024-03-05 10:15:00', 'shipped', 'Seattle', 1658.97),
    (2, '2024-03-07 09:00:00', 'paid', 'Austin', 820.00),
    (3, '2024-03-10 14:30:00', 'cancelled', 'Chicago', 0.00),
    (4, '2024-03-13 11:00:00', 'paid', 'Dallas', 1325.00),
    (5, '2024-03-16 17:45:00', 'pending', 'Boston', 419.99),
    (1, '2024-03-20 08:00:00', 'shipped', 'Seattle', 2345.00),
    (6, '2024-03-22 15:10:00', 'paid', 'Denver', 174.98);

INSERT INTO order_items (order_id, product_id, quantity, unit_price, discount_pct, item_status) VALUES
    (1, 1, 1, 1499.99, 0.00, 'active'),
    (1, 3, 2, 49.99, 0.00, 'active'),
    (1, 2, 1, 129.00, 10.00, 'active'),
    (2, 4, 1, 399.99, 0.00, 'active'),
    (2, 7, 2, 12.99, 0.00, 'active'),
    (3, 9, 1, 15.00, 0.00, 'cancelled'),
    (4, 5, 2, 249.00, 0.00, 'active'),
    (4, 6, 5, 18.50, 0.00, 'active'),
    (4, 9, 1, 15.00, 0.00, 'active'),
    (5, 8, 1, 89.99, 0.00, 'active'),
    (5, 3, 2, 49.99, 5.00, 'active'),
    (6, 1, 1, 1499.99, 0.00, 'active'),
    (6, 2, 1, 129.00, 15.00, 'active'),
    (6, 5, 1, 249.00, 0.00, 'active'),
    (7, 9, 2, 15.00, 0.00, 'active');

INSERT INTO customer_email_history (customer_id, email, source_system, captured_at) VALUES
    (1, 'alice.johnson@example.com', 'crm', '2024-02-01 09:00:00'),
    (1, 'alice.johnson@example.com', 'website', '2024-03-01 10:00:00'),
    (2, 'mark.taylor@example.com', 'crm', '2024-02-10 12:00:00'),
    (2, 'mark.taylor+promo@example.com', 'marketing', '2024-02-12 12:00:00'),
    (3, 'sofia.martinez@example.com', 'crm', '2024-02-15 08:15:00'),
    (3, NULL, 'website', '2024-02-15 08:30:00'),
    (4, NULL, 'crm', '2024-03-11 09:00:00'),
    (5, 'nina.patel@example.com', 'crm', '2024-02-27 11:00:00');

SELECT 'Database setup complete.' AS status;
