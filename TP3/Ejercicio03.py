import pymysql
import datetime

conn = pymysql.connect(host='localhost',port=3306,user="root",passwd="MySQL",db="grupo12")

cur = conn.cursor()
#cur.execute("""DELETE FROM persona WHERE idPersona={0}""".format(repr(7)))
cur.execute('DELETE FROM persona WHERE idPersona=%s',(8))
conn.commit()

cur.close()
conn.close()
