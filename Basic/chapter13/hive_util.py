__author__ = 'hzliyong'

import sqlite3


def convert(value):
    if value.startswith('~'):
        return value.strip('~')
    if not value:
        value = '0'


conn = sqlite3.connect('food.db')
curs = conn.cursor()
curs.execute('''
    CREATE TABLE food(
    id TEXT PRIMARY KEY,
    desc TEXT,
    water FLOAT,
    kcal FLOAT,
    protein FLOAT,
    fat FLOAT,
    ash FLOAT,
    carbs FLOAT,
    fiber FLOAT,
    sugar FLOAT)''')

query = 'INSERT INTO food VALUES (?,?,?,?,?,?,?,?,?,?)'

for line in open('ABBREV.TXT'):
    fields = line.split('^')
    field_count = len(fields)
    values = [convert(f) for f in fields[:field_count]]
    curs.execute(query, values)
conn.commit()
conn.close()
