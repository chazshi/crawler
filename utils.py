import MySQLdb as msqldb
# import pymysql as msqldb
# import time

class MysqlCon(object):
    def __init__(self, mysql_uri, mysql_user, mysql_password, mysql_database):
        config = {
            'host': mysql_uri,
            'port': 3306,
            'user': mysql_user,
            'passwd': mysql_password,
            'db': mysql_database,
            'charset': 'utf8mb4'
        }

        self.mysql_uri = mysql_uri
        self.mysql_user = mysql_user
        self.mysql_password = mysql_password
        self.mysql_database = mysql_database

        self.conn = msqldb.connect(**config)
        self.cursor = self.conn.cursor()
        # print('已连接mysql')
        self.conn.select_db(mysql_database)

        # self.client = msqldb.connect(self.mysql_uri, self.mysql_user, self.mysql_password, self.mysql_database)
        # self.client = msqldb.connect(host=self.mysql_uri, port=3306, user=self.mysql_user, passwd=self.mysql_password, db=self.mysql_database, charset='utf8')
        
        # return self.client
        
    # def getInstance(self):
    #     return self

    def closeCon(self):
        self.conn.close()
        # print('已关闭mysql')

    ### TODO：完成删除表代码
    def dropAllTable(self):
        sql = """SELECT concat('DROP TABLE IF EXISTS ', table_name, ';')
            FROM information_schema.tables
            WHERE table_schema = '%s';""" % "crawler"
        # print("开始删除！")

        self.cursor.execute(sql)

        # try:
        #     count = self.cursor.execute(sql)
        #     # result = self.cursor.fetchall()
        # except Exception as e:
        #     print("执行删除表操作出错: %s" % e)


        # print("count: %s" % count)
        # print("result: %s" % result)
        # print("删除成功！")
    
    def createTable(self, table):
        # print('sql query start!')

        # print("创建数据库")

        sql = """CREATE TABLE IF NOT EXISTS %s (
            title varchar(300) primary key NOT NULL, 
            time varchar(300) NOT NULL, 
            link varchar(300) NOT NULL
            );""" % table
        
        self.cursor.execute(sql)

        # print(sql)

        #创建表
        # TABLE_NAME = table
        # self.conn.cursor().execute('CREATE TABLE %s(title varchar(30) primary key, time varchar(30), link varchar(30))' %table)
        # try:
        #     self.cursor.execute(sql)
        #     print("创建数据表成功")
        # except Exception as e:
        #     print("创建数据表失败： %s" % e)
        # self.conn.commit()

    def storeIntoMsql(self, title, time, link, table):
        # print(title)
        # print(time)
        # print(link)
        # print(table)
        # print("存入数据库")

        sql = """INSERT INTO %s VALUES(
                "%s","%s","%s"
            );""" % (table, title, time, link)
        self.cursor.execute(sql)

        # print("sql: %s" % sql)
        
        # count = self.cursor.execute(sql)
        # result = self.cursor.fetchall()
        # print("count: %s" % count)
        # print("result: %s" % result)

        # try:
        #     count = self.cursor.execute(sql)
        #     print("存入成功：%s" % count)
        #     # return count

        # except Exception as e:
        #     # print("报错了： %s" % e)
        #     print("执行存入操作出错: %s" % e)

        #     self.createTable(table)
        #     print("sql: %s" % sql)
        #     self.cursor.execute(sql)

        #     # return -1

        # finally:
        #     # print('存入数据库成功')
        #     pass
        


    def getAllItems(self, table):
        sql = """SELECT * FROM %s;""" % table
        self.count = self.cursor.execute(sql)    #返回数据条数
        
        # time.sleep(3)
        # print(self.count)
        result = self.cursor.fetchall()
        # print(type(result))
        return result
