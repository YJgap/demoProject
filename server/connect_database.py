import pymysql
 
class MyData:
    def __init__(self):
        pass
    
    def get_database(self):
        data_list = []
        db = pymysql.connect(host='localhost', user='root', db='Anycall', password='P@ssw0rd', charset='utf8')
        curs = db.cursor()
        
        sql = "select * from anycall"
        curs.execute(sql)
        
        rows = curs.fetchall()
        for r in rows:
            temp = { 'id':r[0], 'firstName':r[1],'lastName':r[2],'nickName':r[3],'phone':r[4] }
            data_list.append(temp)
        
        db.commit()
        db.close()
        return data_list
    
    def insert_database(self, firstName, lastName, nickName, phone):
        db = pymysql.connect(host='localhost', user='root', db='Anycall', password='P@ssw0rd', charset='utf8')
        curs = db.cursor()
        
        sql = '''insert into anycall (firstName, lastName, nickName, phone) values(%s,%s,%s,%s)'''
        curs.execute(sql, (firstName, lastName, nickName, phone))
        db.commit()
        db.close()
    
    def update_database(self, id, firstName, lastName, nickName, phone):
        db = pymysql.connect(host='localhost', user='root', db='Anycall', password='P@ssw0rd', charset='utf8')
        curs = db.cursor()
        
        sql = "update anycall set firstName=%s, lastName=%s, nickName=%s, phone=%s where id=%s"
        curs.execute(sql, (firstName, lastName, nickName, phone, id))
        db.commit()
        db.close()

    def delete_database(self, id):
        db = pymysql.connect(host='localhost', user='root', db='Anycall', password='P@ssw0rd', charset='utf8')
        curs = db.cursor()
        
        sql = "delete from emp where empno=%s"
        curs.execute(sql, id)
        db.commit()
        db.close()
 
if __name__ == '__main__':
    result = MyData().get_database()
    print(result)