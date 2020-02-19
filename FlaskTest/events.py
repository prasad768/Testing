# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 10:07:41 2020

@author: hp
"""

from flask import render_template, request
from common import getConn

def getEventsList():
    conn = getConn()
    cursor =conn.cursor()
    cursor.execute("select *  from events ")
    rows=cursor.fetchall()
    return rows
    
    
def getdata (id):
    conn = getConn()
    cursor =conn.cursor()
    if id==0 or id is None:
        row = list(str(' ')*8)
    else:
        cursor.execute("select *  from events where idno = {id}".format(id= id))
        row=cursor.fetchall()[0]
    a={"idno":row[0], "newsdate":row[1], "header":row[2], "type":row[3],"impact":row[4],"impactrationale":row[5],"url":row[6],"effectivedate":row[7]}
    return render_template('events.html', data=a)
    
def postdata ():
    idno=request.form.get('idno')
    newsdate=request.form.get('newsdate')
    header=request.form.get('header')
    newstype=request.form.get('type')
    impact=request.form.get('impact')
    impactrationale=request.form.get('impactrationale')
    url=request.form.get('url')
    effectivedate=request.form.get('effectivedate')
    
    if idno==0 or idno is None or idno ==' ':    
       sql = """insert INTO events (newsdate, header, newstype, impact, impactrationale, url, effectivedate) 
       VALUES ('{newsdate}', '{header}', '{newstype}', '{impact}', '{impactrationale}', '{url}', '{effectivedate}')"""
       sql = sql.format(sql, idno=idno, newsdate=newsdate, header=header, newstype=newstype, impact=impact, impactrationale=impactrationale, url=url, effectivedate=effectivedate)
    else:
        sql = """update events set newsdate='{newsdate}', header='{header}', newstype='{newstype}', impact='{impact}', impactrationale='{impactrationale}', url='{url}', effectivedate='{effectivedate}' 
          where idno={idno} """
        sql = sql.format(sql,  newsdate=newsdate, header=header, newstype=newstype, impact=impact, impactrationale=impactrationale, url=url, effectivedate=effectivedate, idno=idno)
    
    
    print ("sql", sql)
    conn = getConn()
    cursor =conn.cursor()
    cursor.execute(sql)
    conn.commit()
    return getdata(1)
