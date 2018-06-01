import pymysql
import datetime

conn = pymysql.connect(host='localhost',port=3306,user="root",passwd="MySQL",db="grupo12")

cur = conn.cursor()
cur.execute("""INSERT INTO persona(nombre,fecha_nac,dni,altura) VALUES({0},{1},{2},{3})""".format(repr('martin'),repr('1997-01-01'),repr('7854'),repr(1.5)))
conn.commit()

cur.close()
conn.close()
