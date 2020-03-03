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

def postEventsList():
    
    con = getConn()
    cursor =con.cursor()
    cursor.execute("select *  from events")
    rows=cursor.fetchall()
    values = list()
    for row in rows:
        values.update( {"id":row[0], "newsdate":row[1],"header":row[2],"type":row[3],"impact":row[4],"impactrationale":row[5],"url":row[6],"effectivedate":row[7]})
    return values

def editEvent (id):
    con = getConn()
    cursor =con.cursor()
    sql = "edit from events where idno = {id}".format(id=id)
    print (sql)
    cursor.execute(sql)
    con.commit()

def DeleteEvent (id):
    con = getConn()
    cursor =con.cursor()
    sql = "delete from events where idno = {id}".format(id=id)
    print (sql)
    cursor.execute(sql)
    con.commit()

def SaveEvent (id, header):
    sql="""update optionspakshidev.events set header='{header}'
           where idno={id} """
    sql = sql.format(sql, header=header, id=id)
    print ("sql", sql)
    conn = getConn()
    cursor =conn.cursor()
    cursor.execute(sql)
    conn.commit()
    
    

