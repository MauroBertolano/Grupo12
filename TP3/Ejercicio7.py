import pymysql

conn = pymysql.connect(host='localhost',port=3306,user="root",passwd="MySQL",db="grupo12")
cur = conn.cursor()
cur.execute('CREATE TABLE `grupo12`.`personapeso` (`dni` INT NOT NULL, `fecha` DATE NOT NULL, `peso` INT NULL, PRIMARY KEY (`dni`, `fecha`), CONSTRAINT `fk_personaPeso_persona` FOREIGN KEY (`dni`) REFERENCES `grupo12`.`persona` (`dni`) ON DELETE NO ACTION ON UPDATE NO ACTION)')
cur.close()
conn.close()
