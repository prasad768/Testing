# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from mysql import connector
import OptDef
app=Flask(__name__)

@app.route('/test')
def restTest():
    a={"name":"Roopesh", "company":"Artha Sangraha", "doj":"2019/01/02"}
    return render_template('abc.html', data=a)

@app.route('/OptDef', methods=['GET', 'POST'])
def OptDef():
    if request.method == 'GET':
        OptDef.getOptDef()
    if request.method == 'POST':
        OptDef.postOptDef()

@app.route('/OptDefList')
    return optdeflist():

app.run()
