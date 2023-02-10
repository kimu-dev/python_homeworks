/*
Будем развивать схему для музыкального сервиса.

Ранее было ограничение, что каждый исполнитель поет строго в одном жанре - пора убрать это ограничение. Исполнители могут петь в разных жанрах, как и одному жанру могут принадлежать 
несколько исполнителей.

Аналогичное ограничение было и с альбомами у исполнителей (альбом мог выпустить только один исполнитель). Теперь альбом могут выпустить несколько исполнителей вместе. 
Как и исполнитель может принимать участие во множестве альбомов.

С треками ничего не меняем, все так же трек принадлежит строго одному альбому.

Но появилась новая сущность - сборник. Сборник имеет название и год выпуска. В него входят различные треки из разных альбомов.

Обратите внимание: один и тот же трек может присутствовать в разных сборниках.

Задание состоит из двух частей:

Спроектировать и нарисовать схему (как в первой домашней работе). Прислать изображение со схемой.
Написать SQL-запросы, создающие спроектированную БД. Прислать ссылку на файл, содержащий SQL-запросы.

Примечание: можно прислать сначала схему, получить подтверждение, что схема верная и после этого браться за написание запросов.
*/

create table if not exists genres (
	id serial primary key,
	genre_name varchar(50) unique not null
);

create table if not exists musicians (
	id serial primary key,
	musician_name varchar(100) unique not null
);

create table if not exists musicians_genres (
	id serial primary key,
	genre_id int not null references genres(id),
	musician_id int not null references musicians(id)
);

create table if not exists albums (
	id serial primary key,
	album_name varchar(50) not null,
	release_year int not null check (release_year < 2024)
);

create table if not exists musicians_albums (
	id serial primary key,
	album_id int references albums(id),
	musician_id int not null references musicians(id)
);

create table if not exists tracks (
	id serial primary key,
	track_name varchar(50) not null,
	duration int not null check (duration < 600),
	album_id int references albums(id),
	unique (id, album_id)
);

create table if not exists collections (
	id serial primary key,
	collection_name varchar(50) not null,
	release_year int not null check (release_year < 2024)
);

create table if not exists tracks_collections (
	id serial primary key,
	track_id int references tracks(id),
	collection_id int references collections(id)
);

/*
drop table tracks cascade;
drop table musicians cascade;
drop table albums cascade;
drop table music_genres cascade;
drop table collections cascade;
drop table musicians_genres;
drop table musicians_albums;
drop table tracks_collections;
*/

