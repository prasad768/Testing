from common import getSession
from db.OptDef import OptDef
def getOptDefList ():
    return getSession().query(OptDef).all()

    