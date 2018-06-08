import pymysql
import json


conn = pymysql.connect(host='localhost',port=3306,user="root",passwd="MySQL",db="grupo12")
cur = conn.cursor()
cur.execute('select p.dni, p.nombre, p.fecha_nac, p.altura, pp.fecha, pp.peso from persona p inner join personaPeso pp on p.dni=pp.dni')
rows=[]
for row in cur:
    d={}
    d['dni']  = row[0]
    d['nombre']   = row[1]
    d['fechaNac']  = str(row[2])
    d['altura']  = row[3]
    d['fechaPeso']  = str(row[4])
    d['peso']  = row[5]
    rows.append(d)
print(json.dumps(rows, indent=6, separators=(', ', ': ')))
cur.close()
conn.close()
