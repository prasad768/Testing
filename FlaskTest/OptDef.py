from flask import render_template, request
from common import getConn
def getOptDef ():
    conn = getConn()
    cursor =conn.cursor()
    cursor.execute("select *  from bank1")
    row=cursor.fetchall()[0]
    a={"underlying":row[0],"l0":row[1], "l1":row[2],"l2":row[3],"l3":row[4],"l4":row[5],"above":row[6],"below":row[7],"top":row[8],"bottom":row[9],"up":row[10],"down":row[11],"15mtrend":row[12],"direction":row[13],"target":row[14],"pcrdirection":row[15],"to":row[16],"other":row[17]}
    return render_template('OptDef.html', data=a)

def postOptDef ():
    level1 = request.form.get('level1')
    level2 = request.form.get('level2')
    level3 = request.form.get('level3')
    level4 = request.form.get('level4')
    level5 = request.form.get('level5')
    
    sql = """insert into optdef (level1, level2, level3, level4, level5) 
    values ({level1}, {level2}, {level3}, {level4}, {level5})"""
    sql = sql.format(sql, level1=level1, level2=level2, level3=level3, level4=level4, level5=level5)
    
    print ("sql", sql)
    conn = getConn()
    cursor =conn.cursor()
    cursor.execute(sql)
    cursor.commit()
    return getOptDef()
