import sqlite3
import random

db = sqlite3.connect('anekdot.db')
cursor = db.cursor()
random_nubmer = random.randrange(1, 1800, 1)
cursor.execute("SELECT * FROM anekdot WHERE rowid="+ str(random_nubmer))
row = cursor.fetchone()
print(str(row[1]))
db.close()
