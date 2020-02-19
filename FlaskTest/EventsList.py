# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 00:01:20 2020

@author: hp
"""
from flask import Flask, render_template
from common import getConn
app=Flask(__name__)
@app.route('/table')
def getEventsList():
    #a={}
    #return render_template('table.html', data=a)
    con = getConn()
    cursor =con.cursor()
    cursor.execute("select *  from events")
    rows=cursor.fetchall()
    values = list()
    for row in rows:
        values.append( {"newsdate":row[1],"header":row[2],"type":row[3],"impact":row[4],"impactrationale":row[5],"url":row[6],"effectivedate":row[7]})
    return render_template('eventsList.html', data=values)

app.run()