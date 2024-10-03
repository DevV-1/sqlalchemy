from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, DateTime
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
    unname = Column("unname",String(25), nullable = False, unique=True)
    email = Column("email",String, unique=True)
    date = Column("date", DateTime(), default=datetime.utcnow)

    def __init__(self, id, uname, email, date):
        self.id = id
        self.unname = uname
        self.email = email
        self.date = date

    def __repr__(self):
        return f'{self.id} {self.uname} {self.email} on {self.date}'
    
#making engine
engine = create_engine("sqlite:///database/db3.db", echo = True)
Base.metadata.create_all(bind=engine)  #will transfer data into db table format and create mydb.db file

#creating session
Session = sessionmaker(bind=engine)
session = Session()

#creating objects
user1 = User(1, "Mike","abc@gmail.com", datetime.strptime('12/12/12', '%d/%m/%y') )
user2 = User(2, "Anna", "bcd@gmail.com", datetime.strptime('13/12/12', '%d/%m/%y'))
user3 = User(3, "Bob", "cde@gmail.com", datetime.strptime('14/12/12', '%d/%m/%y'))
user4 = User(4, "Angela", "def@gmail.com", datetime.strptime('15/12/12', '%d/%m/%y'))

session.add_all([user1,user2,user3, user4])
session.commit()