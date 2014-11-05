#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Sai Yang'
#learn from Michael Line

import  os, re, sys, uuid, socket, datetime, functools, threading, logging

def _log(s):
    logging.debug(s)

def _dummy_connect():
    raise DBError('Database is not initialized. call init(dbn, ...) first.')

_db_connect = _dummy_connect
_db_convert = '?'

class _LasyConnection(object):
    def __init__(self):
        self.connection = None

    def cursor(self):
        if self.connection is None:
            _log('Open connection...')
            self.connection = _db_connect()
        return self.connection.cursor()
    
    def commit(self):
        self.connection.commit()
    
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

def _select(sql, first, *args):
    global _db_ctx, _db_convert
    cursor = None
    if _db_convert != '?':
        sql = sql.replace('?', _db_convert)
    try:
        cursor = _db_ctx.connection.cursor()
        cursor.execute(sql, args)
        if cursor.description:
            names = [x[0] for x in cursor.description]
        if first:
            values = cursor.fetchone()
            if not values:
                return None
            return values
        return [x for x in cursor.fetchall()]
    finally:
        if cursor:
            cursor.close()

@with_connection
def _update(sql, args, post_fn=None):
    global _db_ctx, _db_convert
    cursor = None
    if _db_convert != '?':
        sql = sql.replace('?', _db_convert)
   # _log('SQL: %s, ARGS: %s' %s (sql, args))
    try:
        cursor = _db_ctx.connection.cursor()
        cursor.execute(sql, args)
        r = cursor.rowcount
        if _db_ctx.transactions==0:
            _db_ctx.connection.commit()
            post_fn and post_fn()
        return r
    finally:
        if cursor:
            cursor.close()

@with_connection
def select(sql, *args):
    return _select(sql, False, *args)

def update(sql, *args):
    return _update(sql, args)

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
    dbpath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'doc_test.sqlite3.db')
    print(dbpath)
    if os.path.isfile(dbpath):
        os.remove(dbpath)
    init('sqlite3', dbpath, '')
    update('create table user (id int primary key, name text, email text, passwd text, last_modified real)')
