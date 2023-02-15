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