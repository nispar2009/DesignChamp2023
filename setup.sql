CREATE DATABASE dc
USE dc

CREATE TABLE quotes (id INTEGER PRIMARY KEY, categ INT, quote TEXT, person TEXT)
CREATE TABLE categs (id INTEGER PRIMARY KEY, _name TEXT)