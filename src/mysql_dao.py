# /usr/bin/env python
# -*- coding: utf-8 -*-
import mysql.connector
import logging
# loggerの設定
logger = logging.getLogger("log")
logging.basicConfig(filename="debug.log", filemode='a', level=logging.DEBUG, \
                    format='%(asctime)s:%(levelname)s:%(message)s')

class Dao():
    #DBオブジェ作成
    def __init__(self,host='localhost',port=3306,user='root',password='root',database='test'\
                 ,auth_plugin='mysql_native_password'):
        try:
            self.conn = mysql.connector.connect(
                host=host,
                port=port,
                user=user,
                password=password,
                database=database,
                auth_plugin=auth_plugin,
            )
            self.cur = self.conn.cursor()
            print(self.conn.is_connected())
            logger.debug("db connection ok")
        except:
            logger.debug("db connection failed")
    #DB操作
    def execute(self, sql):
        try :
            self.cur.execute(sql)
            logger.debug("SQL ok")
            self.conn.commit()
            logger.debug("SQLcommit ok")
        except:
            logger.debug(sql+"SQL failed")
        # return self.cur.fetchall()
    #
    def insert_tabl_genre1(self,genre_id,genre_name):
        try :
            text = "INSERT INTO genre1 (genre_id,genre_name) VALUES (%d,'%s')" % (genre_id,genre_name)
            self.cur.execute(text)
            logger.debug("SQL_genre1 ok")
            self.conn.commit()
            logger.debug("SQLcommit_genre1 ok")
        except:
            logger.debug(str(genre_id)+"SQL_genre1 failed")
    def inser_tabl_rank(self,name,rank,genre):
        try :
            text = "INSERT INTO rank2 (item_name,rank_num,genre_id) VALUES ('%s',%d,%d)" % (name,rank,genre)
            print(text)
            self.cur.execute(text)
            logger.debug("SQL_genre1 ok")
            self.conn.commit()
            logger.debug(text+"SQLcommit_genre1 ok")
        except:
            logger.debug("##SQL_rank failed")

    # def insert_tabl_genre2(self,genre_id,genre1_id,genre_name):
    #     try :
    #         text = "INSERT INTO genre1 (genre_id,genre1,genre_name) VALUES (%d,%d,'%s')" % (genre_id,genre1_id,genre_name)
    #         self.cur.execute(text)
    #         logger.debug("SQL_genre1 ok")
    #         self.conn.commit()
    #         logger.debug("SQLcommit_genre1 ok")
    #     except:
    #         logger.debug(str(genre_id)+"SQL_genre1 failed")
    #
    # def insert_tabl_genre3(self,genre_id,genre1_id,genre2_id,genre_name):
    #     try :
    #         text = "INSERT INTO genre1 (genre_id,genre_name) VALUES (%d,%d,%d,'%s')" % (genre_id,genre1_id,genre2_id,genre_name)
    #         self.cur.execute(text)
    #         logger.debug("SQL_genre1 ok")
    #         self.conn.commit()
    #         logger.debug("SQLcommit_genre1 ok")
    #     except:
    #         logger.debug(str(genre_id)+"SQL_genre1 failed")

# sql=Dao()
# sql.execute("INSERT INTO smartshopping.genre1 (genre_id,genre_name) VALUES (564500,'スマートフォン・タブレット')")
# sql.execute("show databases;")

# Dao().execute("INSERT INTO smartshopping.genre1 (genre_id,genre_name) VALUES (564500,'スマートフォン・タブレット');")

