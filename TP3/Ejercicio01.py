import pymysql

conn = pymysql.connect(host='localhost',port=3306,user="root",passwd="MySQL",db="grupo12")

cur = conn.cursor()

cur.execute('select * from persona')

for row in cur:
    print(row)

cur.close()
conn.close()
