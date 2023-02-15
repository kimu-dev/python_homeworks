insert into musicians (musician_name) values 
	('Madonna'), -- pop
	('Nirvana'), -- rock
	('Kid Cudi'), -- hip-hop
	('Billie Eilish'), -- indi
	('The Weeknd'), -- hip-hop
	('Taylor Swift'), -- country
	('David Guetta'), -- pop
	('Papa Roach'); -- rock

insert into genres (genre_name) values
	('pop'),
	('hip-hop'),
	('rock'),
	('indi'),
	('country');
	
insert into albums (album_name, release_year) values
	('dont slime at me', 2017),
	('Nevermind', 1991),
	('After Hours', 2020),
	('KIDS SEE GHOSTS', 2018),
	('DOMINATION', 2021),
	('1989', 2014),
	('Celebration', 2009),
	('Let''s Love', 2020);

insert into musicians_albums (album_id, musician_id) values
	(7, 1),
	(2, 2),
	(4, 3),
	(1, 4),
	(3, 5),
	(6, 6),
	(8, 7),
	(7, 8);

insert into musicians_genres (genre_id, musician_id) values
	(1, 1),
	(3, 2),
	(2, 3),
	(4, 4),
	(2, 5),
	(5, 6),
	(1, 7),
	(3, 8);

insert into tracks (track_name, duration, album_id) values
	('Smells Like Teen Spirit', 300, 2),
	('Drain You', 223, 2),
	('Holiday', 368, 7),
	('Vogue', 316, 7),
	('Feel The Love', 165, 4),
	('Reborn', 384, 4),
	('party favor', 184, 1),
	('bellyache', 179, 1),
	('Blinding Lights', 200, 3),
	('Save Your Tears', 215, 3),
	('Blank Space', 231, 6),
	('Wildest Dreams', 220, 6),
	('Let''s Love', 222, 8),
	('DOMINATION', 168, 7),
	('My Relign', 194, 7);

insert into collections (collection_name, release_year) values
	('Start', 2019),
	('Sunshine ocean', 2020),
	('Red dress', 2018),
	('My favorite', 2010),
	('Yes/No', 2015),
	('Gold river', 2018),
	('Terra nova', 2021),
	('Orange', 2017);

insert into tracks_collections (track_id, collection_id) values
	(1, 5),
	(2, 5),
	(3, 3),
	(4, 3),
	(5, 8),
	(6, 8),
	(7, 1),
	(8, 1),
	(9, 7),
	(10, 7),
	(11, 2),
	(12, 2),
	(13, 4),
	(14, 6),
	(15, 6);