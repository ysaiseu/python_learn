#!/usr/bin/env python
# -*- coding: utf-8 -*-

class _Engine(object):
	def __init__(self,connect):
		self._connect = connect
	def connect(self):
		return self._connect()

engine = None

class _LasyConnection(object):
    def __init__(self):
        self.connection = None

    def cursor(self):
        if self.connection is None:
            _log('Open connection...')
            self.connection = _db_connect()
        return self.connection.cursor()
    
    def cleanup(self):
        if self.connection:
            connection = self.connection
            self.connection = None
            _log('close connection...')
            connection.close()
        
class _DbCtx(threading.local):
	def __init__(self):
		self.connection = None
		self.transactions = 0

	def is_init(self):
		return not self.connection is None

	def init(self):
		self.connection = _LasyConnection()
		self.transactions = 0

	def cleanup(self):
		self.connection.cleanup()
		self.connection = None
	
	def cursor(self):
		return self.connction.cursor()

_db_ctx = _DbCtx()

class _ConnectionCtx(object):
	def __enter__(self):
		global _db_ctx
		self.should_cleanup = False
		if not _db_ctx.is_init():
			_db_ctx.init()
			self.should_clearup = True
		return self

	def __exit__(self, exctype, excvalue, traceback):
		global _db_ctx
		if self.should_cleanup:
			_db_ctx.clearnup()

def connection():
	return _ConnectionCtx()

def with_connection(func):
    @functools.wraps(func)
    def _wrapper(*args, **kw):
        with _ConnectionCtx():
            return func(*args, **kw)
    return _wrapper

@with_connection
def select(sql, *args):
        pass

@with_connection
def update(sql, *args):
        pass

def init(db_type, db_schema, db_host, db_port=0, db_user=None, db_password=None, db_driver=None, **db_args):

    global _db_connect, _db_convert
    if db_type=='mysql':
        import MySQLdb
        if not 'use_unicode' in db_args:
            db_args['use_unicode'] = True
        if not 'charset' in db_args:
            db_args['charset'] = 'utf8'
        if db_port==0:
            db_port = 3306
        _db_connect = lambda: MySQLdb.connect(db_host, db_user, db_password, db_schema, db_port, **db_args)
        _db_convert = '%s'
    elif db_type=='sqlite3':
        import sqlite3
        _db_connect = lambda: sqlite3.connect(db_schema)
    else:
        raise DBEroor('Unsupported db: %s' % db_type)

if __name__=='__main__':
    sys.path.append('.')
    dpath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'doc_test.sqlite3.db')
    print(dbpath)
    if os.path.isfile(dbpath):
        os.remove(dbpath)
    init('sqlite3', dbpath, '')
