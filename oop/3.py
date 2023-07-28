import mysql.connector as connector

db= connector.connect(user="manjunath" ,password="Fire_master728",database="oop")

try :
    db.cursor().execute(input())
    db.commit()
    res=db.cursor().fetchall()
    for i in res:
        print(i)
except Exception as e:
    print(e)
