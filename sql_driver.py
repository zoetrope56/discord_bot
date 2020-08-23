import os
import sys
import pymysql
import settings

def db_init():
    connection = pymysql.connect(host=settings.MYSQL_HOST,
                       port=int(settings.MYSQL_PORT),
                       user=settings.MYSQL_DB_USER,
                       password=settings.MYSQL_DB_PASSWORD,
                       db=settings.MYSQL_DB_NAME,
                       charset='utf8mb4')
    cursor = connection.cursor()
    return connection, cursor
