import pymysql 
pymysql.install_as_MySQLdb()

import MySQLdb as msqldb
# import pymysql as msqldb
# import time

class MysqlCon(object):
    def __init__(self, mysql_uri, mysql_user, mysql_password, mysql_database, mysql_table):
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
        self.mysql_table = mysql_table

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
    
    # # 不需要了，django创建
    # def createTable(self, table):
    #     # print('sql query start!')

    #     # print("创建数据库")

    #     sql = """CREATE TABLE IF NOT EXISTS %s (
    #         title varchar(250) primary key NOT NULL, 
    #         time varchar(300) NOT NULL, 
    #         link varchar(300) NOT NULL
    #         );""" % table
        
    #     self.cursor.execute(sql)

        # print(sql)



    # id city title time link
    def storeIntoMsql(self, city, title, time, link):
        # print(self.mysql_table)
        # print(city)
        # print(title)
        # print(time)
        # print(link)
        # print("存入数据库")
        
        sql = """INSERT INTO %s( city, title, time, link) VALUES(
                "%s","%s","%s","%s"
            );""" % (self.mysql_table, city, title, time, link)

        # sql = """INSERT INTO crawler.infos(city, title, time, link) 
        #     VALUES("1安庆","1潜山市博物馆监控改造升级项目招标公告","12018-10-12","1www.aqzbcg.org:1102/jyxx/012002/012002001/20181012/c1756072-71a0-46e2-90a6-6d9d075997f4.html");"""
        

        # sql = """INSERT INTO crawler.infos select null,"1安庆","1潜山市博物馆监控改造升级项目招标公告","12018-10-12","1www.aqzbcg.org:1102/jyxx/012002/012002001/20181012/c1756072-71a0-46e2-90a6-6d9d075997f4.html";"""
        
        

        # print("sql: %s" % sql)
        self.cursor.execute(sql)
        self.conn.commit()
        # self.cursor.executemany(sql)
        # self.getAllItemsByTableName("infos")
        # num=self.cursor.rownumber
        # print(num)

        # data = self.cursor.fetchall()
        # print(data)


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
        

    # 1.查询所有表数据
    def getAllItems(self):
        pass

    # 2.获取所有表名
    def getAllTableName(self):
        pass

    # 3.根据表名获取表数据
    def getAllItemsByTableName(self, table):
        # pass

        # print("111")
        sql = """SELECT * FROM infos;"""# % table
        self.count = self.cursor.execute(sql)    #返回数据条数
        
        # time.sleep(3)
        # print(self.count)
        result = self.cursor.fetchall()
        # print(result)

        # print("111")
        # print(type(result))
        return result
    
    # 4.关键词查询
    def getItemsLike(self):
        pass

    