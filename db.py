import threading

if __name__ == '__main__':
    create_engine('localhost', 'root', '123456', 'crawler')


def create_engine(host, user, password, database):
    import MySQLdb as msqldb
    global engine
    if engine is not None:
        raise DBError('Engine is already initialized.')
    params = dict(host=host,user=user,password=password,database=database,port=3306)
    defaults=dict(use_unicode=True,charset='utf8mb4',collation='utf8mb4_general_ci',autocommit=False)
    kw=[]
    for k, v in defaults.items():
        params[k] = kw.pop(k, v)
    params.update(kw)
    params['buffered'] = True

class DBError(Exception):
    pass


class MultiColumnsError(DBError):
    pass

# 数据库引擎对象
class _Engine(object):
    def __init__(self, connect):
        self._connect = connect
    def connect(self):
        return self._connect()

engine = None

# 持有数据库连接的上下文对象
class _DbCtx(threading.local):
    def __init__(self):
        self.connection = None
        self.transactions = 0

    def is_init(self):
        return not self.connection is None #
    def init(self):
        self.connection = _LasyConnection()
        self.transactions = 0
    def cleanup(self):
        self.connection.cleanup()
        self.connection = None
    def cursor(self):
        return self.connection.cursor()

_db_ctx = _DbCtx()

class _ConnectionCtx(object):
    def __enter__(self):    # 定义了__enter__和__exit__方法的对象可以用于with语句
        global _db_ctx
        self.should_cleanup = False
        if not _db_ctx.is_init():
            _db_ctx.init()
            self.should_cleanup = True
        return self
    def __exit__(self, exctype, excvalue, traceback):
        global _db_ctx
        if self.should_cleanup:
            _db_ctx.cleanup()

def connection():
    return _ConnectionCtx()