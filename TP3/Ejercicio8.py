import pymysql
import json


conn = pymysql.connect(host='localhost',port=3306,user="root",passwd="MySQL",db="grupo12")
cur = conn.cursor()
cur.execute('select p.dni, p.nombre, pp.fecha, pp.peso from persona p inner join personaPeso pp on p.dni=pp.dni')
rows=[]
for row in cur:
    d={}
    d['dni']  = row[0]
    d['nombre']   = row[1]
    d['fechaPeso']  = str(row[2])
    d['peso']  = row[3]
    rows.append(d)
print(json.dumps(rows, separators=(', ', ': ')))
cur.close()
conn.close()
