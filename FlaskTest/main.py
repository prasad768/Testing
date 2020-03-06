# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, send_from_directory
from OptDef import getOptDef, postOptDef
from events import getdata, postdata, getEventData
import EventsList as evt


import os
app=Flask(__name__)

@app.route('/')
def root():
    return render_template('main.html')

@app.route('/optdeflist')
def OptDeflist():
    import OptDefList
    return render_template('Optdeflist.html', rows=OptDefList.getOptDefList())

@app.route ('/getoptDef') 
def test1():

    id = request.args.get("id")
    print ("id = ", id)
    event= getOptDef(id)
    print (event)
    return event

    
@app.route('/optdef', methods=['GET', 'POST'])
def OptDef():
    try:
        id = request.args.get("id")
    finally:
        if id==None:
            id=0
    print ("Id: ", id)
    if request.method == 'GET':
        return render_template('OptDef.html', data=getOptDef(id))
    if request.method == 'POST':
        id=postOptDef(id)
        return render_template('OptDef.html', data=getOptDef(id))

@app.route ('/getevent') 
def test():

    id = request.args.get("id")
    print ("id = ", id)
    event= getEventData(id)
    print (event)
    return event

@app.route('/events',methods=['GET','POST'])
def table1():
    id = request.args.get("id")
    if request.method == 'GET':
        return getdata(id)
    if request.method == 'POST':
        return postdata()

@app.route('/eventslist')
def eventslist():
    return render_template('eventsList.html', rows=evt.getEventsList())

@app.route('/saveEvent', methods=['POST'])
def saveEvent():
    header=request.form.get('header')
    id=request.form.get('id')
    evt.SaveEvent(id, header)
    print ('Save Event is called')
    
#@app.route('/saveOptDef', methods=['POST'])
#def saveOptDef():
#    notabove=request.form.get('notabove')
#    id=request.form.get('id')
#    saveOptDef(id,notabove)
#    print ('Save OptDef is called')

@app.route('/deleteevent')
def eventsDelete():
    id = request.args.get("id")
    evt.DeleteEvent(id)
    return render_template('eventsList.html', rows=evt.getEventsList())
#@app.route('/deleteOpt')
#def optDelete():
#    id = request.args.get("id")
#    deleteOpt(id)
#    
     
@app.route ('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

app.run()
