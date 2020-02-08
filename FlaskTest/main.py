# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from OptDef import getOptDef, postOptDef
from events import getdata, postdata

from OptDefList import getOptDefList
app=Flask(__name__)

@app.route('/')
def root():
    return render_template('main.html')

@app.route('/test')
def restTest():
    a={"name":"Roopesh", "company":"Artha Sangraha", "doj":"2019/01/02"}
    return render_template('abc.html', data=a)

@app.route('/optdef', methods=['GET', 'POST'])
def OptDef():
    if request.method == 'GET':
        return getOptDef()
    if request.method == 'POST':
        return postOptDef()

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
