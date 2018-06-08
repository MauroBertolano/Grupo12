import pymysql

conn = pymysql.connect(host='localhost',port=3306,user="root",passwd="MySQL",db="grupo12")

cur = conn.cursor()

cur.execute('update persona set nombre={0} where idPersona={1}'.format(repr("mauro"),repr(2)))
cur.execute('select * from persona')
for row in cur:
    print(row)

cur.close()
conn.close()
