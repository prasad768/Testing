# -*- coding: utf-8 -*-
from mysql import connector
def getConn () :
    #return connector.connect(user='root',password='123456789',host='localhost',database='test',auth_plugin='mysql_native_password')
    return connector.connect(user='Mercury', password='Mercury@1234', host='104.211.223.42', database='optionspakshidev', auth_plugin='mysql_native_password')

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
engine=create_engine("mysql://Mercury:Mercury@1234@104.211.223.42/optionspakshidev")

def getEngine():
    return engine
    
def getSession() :
    session = Session(bind = engine)
    return session
