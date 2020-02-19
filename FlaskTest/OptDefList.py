from flask import render_template
from common import getConn
def getOptDefList ():
    con = getConn()
    cursor =con.cursor()
    cursor.execute("select *  from planning")
    a=cursor.fetchall()
    #a={"time":row[1],"strike":row[2],"entry":row[3],"stoploss":row[4],"target":row[5],"risk":row[6]}
    
    return render_template('OptDefList1.html', data=a)

def getOptDefList1 ():
    con = getConn()
    cursor =con.cursor()
    cursor.execute("select id, underlying  from OptDef ")
    a=cursor.fetchall()
    #a={"time":row[1],"strike":row[2],"entry":row[3],"stoploss":row[4],"target":row[5],"risk":row[6]}
    return render_template('OptDef_Select.html', data=a)
