# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from OptDef import getOptDef, postOptDef
from events import getdata, postdata
from EventsList import getEventsList, DeleteEvent

from OptDefList import getOptDefList1
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

@app.route('/events',methods=['GET','POST'])
def table1():
    if request.method == 'GET':
        id = request.args.get("id")
        return getdata(id)
    if request.method == 'POST':
        return postdata()

@app.route('/eventslist')
def eventslist():
    return render_template('eventsList.html', rows=getEventsList())

@app.route('/deleteevent')
def eventsDelete():
    id = request.args.get("id")
    DeleteEvent(id)
    return render_template('eventsList.html', rows=getEventsList())


app.run()
