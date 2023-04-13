import pymysql
import pandas as pd

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     passwd='P@ssw0rd',
                     db='Anycall',
                     charset='utf8')

data = pd.read_csv('test.csv')
df = pd.DataFrame(data)

cursor = db.cursor()

for name, phone in df[['name', 'phone']].values:
    sql = f"INSERT INTO yjgap(name, phone) VALUES('{name}', '{phone}');"
    cursor.execute(sql)

cursor.execute("show tables") 
db.commit()
db.close()