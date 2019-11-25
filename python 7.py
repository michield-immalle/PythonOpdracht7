import sqlite3
conn = sqlite3.connect('Leerlingen.sqlite3')

c = conn.cursor()

c.execute(''' CREATE TABLE leerlingen
                (ID integer, primary key, Voornaam tekst, achternaam tekst)''')

c.execute("INSERT INTO leerlingen VALUES('1', 'Joren', 'Rijk')")
c.execute("INSERT INTO leerlingen VALUES('2', 'Flip', 'Bernaard')")
c.execute("INSERT INTO leerlingen VALUES('3', 'Nick', 'Vervoort')")
c.execute("INSERT INTO leerlingen VALUES('4', 'Michiel', 'Dries')")
c.execute("INSERT INTO leerlingen VALUES('5', 'Jarnick', 'Sinaas')")
c.execute("INSERT INTO leerlingen VALUES('6', 'Thijs', 'Vervelen')")
c.execute("INSERT INTO leerlingen VALUES('7', 'Brent', 'Opwinden')")
c.execute("INSERT INTO leerlingen VALUES('8', 'Arne', 'Muilemans')")
c.execute("INSERT INTO leerlingen VALUES('9', 'Seppe', 'Weigerd')")
c.execute("INSERT INTO leerlingen VALUES('10', 'Jarnick', 'Onderbroeckie')")
