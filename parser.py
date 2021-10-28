import sqlite3
import requests
import bs4
import re

db = sqlite3.connect('anekdot.db')
cursor = db.cursor()
cursor.executescript("""create table anekdot(id int auto_increment primary key, anekdot longtext);""")
z = 0
for _ in range(60):
    z=z+1
    getting_url = requests.get('http://anekdotme.ru/random')
    getting_html = bs4.BeautifulSoup(getting_url.text, "html.parser")
    getting_anekgots = getting_html.select('.anekdot_text')
    for x in getting_anekgots:
        parsed_anekdots = (x.getText().strip())
        reg = re.compile('[^a-zA-Zа-яА-я .,!]')
        parsed_anekdots = reg.sub('', parsed_anekdots)
        cursor.execute("INSERT INTO anekdot (anekdot) VALUES ('"+parsed_anekdots+"')")
        db.commit()
    print(z)
db.close()
