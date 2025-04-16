drop table if exists material_types;

create table material_types(
	id int primary key generated always as identity,
	type_name varchar(20) not null,
	failure_rate decimal not null
);


truncate table material_types;
truncate table partner_products;
truncate table partners cascade;
truncate table partner_types cascade;
truncate table products cascade;
truncate table product_types cascade;

insert into material_types (type_name, failure_rate) 
OVERRIDING SYSTEM VALUE
values
('Тип материала 1', 0.10),
('Тип материала 2', 0.95),
('Тип материала 3', 0.28),
('Тип материала 4', 0.55),
('Тип материала 5', 0.34);


insert into product_types (id, type_name, coef)
OVERRIDING SYSTEM VALUE
values
(1, 'Ламинат', 2.35),
(2, 'Массивная доска', 5.15),
(3, 'Паркетная доска', 4.34),
(4, 'Пробковое покрытие', 1.5);

select setval('product_types_id_seq', (select max(id) from product_types));

insert into products (id, product_type, product_name, article, min_cost)
OVERRIDING SYSTEM VALUE
values
(1,3,'Паркетная доска Ясень темный однополосная 14 мм','8758385',4456.90),
(2,3,'Инженерная доска Дуб Французская елка однополосная 12 мм','8858958',7330.99),
(3,1,'Ламинат Дуб дымчато-белый 33 класс 12 мм','7750282',1799.33),
(4,1,'Ламинат Дуб серый 32 класс 8 мм с фаской','7028748',3890.41),
(5,4,'Пробковое напольное клеевое покрытие 32 класс 4 мм','5012543',5450.59);

select setval('products_id_seq', (select max(id) from products));

insert into partner_types (id, type_name)
OVERRIDING SYSTEM VALUE
values
(1, 'ЗАО'),
(2, 'ООО'),
(3, 'ПАО'),
(4, 'ОАО');

select setval('partner_types_id_seq', (select max(id) from partner_types));

insert into partners (
    id,
    partner_type,
    partner_name,
    director_name,
    email,
    phone,
    address,
    inn,
    rating
) 
OVERRIDING SYSTEM VALUE
values
(1, 1, 'База Строитель', 'Иванова Александра Ивановна', 'aleksandraivanova@ml.ru', '493 123 45 67', '652050, Кемеровская область, город Юрга, ул. Лесная, 15', 2222455179, 7),
(2, 2, 'Паркет 29', 'Петров Василий Петрович', 'vppetrov@vl.ru', '987 123 56 78', '164500, Архангельская область, город Северодвинск, ул. Строителей, 18', 3333888520, 7),
(3, 3, 'Стройсервис', 'Соловьев Андрей Николаевич', 'ansolovev@st.ru', '812 223 32 00', '188910, Ленинградская область, город Приморск, ул. Парковая, 21', 4440391035, 7),
(4, 4, 'Ремонт и отделка', 'Воробьева Екатерина Валерьевна', 'ekaterina.vorobeva@ml.ru', '444 222 33 11', '143960, Московская область, город Реутов, ул. Свободы, 51', 1111520857, 5),
(5, 1, 'МонтажПро', 'Степанов Степан Сергеевич', 'stepanov@stepan.ru', '912 888 33 33', '309500, Белгородская область, город Старый Оскол, ул. Рабочая, 122', 5552431140, 10);

select setval('partners_id_seq', (select max(id) from partners));

insert into partner_products (
    id,
    product_id,
    partner_id,
    product_amount,
    sale_date
)
OVERRIDING SYSTEM VALUE
values
(1,1,1,15500,'2023-03-23'),
(2,3,1,12350,'2023-12-18'),
(3,4,1,37400,'2024-06-07'),
(4,2,2,35000,'2022-12-02'),
(5,5,2,1250,'2023-05-17'),
(6,3,2,1000,'2024-06-07'),
(7,1,2,7550,'2024-07-01'),
(8,1,3,7250,'2023-01-22'),
(9,2,3,2500,'2024-07-05'),
(10,4,4,59050,'2023-03-20'),
(11,3,4,37200,'2024-03-12'),
(12,5,4,4500,'2024-05-14'),
(13,3,5,50000,'2023-09-19'),
(14,4,5,670000,'2023-11-10'),
(15,1,5,35000,'2024-04-15'),
(16,2,5,25000,'2024-06-12');

select setval('partner_products_id_seq', (select max(id) from partner_products));

