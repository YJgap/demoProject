import pymysql
 
class MyData:
    def __init__(self):
        pass
    
    def get_database(self):
        data_list = []
        #host: 0.0.0.2 이거에 맞는 포트를 활용, user에 대해서도 여러가지 권한을 주어야 한다.(어드민, 일반 사용자, 관리자1...)
        curs = db.cursor()
        
        sql = "select * from anycall"
        curs.execute(sql)
        
        rows = curs.fetchall()
        for r in rows:
            temp = { 'id':r[0], 'firstName':r[1],'lastName':r[2],'nickName':r[3],'phone':r[4],'memo':r[5] }
            data_list.append(temp)
        
        db.commit()
        db.close()
        return data_list
        # return rows
    
    def insert_database(self, firstName, lastName, nickName, phone, memo):
        curs = db.cursor()
        
        sql = '''insert into anycall (firstName, lastName, nickName, phone, memo) values(%s,%s,%s,%s)'''
        curs.execute(sql, (firstName, lastName, nickName, phone, memo))
        db.commit()
        db.close()
    
    def update_database(self, id, firstName, lastName, nickName, phone, memo):
        curs = db.cursor()
        
        sql = "update anycall set firstName=%s, lastName=%s, nickName=%s, phone=%s, memo=%s where id=%s"
        curs.execute(sql, (firstName, lastName, nickName, phone, memo, id))
        # print(sql, (firstName, lastName, nickName, phone, id, memo))
        db.commit()
        db.close()

    # def update_memo_in_database(contact_id, memo):
    #     curs = db.cursor()

    #     sql = "UPDATE anycall SET memo=%s WHERE id=%s"
    #     curs.execute(sql, (memo, contact_id))
    #     db.commit()
    #     db.close()


    def delete_database(self, id):
        curs = db.cursor()
        
        sql = "delete from emp where empno=%s"
        curs.execute(sql, id)
        db.commit()
        db.close()
 
if __name__ == '__main__':
    result = MyData().get_database()
    # print(result)
