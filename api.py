import utils as mysql
import crawler.settings as msqlSettings

# client = mysql.MysqlCon(msqlSettings.MYSQL_URI, msqlSettings.MYSQL_USER, msqlSettings.MYSQL_PASSWORD, msqlSettings.MYSQL_DATABASE)
# result = client.getAllItems('anqing')
# # print(result)
# client.closeCon()


def api(func):
    @functools.wraps(func)
    def _wrapper(*args, **kw):
        try:
            r = json.dumps(func(*args, **kw))
        except APIError, e:
            r = json.dumps(dict(error=e.error, data=e.data, message=e.message))
        except Exception, e:
            r = json.dumps(dict(error='internalerror', data=e.__class__.__name__, message=e.message))
        ctx.response.content_type = 'application/json'
        return r
    return _wrapper

@api
@get('/api/users')
def api_get_users():
    users = User.find_by('order by created_at desc')
    # 把用户的口令隐藏掉:
    for u in users:
        u.password = '******'
    return dict(users=users)