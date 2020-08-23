import os
import sys
import csv
import pymysql

parentDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentDir)
import settings

def search(connection, cursor, message):
    try:
        if not cursor:
            return settings.SQL_CONNECTION_ERROR
        print('message.content >> {}'.format(message))
        sql = "select (RESULT) from KEYWORD_DICTIONARY where keyword like '" + message.content+ "'"
        cursor.execute(sql)

        last_row = list(cursor.fetchall())[-1]
        if last_row[0]:
            return last_row[0]
        else:
            return None
    except IndexError:
        return None
    except Exception as e:
        print(e)
        # try error report by using 'e' param
        return 'Server busy. please slow down'
