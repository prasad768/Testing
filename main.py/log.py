# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 12:38:08 2020

@author: lenovo
"""

from flask import Flask, render_template
from mysql import connector
app=Flask(__name__)
@app.route("/")
def home():
    a={"name":"prasad","company":"artha sangrama"}
    return render_template('home.html',data=a)

@app.route("/about")
def root():
    conn = connector.connect(user='root', password='123456', host='localhost', database='test', auth_plugin='mysql_native_password')
    cursor =conn.cursor()
    cursor.execute("select *  from bank1")
    result=cursor.fetchall()[0]
    return render_template("about.html",user=result )



app.run() 