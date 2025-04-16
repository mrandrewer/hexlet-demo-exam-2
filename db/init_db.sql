drop table if exists partner_products;
drop table if exists partners;
drop table if exists partner_types;
drop table if exists products;
drop table if exists product_types;
drop table if exists material_types;

create table material_types(
	id int primary key generated always as identity,
	type_name varchar(20) not null,
	failure_rate decimal not null
);

create table partner_types(
	id int primary key generated always as identity,
	type_name varchar(20) not null
);

create table partners (
	id int primary key generated always as identity,
	partner_type int not null references partner_types(id),
	partner_name varchar(250) not null,
	director_name varchar(150) not null,
	email varchar(100) not null,
	phone varchar(20) not null,
	address varchar(1000) null,
	inn varchar(11) not null,
	rating int not null
);

create table product_types(
	id int primary key generated always as identity,
	type_name varchar(50) not null,
	coef real not null
);

create table products(
	id int primary key generated always as identity,
	product_type int not null references product_types(id),
	product_name varchar(250) not null,
	article int not null,
	min_cost decimal not null
);

create table partner_products(
	id int primary key generated always as identity,
	product_id int not null references products(id),
	partner_id int not null references partners(id),
	product_amount int not null,
	sale_date date not null
);
	