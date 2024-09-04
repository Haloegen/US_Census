import sqlite3
import csv
# This creates the database, if the database doesnt exist which it currently doesnt
conn = sqlite3.connect('US.db')
# This allows use use to query the data by creating a cursor object
cur = conn.cursor()

cur.execute(''' 
    CREATE TABLE IF NOT EXISTS US_CENSUS (
    id INTEGER PRIMARY KEY,
    age INTERGER NOT NULL,
    sex TEXT NOT NULL,
    bmi REAL NOT NULL,
    children INTEGER NOT NULL,
    smoker TEXT NOT NULL, 
    region TEXT NOT NULL,
    charges INTEGER
    )
''')

conn.commit()


with open('insurance.csv', newline='') as insurance_csv:
    insurance_reader = csv.reader(insurance_csv)
    next(insurance_reader, None)
    for row in insurance_reader:
        cur.execute('''
        INSERT INTO US_CENSUS(age, sex,bmi,children,smoker,region,charges)
        VALUES (?, ?, ?, ?, ?,? , ?)

        ''', (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        conn.commit()

cur.execute('SELECT * FROM US_CENSUS')
rows=cur.fetchall()
for row in rows:
    print(row)

conn.close()

