import pymysql

conn = pymysql.connect(host='localhost',port=3306,user="root",passwd="MySQL",db="grupo12")

cur = conn.cursor()

cur.execute('select * from persona where dni={0}'.format(repr(4567)))

for row in cur:
    print(row)

cur.close()
conn.close()
