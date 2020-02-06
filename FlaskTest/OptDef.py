from flask import render_template, request
from mysql import connector


def getOptDef ():
    conn = connector.connect(user='Mercury', password='Mercury@1234', host='104.211.223.42', database='optionspakshidev', auth_plugin='mysql_native_password')
    cursor =conn.cursor()
    cursor.execute("select *  from bank1")
    row=cursor.fetchall()[0]
    a={"underlying":row[0],"l0":row[1], "l1":row[2],"l2":row[3],"l3":row[4],"l4":row[5],"above":row[6],"below":row[7],"top":row[8],"bottom":row[9],"up":row[10],"down":row[11],"15mtrend":row[12],"direction":row[13],"target":row[14],"pcrdirection":row[15],"to":row[16],"other":row[17]}
    return render_template('OptDef.html', data=a)

def postOptDef ():
    level1 = request.form.get('level1')
    print ("Level 1", level1)
    return render_template('OptDef.html', data=1)
