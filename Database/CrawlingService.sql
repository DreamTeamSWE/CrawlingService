drop table if exists location;
drop table if exists profilo_instagram;
drop table if exists post;
drop table if exists immagine;

/* CREATE DATABASE database_name DEFAULT CHARSET = utf8mb4 DEFAULT COLLATE = utf8mb4_unicode_ci; */

CREATE TABLE location (
    id int NOT NULL AUTO_INCREMENT,
	lat DECIMAL(7,4) NOT NULL,
	lng DECIMAL(7,4) NOT NULL,
	loc_name varchar(100) NOT NULL COLLATE utf8_general_ci,
	category varchar(100) NOT NULL,
	phone varchar(20),
	website varchar (2048),
	is_restaurant boolean NOT NULL,
	primary key(id),
	unique (lat, lng, loc_name)
	
	
);

CREATE TABLE profilo_instagram (
	username varchar(30) NOT NULL,
	data_ultimo_check datetime,
	post_utili int default 0,
	post_visti int default 0,
	level int default 2,
	primary key(username)
);

/* gestire emoji: https://stackoverflow.com/questions/39463134/how-to-store-emoji-character-in-mysql-database */

CREATE TABLE post (
	id int NOT NULL AUTO_INCREMENT,  /* da vedere se usare quello builtin del post */
    crawler_id varchar (50) NOT NULL unique,
	testo varchar(3000) , /* null per i post senza testo
							  --max lunghezza post instagram è 2200 chars */
	data_pubb date NOT NULL,
	username_autore varchar(30) NOT NULL 
		references profilo_instagram(username)
        on update cascade
        on delete set null,
    id_location int NOT NULL 
		references location(id)
        on update cascade
        on delete cascade,
	primary key(id)
) /* DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci; */;

/* TODO: #3 delete cascade non va*/
CREATE TABLE immagine (
    id int NOT NULL AUTO_INCREMENT,
    post_id int NOT NULL
		references post (id)
		on update cascade
		on delete cascade,
    primary key (id)
);