from sqlalchemy import Column, Integer, String
#from common import getEngine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
Base = declarative_base()

class OptDef(Base):
   __tablename__ = 'OptDef'
   id = Column('Id', Integer, primary_key=True )

   underlying= Column('Underlying', String)
   level1 = Column('level1', Integer)
   level2 = Column('level2', Integer)
   level3 = Column('level3', Integer)
   level4 = Column('level4', Integer)
   level5 = Column('level5', Integer)
   notabove = Column('notabove', Integer)
   notbelow = Column('notbelow', Integer)
   ivtop = Column('ivtop', Integer)
   ivbottom = Column('ivbottom', Integer)
   weeklyexpirytargetup = Column('weeklyexpirytargetup', Integer)
   weeklyexpirytargetdown = Column('weeklyexpirytargetdown', Integer)
   trend15m = Column('trend15m', Integer)
   maxpaindirection  = Column('maxpaindirection', Integer)
   maxpaintarget  = Column('maxpaintarget', Integer)
   pcrdirection  = Column('pcrdirection', Integer)
   pcrup  = Column('pcrup', Integer)
   pcrdown  = Column('pcrdown', Integer)
engine=create_engine("mysql://Mercury:Mercury@1234@104.211.223.42/optionspakshidev")
Base.metadata.create_all(engine)