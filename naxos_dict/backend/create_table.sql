CREATE TABLE glossary (
	ID int NOT NULL,
	term VARCHAR(255) UNIQUE NOT NULL,
	definition VARCHAR(255) UNIQUE NOT NULL,
	PRIMARY KEY(ID)
);
