import pymysql
import json


conn = pymysql.connect(host='localhost',port=3306,user="root",passwd="MySQL",db="grupo12")
cur = conn.cursor()
cur.execute('select * from persona')
rows=[]
for row in cur:
    d={}
    d['nombre']  = str(row[0])
    d['fecha_nac']   = str(row[1])
    d['dni']  = str(row[2])
    d['altura']  = str(row[3])
    rows.append(d)
print(json.dumps(rows, separators=(', ', ': ')))
cur.close()
conn.close()
