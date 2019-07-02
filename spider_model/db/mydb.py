# -*- coding:utf-8 -*-
import pymysql
from spider_model.conf.confs import *
from spider_model.logs.log_info import logger


class MySQL:
    def __init__(self, host=MYSQL_HOST, username=MYSQL_USER, password=MYSQL_PASSWORD, port=MYSQL_PORT,
                 database=MYSQL_DATABASE):
        """
        MySQL初始化
        :param host:
        :param username:
        :param password:
        :param port:
        :param database:

        """
        try:
            self.db = pymysql.connect(host, username, password, database, charset='utf8', port=port)
            self.cursor = self.db.cursor()
        except pymysql.MySQLError as e:
            logger.error(e.args)
            # print(e.args)

    def insert(self, table, data):
        """
        插入数据
        :param table:
        :param data:
        :return:
        """
        keys = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))
        sql_query = 'insert into %s (%s) values (%s)' % (table, keys, values)
        print(sql_query)
        try:
            self.cursor.execute(sql_query, tuple(data.values()))
            self.db.commit()
        except pymysql.MySQLError as e:
            logger.error(e.args)
            self.db.rollback()

    def query_insert(self, table, data):
        """
        查询后插入
        :return: 数据库中没有重复数据
        """
        keys = [keys for keys, values in data.items()]
        values = [values for keys, values in data.items()]
        sql = "select * from {0} where {1}='{2}'".format(table, keys[0], values[0])
        self.cursor.execute(sql)
        cons = self.cursor.fetchall()
        if len(cons) == 0:
            sql_query = 'insert into %s (%s) values (%s)' % (table, keys, values)
            try:
                self.cursor.execute(sql_query, tuple(data.values()))
                self.db.commit()
            except pymysql.MySQLError as e:
                logger.error(e.args)
                self.db.rollback()
        else:
            logger.info('数据已经存在')

    def db_close(self):
        if self.db:
            logger.info('数据已经存在')
            self.db.close()
