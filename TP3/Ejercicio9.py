import pymysql


conn = pymysql.connect(host='localhost',port=3306,user="root",passwd="MySQL",db="grupo12")
cur = conn.cursor()
cur.execute('select p.dni, p.nombre, pp.fecha, pp.peso from persona p inner join personaPeso pp on p.dni=pp.dni where p.dni=1')
rows=[]
for row in cur:
    print('dni: ', row[0], '; ', 'nombre', row[1], '; ', 'fechaPeso', str(row[2]), '; ', 'peso', row[3])
cur.close()
conn.close()
