-- Run this once to initialize the SQLite database
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password BLOB NOT NULL,
    age INTEGER,
    weight REAL,
    join_date DATE DEFAULT CURRENT_DATE
);

CREATE TABLE IF NOT EXISTS habits (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    date DATE NOT NULL,
    exercise_minutes INTEGER DEFAULT 0,
    sleep_hours REAL DEFAULT 0,
    water_litres REAL DEFAULT 0,
    calories INTEGER DEFAULT 0,
    FOREIGN KEY(user_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS goals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    exercise_goal INTEGER DEFAULT 30, -- minutes/day
    sleep_goal REAL DEFAULT 7.0,      -- hours/day
    water_goal REAL DEFAULT 3.0,      -- litres/day
    calories_goal INTEGER DEFAULT 2200,
    FOREIGN KEY(user_id) REFERENCES users(id)
);
