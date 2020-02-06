# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from mysql import connector
app=Flask(__name__)

@app.route('/test')
def restTest():
    a={"name":"Roopesh", "company":"Artha Sangraha", "doj":"2019/01/02"}
    return render_template('abc.html', data=a)

@app.route('/OptDef', methods=['GET', 'POST'])
def OptDef():
    if request.method == 'GET':
        conn = connector.connect(user='Mercury', password='Mercury@1234', host='104.211.223.42', database='optionspakshidev', auth_plugin='mysql_native_password')
        cursor =conn.cursor()
        cursor.execute("select *  from bank1")
        row=cursor.fetchall()[0]
        a={"underlying":row[0],"l0":row[1], "l1":row[2],"l2":row[3],"l3":row[4],"l4":row[5],"above":row[6],"below":row[7],"top":row[8],"bottom":row[9],"up":row[10],"down":row[11],"15mtrend":row[12],"direction":row[13],"target":row[14],"pcrdirection":row[15],"to":row[16],"other":row[17]}
        return render_template('OptDef.html', data=a)
    if request.method == 'POST':
        level1 = request.form.get('level1')
        print ("Level 1", level1)
        return render_template('OptDef.html', data=a)
        

@app.route('/OptDefList')
def optdeflist():
    con = connector.connect(user='root',password='123456789',host='localhost',database='test',auth_plugin='mysql_native_password')
    cursor =con.cursor()
    cursor.execute("select *  from planning")
    a=cursor.fetchall()
    #a={"time":row[1],"strike":row[2],"entry":row[3],"stoploss":row[4],"target":row[5],"risk":row[6]}
    
    return render_template('OptDefList1.html', data=a)

methods=['GET', 'POST']
app.run()
