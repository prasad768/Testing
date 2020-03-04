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
   maxpainTarget  = Column('maxpaintarget', Integer)
   pcrUp  = Column('pcrUp', Integer)
engine=create_engine("mysql://Mercury:Mercury@1234@104.211.223.42/optionspakshidev")
Base.metadata.create_all(engine)