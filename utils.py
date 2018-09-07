import MySQLdb

class MysqlCon(object):
    def __init__(self, mysql_uri, mysql_user, mysql_password, mysql_database):
        self.mysql_uri = mysql_uri
        self.mysql_user = mysql_user
        self.mysql_password = mysql_password
        self.mysql_database = mysql_database

    def openCon(self):
        self.client = MySQLdb.connect(self.mysql_uri, self.mysql_user, self.mysql_password, self.mysql_database)
        # return self.client
        print('已连接mysql')

    def closeCon(self):
        self.client.close()
        print('已关闭mysql')

    # def getCursor(self):
    #     self.cursor = self.client.cursor()

    def createTable(self, table):
        # print('sql query start!')
        
        # sql = """CREATE TABLE %s (
        #     TITLE CHAR(20) NOT NULL,
        #     time CHAR(20) NOT NULL, 
        #     link CHAR(20) NOT NULL,  
        #     ) IF NOT EXISTS %s""" % table


        sql = 'SHOW TABLES;'
        result = self.client.cursor().execute(sql).fetchall()
        # self.client.commit()
        # result = self.client.cursor().fetchall()    #？？？
        # print('sql query excuted!')
        print(result)

    

# def test():
#     print('test pass')

    



            # sql = 'SHOW'
        # try:
        #     # 执行SQL语句
        #     cursor.execute(sql)
        #     # 获取所有记录列表
        #     results = cursor.fetchall()
        #     for row in results:
        #         fname = row[0]
        #         lname = row[1]
        #         age = row[2]
        #         sex = row[3]
        #         income = row[4]
        #         # 打印结果
        #         print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
        #                 (fname, lname, age, sex, income )
        #     except:
        #     print "Error: unable to fecth data"
        

