from mysql import connector
from flask import render_template
def getOptDefList ():
    con = connector.connect(user='root',password='123456789',host='localhost',database='test',auth_plugin='mysql_native_password')
    cursor =con.cursor()
    cursor.execute("select *  from planning")
    a=cursor.fetchall()
    #a={"time":row[1],"strike":row[2],"entry":row[3],"stoploss":row[4],"target":row[5],"risk":row[6]}
    
    return render_template('OptDefList1.html', data=a)
