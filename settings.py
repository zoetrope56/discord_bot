import os

TOKEN = os.getenv('DISCORD_TOKEN')
ASSET_KEYWORD = os.path.join(
                    os.path.dirname(__file__),
                    'command',
                    'asset',
                    'keywords.csv')

DISCORD_BOT_NAME = '김결정'

DANCE = False

MYSQL_HOST = os.getenv('L_MYSQL_DB_HOST')
MYSQL_PORT = os.getenv('L_MYSQL_DB_PORT', 3306)
MYSQL_DB_NAME = os.getenv('L_MYSQL_DB_NAME')
MYSQL_DB_USER = os.getenv('L_MYSQL_DB_USER')
MYSQL_DB_PASSWORD = os.getenv('L_MYSQL_DB_PASSWORD')

BANNED_KEYWORD = [
    '추가',
    '제거',
    '변경',
    # please add ban keyword on this list
]

ERROR_SQL_CONNECTION = 4001

MESSAGE_ERROR_CANNOT_USE_KEYWORD = '해당 키워드는 사용할 수 없습니다.'
MESSAGE_SUCCESS_ADD_KEYWORD = '키워드 추가 완료.'
MESSAGE_ERROR_ADD_KEYWORD_1 = '키워드 추가 실패.'
MESSAGE_ERROR_ADD_KEYWORD_2 = '키워드 추가 실패 - Internal error'
