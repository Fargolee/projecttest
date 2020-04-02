import pymysql

class Db():
    def __init__(self , host , user , password , name):
        self.host = host
        self.user = user
        self.password = password
        self.name = name

    def chaxun(self , sql):
        db = pymysql.connect(host=self.host , user=self.user , password=self.password , db=self.name )
        cur = db.cursor()
        try:
            cur.execute(sql)
            res = cur.fetchall()
            db.close()
            return res
        except  Exception as e:
            return "SQL语句写错!" , e

    def xiugai(self , sql):
        db = pymysql.connect(host=self.host , user=self.user , password=self.password , db=self.name)
        cur = db.cursor()
        try:
            cur.execute(sql)
            db.close()
            return True
        except Exception as e:
            return "SQL语句写错!" , e

# db = Db("192.144.148.91", "ljtest", "123456", "ljtestdb")

# res = db.chaxun("select * from t_user where id = 251;")
# print(res)