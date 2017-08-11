create table cliente
(
	id INTEGER primary key autoincrement,
	name VARCHAR(80)
);

create table proveedor
(
	id INTEGER primary key autoincrement,
	name VARCHAR(80)
);

create table factura_cliente
(
	id INTEGER primary key autoincrement,
	cliente INTEGER,
	n_orden INTEGER,
	fecha DATE,
	importe REAL
);

create table factura_proveedor
(
	id INTEGER primary key autoincrement,
	proveedor INTEGER,
	n_orden INTEGER,
	fecha DATE,
	importe REAL
);

create table gasto
(
	id INTEGER primary key autoincrement,
	name VARCHAR(80)
);

create table factura_gasto
(
	id INTEGER primary key autoincrement,
	gasto INTEGER,
	n_orden INTEGER,
	fecha DATE,
	importe REAL
);


