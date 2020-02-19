# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from OptDef import getOptDef, postOptDef
from events import getdata, postdata
from EventsList import getEventsList
from common import getConn

from OptDefList import getOptDefList
app=Flask(__name__)

@app.route('/')
def root():
    return render_template('main.html')

@app.route('/optdeflist')
def OptDeflist():
    return getOptDefList1 ()
    
@app.route('/optdef', methods=['GET', 'POST'])
def OptDef():
    id = request.args.get("id")
    if request.method == 'GET':
        return getOptDef(id)
    if request.method == 'POST':
        return postOptDef(id)

@app.route('/optdeflist')
def OptDefList():
    return getOptDefList()

@app.route('/events',methods=['GET','POST'])
def table1():
    if request.method == 'GET':
        id = request.args.get("id")
        return getdata(id)
    if request.method == 'POST':
        return postdata()

@app.route('/eventslist')
def eventslist():
    return render_template('eventsList.html', data=getEventsList())

def getOptDefList1 ():
    con = getConn()
    cursor =con.cursor()
    cursor.execute("select id, underlying  from OptDef ")
    a=cursor.fetchall()
    #a={"time":row[1],"strike":row[2],"entry":row[3],"stoploss":row[4],"target":row[5],"risk":row[6]}
    return render_template('OptDef_Select.html', data=a)

app.run()
