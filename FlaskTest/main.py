# -*- coding: utf-8 -*-

from flask import Flask, render_template
from mysql import connector
app=Flask(__name__)

@app.route('/test')
def restTest():
    a={"name":"Roopesh", "company":"Artha Sangraha", "doj":"2019/01/02"}
    return render_template('abc.html', data=a)

@app.route('/OptDef')
def roots():
    conn = connector.connect(user='root', password='123456', host='localhost', database='test', auth_plugin='mysql_native_password')
    cursor =conn.cursor()
    cursor.execute("select *  from bank1")
    row=cursor.fetchall()[0]
    a={"underlying":row[0],"l0":row[1], "l1":row[2],"l2":row[3],"l3":row[4],"l4":row[5],"above":row[6],"below":row[7],"top":row[8],"bottom":row[9],"up":row[10],"down":row[11],"15mtrend":row[12],"direction":row[13],"target":row[14],"pcrdirection":row[15],"to":row[16],"other":row[17]}
    return render_template('OptDef.html', data=a)

@app.route('/OptDefList')
def optdeflist():
    a={}
    return render_template('OptDefList.html', data=a)

app.run()
