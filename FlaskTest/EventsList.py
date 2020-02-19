# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 00:01:20 2020

@author: hp
"""
from common import getConn

def getEventsList():
    #a={}
    #return render_template('table.html', data=a)
    con = getConn()
    cursor =con.cursor()
    cursor.execute("select *  from events")
    rows=cursor.fetchall()
    values = list()
    for row in rows:
        values.append( {"id":row[0], "newsdate":row[1],"header":row[2],"type":row[3],"impact":row[4],"impactrationale":row[5],"url":row[6],"effectivedate":row[7]})
    return values

def DeleteEvent (id):
    con = getConn()
    cursor =con.cursor()
    sql = "delete from events where idno = {id}".format(id=id)
    print (sql)
    cursor.execute(sql)
    con.commit()
    