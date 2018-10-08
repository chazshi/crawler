# test code

# import utils as mysql
import crawler.settings as msqlSettings

from utils import MysqlCon as mysql

client = mysql(msqlSettings.MYSQL_URI, msqlSettings.MYSQL_USER, msqlSettings.MYSQL_PASSWORD, msqlSettings.MYSQL_DATABASE)
result = client.getAllItems('anqing')
print(result)


client.closeCon()   # 执行完毕清除数据
