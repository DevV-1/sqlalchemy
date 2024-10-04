from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, DateTime, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

"""
class User
    id int
    username str
    email str
    date_created datetime
"""

class User(Base):
    __tablename__ = 'users'

    id = Column("id",Integer, primary_key = True)
    unname = Column("unname",String(25), nullable = False)
    email = Column("email",String)
    date = Column("date", Date(), default=datetime.utcnow) #just date
    # date = Column("date", DateTime(), default=datetime.utcnow) #time as well

    def __init__(self, id, uname, email, date=None):
        self.id = id
        self.unname = uname
        self.email = email
        self.date = date

    def __repr__(self):
        return f'{self.id} {self.unname} {self.email} on {self.date}'
    

#making engine
engine = create_engine("sqlite:///database/db3.db", echo = True)
Base.metadata.create_all(bind=engine)  #will transfer data into db table format and create mydb.db file

#creating session
Session = sessionmaker(bind=engine)
session = Session()