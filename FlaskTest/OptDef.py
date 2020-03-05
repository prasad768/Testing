from db.OptDef import OptDef
from flask import request

from common import getSession
def getOptDef (id):
    session=getSession()
    o=session.query(OptDef).get(id)
    print ("Object: ", o.id, o.underlying, o.level1)
    if o==None:
        o = OptDef()
    return o

#    conn = getConn()
#    cursor =conn.cursor()
#    if id is None or id == 0 :
#        cursor.execute("select *  from optdef".format(id=id))
#    else:
#        cursor.execute("select *  from optdef where id={id}".format(id=id))
#    row=cursor.fetchall()[0]
#    a={"id":row[0], "underlying":row[1],"l0":row[2], "l1":row[3],"l2":row[4],"l3":row[5],"l4":row[6],"above":row[7],"below":row[8],"top":row[9],"bottom":row[10],"up":row[11],"down":row[12],"trend15m":row[13],"direction":row[14],"target":row[15],"pcrdirection":row[16],"to":row[17],"other":row[18]}
#    return a

def postOptDef (id):
    session=getSession()
    o=session.query(OptDef).get(id)
    if o==None:
        o = OptDef()
    o.underlying='BANKNIFTY'
    o.level1 = request.form.get('level1')
    o.level2 = request.form.get('level2')
    o.level3 = request.form.get('level3')
    o.level4 = request.form.get('level4')
    o.level5 = request.form.get('level5')
    o.notabove = request.form.get('notabove')
    o.notbelow = request.form.get('notbelow')
    o.ivtop = request.form.get('ivtop')
    o.ivbottom = request.form.get('ivbottom')
    o.weeklyexpirytargetup = request.form.get('weeklyexpirytargetup')
    o.weeklyexpirytargetdown = request.form.get('weeklyexpirytargetdown')
    o.trend15m = request.form.get('trend15m')
    o.maxpaindirection = request.form.get('maxpaindirection')
    o.maxpaintarget = request.form.get('maxpaintarget')
    o.pcrdirection = request.form.get('pcrdirection')
    o.pcrup = request.form.get('pcrup')
    o.pcrdown = request.form.get('pcrdown')
    session.add(o)
    session.commit()
    return o.id
    