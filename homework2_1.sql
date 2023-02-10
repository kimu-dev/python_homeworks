create table if not exists employee (
	id serial primary key,
	name varchar(30) not null, 
	department varchar(30) not null, 
	chief_id int references employee(id),
	unique (department, chief_id)
);