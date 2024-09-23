from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()  #making a base declarative class

class Person(Base):
    __tablename__ = 'people'  #using dec class to create a table

    #declaring table variables
    ssn = Column("ssn" , Integer, primary_key=True)
    fname = Column("fname" , String)
    lname = Column("lname" , String)
    gender = Column("gender" , CHAR)
    age = Column("age" , Integer)

    #initializing class propeties
    def __init__(self, ssn, first, last, gender, age):
        self.ssn=ssn
        self.fname=first
        self.last=last
        self.gender=gender
        self.age=age

    def __repr__(self): # returns a string representation of an object
        return f"({self.ssn} {self.name} {self.gender} {self.age})" 
    
#making engine
engine = create_engine("sqlite:///mydb.db", echo = True)
Base.metadata.create_all(bind=engine)

