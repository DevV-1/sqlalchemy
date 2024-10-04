#######creating tables customer and invoice

from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()  #making a base declarative class

class Customer(Base):
    __tablename__ = 'customer'  #using dec class to create a table

    #declaring table variables
    id = Column("id" , Integer, primary_key=True)
    fname = Column("fname" , String)
    lname = Column("lname" , String)
    company = Column("company" , String)
    city = Column("city" , String)
    state = Column("state" , String)
    postal_code = Column("postal_code" , String)

    #initializing class propeties
    def __init__(self, id, first, last, company, city, state, postal_code):
        self.id=id
        self.fname=first
        self.lname=last
        self.company=company
        self.city=city
        self.state=state
        self.postal_code=postal_code

    def __repr__(self): # returns a string representation of an object
        return f"({self.id} {self.fname} {self.lname} {self.company} {self.city} {self.state} {self.postal_code})" 
    
class Invoice(Base):
    __tablename__ = "invoice"

    id = Column("id", Integer, primary_key=True)
    customer_id = Column("customer_id", Integer())
    billing_adress = Column("billing_adress", String())
    total = Column("total", Integer())

    def __init__(self, id, customer_id, billing_adress, total):
        self.id = id
        self.customer_id = customer_id
        self.billing_adress = billing_adress
        self.total = total

    def __repr__(self):
        return f"({self.id} {self.customer_id} {self.billing_adress} {self.total})"
    

#making engine
engine = create_engine("sqlite:///database/db2.db", echo = True)
Base.metadata.create_all(bind=engine)  #will transfer data into db table format and create mydb.db file

#creating session
Session = sessionmaker(bind=engine)
session = Session()

#creating objects
c1 = Customer(1, "Mike", "Smith", "CompA", "CityA", "StateA", 1221)
c2 = Customer(2, "Anna", "Blue", "CompB", "CityB", "StateB", 1212)
c3 = Customer(3, "Bob", "White", "CompC", "CityC", "StateC", 2121)
c4 = Customer(4, "Angela", "Cold", "CompA", "CityA", "StateA", 1221)
c5 = Customer(5, "Angela", "Cold", "CompC", "CityB", "StateQ", 3434)
c6 = Customer(6, "Angela", "Cold", "CompA", "CityC", "StateW", 4343)

# #adding to session
# session.add(c1)
# session.add(c2)
# session.add(c3)
# session.add(c4)
# or
session.add_all([c1,c2,c3,c4,c5,c6])

#creating invoice table objects
i1 = Invoice(1, c1.id, 'ABC', 212)
i2 = Invoice(2, c2.id, 'BCD', 21)
i3 = Invoice(3, c3.id, 'ABC', 12)
i4 = Invoice(3, c3.id, 'WED', 1)
i5 = Invoice(4, c4.id, 'QWE', 312)
i6 = Invoice(4, c4.id, 'SDF', 22)
i7 = Invoice(2, c2.id, 'YUI', 27)
i8 = Invoice(2, c2.id, 'POI', 42)

session.add_all([i1,i2,i3,i4,i5,i6,i7,i8])

#printing few
print(c1,i2,i4,c3)
