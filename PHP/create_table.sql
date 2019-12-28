CREATE TABLE IF NOT EXISTS stories
(
	id INT AUTO_INCREMENT	PRIMARY KEY,
	author INT	            NOT NULL,
	edition INT	            DEFAULT 1 NULL,
	published DATE	        DEFAULT 1970-01-01 NULL,
	title TEXT		 	    NOT NULL,
	subtitle TEXT 		    NOT NULL,
	content TEXT		    NOT NULL	
);
