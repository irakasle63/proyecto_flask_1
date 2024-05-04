import sqlite3

#ProgrammingError
#sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. 
#The object was created in thread id 139831566119360 and this is thread id 139831443187264.


#SOLUCION
#sqlite3.connect("BDFlask_Sqlite.db", check_same_thread=False)

con = sqlite3.connect("wheather.db", check_same_thread=False)
cur = con.cursor()
cur.execute(
    "CREATE TABLE IF NOT EXISTS cities(id, name, temperature, rain_probability)"
)


def create(weather):
    con = sqlite3.connect("wheather.db")
    try:
        cur = con.cursor()
        cur.execute(
            """
            INSERT INTO cities ("id", "name", "temperature", "rain_probability") 
            VALUES (?, ?, ?, ?);
            """,
            [
                weather["id"],
                weather["name"],
                weather["temperature"],
                weather["rain_probability"],
            ],
        )
        # {'id': 'MNG', 'name': 'Managua', 'temperature': 38, 'rain_probability': 0.7}
        con.commit()
    finally:
        con.close()


def update(weather):
    con = sqlite3.connect("wheather.db")
    try:
        cur = con.cursor()
        cur.execute(
            """
            UPDATE cities 
               SET "name"=?, "temperature"=?, "rain_probability"=?
             WHERE "id"=?
            """,
            [
                weather["name"],
                weather["temperature"],
                weather["rain_probability"],
                weather["id"],
            ],
        )
        con.commit()
    finally:
        con.close()


def read(id):
    con = sqlite3.connect("wheather.db")
    try:
        cur = con.cursor()
        res = cur.execute("SELECT * FROM cities WHERE id=?", [id])
        row = res.fetchone()
        # (BIO, Bilbao. 19, 0.6)
        city = {
            "id": row[0],
            "name": row[1],
            "temperature": row[2],
            "rain_probability": row[3],
        }

        return city
    finally:
        con.close()


def read_all():
    res = cur.execute("SELECT name FROM cities")
   # resultado = res.fetchone()
    resultado = res.fetchall()
    print(resultado)
    return resultado


def delete(id):
    del WEATHER_DB[id]

    '''
BIO	Bilbao	34	0.5
MAD	Mad	20	0.3
MNG	Managua	38	0.7

    '''
