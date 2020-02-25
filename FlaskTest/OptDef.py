from flask import render_template, request
from common import getConn
def getOptDef (id):
    conn = getConn()
    cursor =conn.cursor()
    if id is None or id == 0 :
        cursor.execute("select *  from optdef".format(id=id))
    else:
        cursor.execute("select *  from optdef where id={id}".format(id=id))
    row=cursor.fetchall()[0]
    a={"id":row[0], "underlying":row[1],"l0":row[2], "l1":row[3],"l2":row[4],"l3":row[5],"l4":row[6],"above":row[7],"below":row[8],"top":row[9],"bottom":row[10],"up":row[11],"down":row[12],"trend15m":row[13],"direction":row[14],"target":row[15],"pcrdirection":row[16],"to":row[17],"other":row[18]}
    return render_template('OptDef.html', data=a)

def postOptDef (id):
    level1 = request.form.get('level1')
    level2 = request.form.get('level2')
    level3 = request.form.get('level3')
    level4 = request.form.get('level4')
    level5 = request.form.get('level5')
    notabove = request.form.get('notabove')
    notbelow = request.form.get('notbelow')
    ivtop = request.form.get('ivtop')
    ivbottom = request.form.get('ivbottom')
    weeklyexpirytargetup = request.form.get('weeklyexpirytargetup')
    weeklyexpirytargetdown = request.form.get('weeklyexpirytargetdown')
    trend15m = request.form.get('trend15m')
    maxpaindirection = request.form.get('maxpaindirection')
    maxpaintarget = request.form.get('maxpaintarget')
    pcrdirection = request.form.get('pcrdirection')
    pcrup = request.form.get('pcrup')
    pcrdown = request.form.get('pcrdown')
    
    if id==0: 
        sql = """insert into optDef  (level1, level2, level3, level4, level5,notabove,notbelow,ivtop,ivbottom,weeklyexpirytargetup,weeklyexpirytargetdown,trend15m,maxpaindirection,maxpaintarget,pcrdirection,pcrup,pcrdown) 
        values ({level1}, {level2}, {level3}, {level4}, {level5},{notabove},{notbelow},{ivtop},{ivbottom},{weeklyexpirytargetup},{weeklyexpirytargetdown},{trend15m},{maxpaindirection},{maxpaintarget},{pcrdirection},{pcrup},{pcrdown})"""
        sql = sql.format(sql, level1=level1, level2=level2, level3=level3, level4=level4, level5=level5,notabove=notabove,notbelow=notbelow,ivtop=ivtop,ivbottom=ivbottom,weeklyexpirytargetup=weeklyexpirytargetup,weeklyexpirytargetdown=weeklyexpirytargetdown,trend15m=trend15m,maxpaindirection=maxpaindirection,maxpaintarget=maxpaintarget,pcrdirection=pcrdirection,pcrup=pcrup,pcrdown=pcrdown)
    else:
        #sql="""update optdef set level1='{level1}', level2='{level2}', level3='{level3}', level4='{level4}', level5='{level5}',notabove='{notabove}',notbelow='{notbelow}',ivtop='{ivtop}',ivbottom='{ivbottom}',weeklyexpirytargetup='{weeklyexpirytargetup}',weeklyexpirytargetdown='{weeklyexpirytargetdown}',trend15m='{trend15m}',maxpaindirection='{maxpaindirection}'
           #where id={id} """
       # sql = sql.format(sql, level1=level1, level2=level2, level3=level3, level4=level4, level5=level5,notabove=notabove,notbelow=notbelow,ivtop=ivtop,ivbottom=ivbottom,weeklyexpirytargetup=weeklyexpirytargetup,weeklyexpirytargetdown=weeklyexpirytargetdown,trend15m=trend15m,maxpaindirection=maxpaindirection,maxpaintarget=maxpaintarget,pcrdirection=pcrdirection,pcrup=pcrup,pcrdown=pcrdown,id=id)
        id=request.form.get('id')
        sql="""delete from optdef where id={id} """
        sql=sql.format(sql,id=id)   
        
    
    print ("sql", sql)
    conn = getConn()
    cursor =conn.cursor()
    cursor.execute(sql)
    conn.commit()
    return getOptDef(0)
