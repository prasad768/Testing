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
    a={"underlying":row[0], "l1":row[1],"l2":row[2]}
    return render_template('OptDef.html', data=a)

@app.route('/OptDefList')
def optdeflist():
    a={}
    return render_template('OptDefList.html', data=a)

app.run()
