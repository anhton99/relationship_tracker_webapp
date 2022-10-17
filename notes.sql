/* create users table */
CREATE TABLE users (id INTEGER,
username TEXT NOT NULL,
hash TEXT NOT NULL,
PRIMARY KEY(id))


/* create entries table */
CREATE TABLE entries (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    user_id INTEGER NOT NULL,
    subject TEXT NOT NULL,
    entries TEXT NOT NULL,
    time DATE NOT NULL)

/* create tracker table */
CREATE TABLE tracker (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    user_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    hours NUMERIC NOT NULL,
    relationship TEXT NOT NULL,
    activity TEXT NOT NULL,
    time DATE NOT NULL);




