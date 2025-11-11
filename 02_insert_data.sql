INSERT INTO productos(nombre, precio, stock) VALUES 
('Auriculares Bluetooth', 120.00, 35),
('Cámara Web HD', 75.00, 60),
('Monitor Curvo 32"', 850.00, 15),
('Teclado Inalámbrico', 65.00, 70),
('Base para Laptop', 55.00, 40),
('Adaptador USB-C', 25.00, 90);

INSERT INTO departamento(nombre) VALUES
('Logística'),
('Desarrollo'),
('Finanzas'),
('Publicidad');

INSERT INTO empleados(nombre) VALUES
('Laura Méndez'),
('Jorge Ramírez'),
('Valeria Cruz'),
('Tomás Herrera'),
('Claudia Salinas'),
('Andrés Navarro');

INSERT INTO empleados_departamento(id_empleado, id_departamento) VALUES
(1, 2),
(2, 3),
(3, 1),
(4, 4),
(5, 2),
(6, 1),
(1, 3);
