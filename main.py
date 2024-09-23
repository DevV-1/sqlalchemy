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
        self.lname=last
        self.gender=gender
        self.age=age

    def __repr__(self): # returns a string representation of an object
        return f"({self.ssn} {self.fname} {self.lname} {self.gender} {self.age})" 
    
class Thing(Base):
    __tablename__ = "things"

    tid = Column("tid", Integer, primary_key=True)
    desc = Column("desc", String)
    owner = Column("owner", ForeignKey("people.ssn"))

    def __init__(self, tid, description, owner):
        self.tid = tid
        self.desc = description
        self.owner = owner

    def __repr__(self):
        return f"({self.tid} {self.desc} owned by {self.owner})"
    

#making engine
engine = create_engine("sqlite:///mydb.db", echo = True)
Base.metadata.create_all(bind=engine)  #will transfer data into db table format and create mydb.db file

#creating session
Session = sessionmaker(bind=engine)
session = Session()

#creating objects
# person1 = Person(12312, "Mike", "Smith", "m", 23)
# person2 = Person(21213, "Anna", "Blue", "f", 25)
# person3 = Person(32132, "Bob", "White", "m", 26)
# person4 = Person(31231, "Angela", "Cold", "f", 43)

# #adding to session
# session.add(person1)
# session.add(person2)
# session.add(person3)
# session.add(person4)

#adding together
# session.add([person1, person2])

# session.commit()


#queries
#return all persons
# results = session.query(Person).all()
# print(results)

# results = session.query(Person).filter(Person.lname == "Blue")
# for r in results:
#     print(r)

# #will return all values where An is present in fname
# results = session.query(Person).filter(Person.fname.like("%An%"))
# for r in results:
#     print(r)

# results = session.query(Person).filter(Person.age > 30)
# for r in results:
#     print(r)

# #will select all values where fname is Anna, Blue,or Mike
# results = session.query(Person).filter(Person.fname.in_(["Anna", "Blue", "Mike"]))
# for r in results:
#     print(r)

# #printing an object
# print(repr(person2))


# #creating second table
    
# t1 = Thing(1, "laptop", person1.ssn)
# t2 = Thing(2, "mouse", person2.ssn)
# t3 = Thing(3, "keys", person3.ssn)
# t4 = Thing(4, "car", person1.ssn)
# t5 = Thing(5, "hi", person4.ssn)

# session.add_all([t1,t2,t3,t4,t5])
# session.commit()

results = session.query(Thing, Person).filter(Thing.owner == Person.ssn).filter(Person.fname == "Anna")
for r in results:
    print(r)