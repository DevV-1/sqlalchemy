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

    id = Column("id", Integer, primary_key = True)
    uname = Column("uname",String(25), nullable = False)
    age = Column("age",String, default = 'a@gmail.com')
    date = Column("date", Date(), default=datetime.utcnow) #just date
    # date = Column("date", DateTime(), default=datetime.utcnow) #time as well

    def __init__(self, id, uname, age=None, date=None):
        self.id = id
        self.uname = uname
        self.age = age
        self.date = date

    def __repr__(self):
        return f'{self.id} {self.uname} {self.age} on {self.date}'

#making engine
engine = create_engine("sqlite:///database/db3.db", echo = True)
Base.metadata.create_all(bind=engine)  #will transfer data into db table format and create db3.db file

#creating session
Session = sessionmaker(bind=engine)
session = Session()