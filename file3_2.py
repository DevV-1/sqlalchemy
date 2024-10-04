#adding users (creating objects)

from sqlalchemy.orm import sessionmaker
from file3_1 import User, engine, Session
from datetime import datetime


#creating session
session = Session(bind=engine)

#creating objects 
# user1 = User(id = 11, uname= "Mike",email="abc@gmail.com")  #default value will be considered here
# user2 = User(12, "Anna", "bcd@gmail.com", datetime.strptime('13/12/12', '%d/%m/%y'))
# user3 = User(13, "Bob", "cde@gmail.com", datetime.strptime('14/12/12', '%d/%m/%y'))
# user4 = User(14, "Angela", "def@gmail.com", datetime.strptime('15/12/12', '%d/%m/%y'))

# session.add_all([user1,user2,user3, user4])
# session.commit()

#adding another object
# user5 = User(15, "Jack", "efg@gmail.com", datetime.strptime('16/12/12', '%d/%m/%y'))
# session.add(user5)
# session.commit()

user6 = User(16, "Vink", "fgh@gmail.com", datetime.strptime('17/12/12', '%d/%m/%y'))
session.add(user6)
session.commit()