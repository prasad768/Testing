# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from OptDef import getOptDef, postOptDef
from events import getdata, postdata

from OptDefList import getOptDefList
app=Flask(__name__)

@app.route('/')
def root():
    return render_template('main.html')

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
        return getdata()
    if request.method == 'POST':
        return postdata()


app.run()
