import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

cur.executescript('''
    DROP TABLE IF EXISTS User;
    DROP TABLE IF EXISTS Member;
    DROP TABLE IF EXISTS Course;

    CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
    );

    CREATE TABLE Course (
        id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title  TEXT UNIQUE
    );

    CREATE TABLE Role (
        role        INTEGER PRIMARY KEY,
        status       TEXT UNIQUE
    );

    CREATE TABLE Member (
        user_id     INTEGER,
        course_id   INTEGER,
        str_status    TEXT,
        PRIMARY KEY (user_id, course_id)
    )    
''')
# PRIMARY KEY (user_id, course_id) -> means that you can be a member of the course only once

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = 'roster_data.json'

str_data = open(fname).read()
json_data = json.loads(str_data)

for entry in json_data:
    
    name = entry[0]
    title = entry[1]
    role = entry[2]

    print((name, title))    # two paranthesis cause it's a 2 tuple

    if role == 1:
        cur.execute('''INSERT OR IGNORE INTO Role (role, status) 
            VALUES (?, 'Professor')''', (role, ))
        cur.execute('SELECT role FROM Role WHERE status = ?', (role, ))
        str_status = cur.fetchone()
    elif role == 0:
        cur.execute('''INSERT OR IGNORE INTO Role (role, status) 
            VALUES (?, 'Student')''', (role, ))
        cur.execute('SELECT role FROM Role WHERE status = ?', (role, ))
        str_status = cur.fetchone()
    

    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', ( name, ))
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, str_status) VALUES ( ?, ?, ? )''',
        ( user_id, course_id, str_status) )

    conn.commit()