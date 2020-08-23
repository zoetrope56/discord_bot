
import os
import sys
import hashlib
import settings

parentDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentDir)
import settings

def check_md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def insert_keyword(connection, cursor, key, value):
    try:
        if not cursor:
            return settings.SQL_CONNECTION_ERROR
        sql = 'insert into KEYWORD_DICTIONARY(keyword, result) values (%s, %s)'
        cursor.execute(sql, (key, value))
        return connection ,'<'+ key +'> : ' + settings.MESSAGE_SUCCESS_ADD_KEYWORD
    except IndexError:
        return settings.MESSAGE_ERROR_ADD_KEYWORD_1
    except Exception as e:
        print(e)
        # try error report by using 'e' param
        return settings.MESSAGE_ERROR_ADD_KEYWORD_2
