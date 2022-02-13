# 방법 1. 반복문으로 db에 직접 넣기
import pandas as pd
import pymysql

df = pd.read_csv("csv 파일 이름")

conn = pymysql.connect(host='localhost', port=3306, user='root', password='db 접속 암호', db='gemini')
cursor = conn.cursor()

# 반복문으로 정보 저장하기
for _ in range(10):
    area = "1000"
    concert_name = "정승환 슈퍼 콘서트"
    place = "부산 대연동 부경대학교"
    date  = "2022-02-10"    
    sql = f'''INSERT INTO `interparkconcert` (area, concert_name, place, date) 
        VALUES ('{area}', '{concert_name}', '{place}', '{date}');'''
    # 실행하는 코드
    cursor.execute(sql)

# 데이터베이스에 정보 저장 후 commit으로 저장하기
conn.commit()

# db에 저장된 정보 가져오기
sql = "select * from interparkconcert"
result = pd.read_sql_query(sql, conn)
df = result[:100]

#----------------------------------------------------------------------------------------------------------------------------------------#
# 방법 2. 데이터프레임을 데이터베이스에 넣기
import pandas as pd

import sqlalchemy
from sqlalchemy import create_engine
import configparser

config = configparser.ConfigParser()
# config.ini : 설정값이나 시크릿값을 따로 관리하기 위한 파일
config.read('config.ini', encoding='utf-8')

MY_SQL_PASSWORD = config['mySQL']['password']
MY_SQL_PATH = 'mysql+pymysql://' + 'root' + ':' + MY_SQL_PASSWORD + '@' + 'localhost' + ':3306/' + 'gemini?charset=utf8'

# 리스트를 데이터프레임으로 변환 후 db에 추가하기
def insert_concert_info_in_sql(concert_list: list):
    myEngine = create_engine(MY_SQL_PATH)
    cnxn = myEngine.connect()
    df = pd.DataFrame(concert_list)
    df.columns = ["area", "concert_name", "place", "start_date", "end_date"]
    df.to_sql('concert', con=cnxn, if_exists='append', index=False)    

#----------------------------------------------------------------------------------------------------------------------------------------#
# 데이터베이스 생성 코드

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Float, DateTime
import pymysql

import configparser

config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')

MY_SQL_PASSWORD = config['mySQL']['password']

MY_SQL_PATH = 'mysql+pymysql://' + 'root' + ':' + MY_SQL_PASSWORD + '@' + 'localhost' + ':3306/' + 'gemini?charset=utf8'
myEngine = create_engine(MY_SQL_PATH)
cnxn = myEngine.connect()

Base = declarative_base()
DBSession = sessionmaker(bind=myEngine)
session = DBSession()

class create_table_in_sql(Base):
    __tablename__ = "concert"
    id = Column(Integer, primary_key=True)
    area = Column(String(100))
    concert_name = Column(String(100))
    place = Column(String(100))
    start_date = Column(DateTime(timezone=True))
    end_date = Column(DateTime(timezone=True))

Base.metadata.create_all(myEngine)