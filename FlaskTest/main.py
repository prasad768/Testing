# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from OptDef import getOptDef, postOptDef
from OptDefList import getOptDefList
app=Flask(__name__)

@app.route('/test')
def restTest():
    a={"name":"Roopesh", "company":"Artha Sangraha", "doj":"2019/01/02"}
    return render_template('abc.html', data=a)

@app.route('/OptDef', methods=['GET', 'POST'])
def OptDef():
    if request.method == 'GET':
        return getOptDef()
    if request.method == 'POST':
        return postOptDef()

@app.route('/OptDefList')
def OptDefList():
    return getOptDefList()

app.run()
