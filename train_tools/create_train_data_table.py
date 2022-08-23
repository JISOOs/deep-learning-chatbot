import pymysql
from config.DatabaseConfig import *

db = None
try:
    db = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        passwd=DB_PASSWORD,
        db=DB_NAME,
        charset='utf8'
    )
    print("DB 연결 성공")

    # 1. 테이블 생성
    sql = '''
    CREATE TABLE IF NOT EXISTS `chatbot_train_data` (
        `id` int unsigned not null auto_increment,
        `intent` varchar(45) null,
        `ner` varchar(1024) null,
        `query` text null,
        `answer` text not null,
        `answer_image` varchar(2048) null,
        primary key(`id`))
    ENGINE=InnoDB DEFAULT CHARSET=UTF8
    '''

    with db.cursor() as cursor:
        cursor.execute(sql)

except Exception as e:
    print(e)
finally:
    if db is not None:
        db.close()
        print("DB 닫기 성공")
