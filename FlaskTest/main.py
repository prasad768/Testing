# -*- coding: utf-8 -*-

from flask import Flask, render_template
app=Flask(__name__)

@app.route('/test')
def restTest():
    a={"name":"Roopesh", "company":"Artha Sangraha", "doj":"2019/01/02"}
    return render_template('abc.html', data=a)

@app.route('/OptDef')
def roots():
    a={}
    return render_template('abc.html', data=a)

@app.route('/OptDefList')
def roots():
    a={}
    return render_template('abc.html', data=a)

app.run()
