import pymysql
import pandas as pd

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='P@ssw0rd',
                     db='Anycall',
                     charset='utf8')

data = pd.read_csv('NaverContact.csv')
df = pd.DataFrame(data)

cursor = db.cursor()
df['nickName'].fillna("")
for firstName, lastName, nickName, phone in df[['firstName', 'lastName', 'nickName', 'phone']].values:
    sql = f"INSERT INTO anycall(firstName, lastName, nickName, phone) VALUES('{firstName}', '{lastName}', '{nickName}', '{phone}');"
    cursor.execute(sql)

cursor.execute("show tables")
db.commit()
db.close()
print("DB Setup sucksex")