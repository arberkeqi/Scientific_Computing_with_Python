import sqlite3

# make a connection & create the file when it runs
conn = sqlite3.connect('orgdb.sqlite')
# like a handle; 
# open and send sql commends to the cursor and get responses through that cursor
cur = conn.cursor() 

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (
    org TEXT,  
    count INTEGER
    )'''
)

fname = input('Enter file name: ')
if (len(fname) < 1): 
    fname = 'mbox.txt'

fhand = open(fname)

counts = dict()
for lines in fhand:
    if not lines.startswith("From:"):
        continue
    pieces = lines.split()
    orgname = pieces[1]
    atpos = orgname.find("@")
    org = orgname[atpos + 1:]

    # '?' -> is a place holder; way not to allow sql injection 
    # it will be replaced by the "org" variable
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,)) # not retrieving the data
    row = cur.fetchone() # the info that we get from db
    if row is None: # if the db is empty print that line
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,)) # if the first time put count = 1
    else:
        # is always good to do an update cause maybe many working in it
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()