import pymysql
#import mysql.connector
import sys
_connection = None

def get_connection():
    global _connection
    if not _connection:
        #_connection = pymysql.connect(host="localhost",port=10002,user="pythonesia",passwd="PemalangPintar2018", db="pythonesia",max_allowed_packet=16777216)
        _connection = pymysql.connect(host="localhost",port=3306,user="root",passwd="12345678", db="sidekem")
        #_connection = mysql.connector.connect(user='pythonesia',port='10002', password='PemalangPintar2018',host='localhost',database='pythonesia')
    return _connection

__all__ = [ 'getConnection' ]

