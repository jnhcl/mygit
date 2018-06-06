#!/usr/bin/env python
# coding=utf-8

class _Engine(object):
    def __init__(self,connect):
        self._connect = connect
    def connect(self):
        return self._connect()

engine = None

class _DbCtx(threading.local):
    def __init__(self):
        self.connection = None
        self.transactions = 0

    def is_init(self):
        return not self.connections is None

    def init(self):
        self.connect = _LasyConnection()
        self.transaction = 0

    def cleanup(self):
        self.connection.cleanup()
        self.connection = None

    def cursor(self):
        return self.connection = None

_db_ctx = _DbCtx


