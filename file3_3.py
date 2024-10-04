#####queries
# from file3_1 import User, Session, engine
# from sqlalchemy import desc

# session = Session(bind=engine)

# user = session.query(User).all()
# # for user in users:
# #     print(user)
# print(user)

# results = session.query(User).filter(User.unname == "Anna")
# for r in results:
#     print(r)

# #will return all values where An is present in fname
# results = session.query(User).filter(User.unname.like("%An%"))
# for r in results:
#     print(r)

# #will return all values where An is present in fname (first occurence)
# results = session.query(User).filter(User.unname.like("%An%")).first()
# print(results)

# results = session.query(User).filter(User.id > 14)
# for r in results:
#     print(r)

# #will select all values where fname is Anna, Blue,or Mike
# results = session.query(User).filter(User.unname.in_(["Anna", "Jack", "Mike"]))
# for r in results:
#     print(r)

# #updating data
# up_user = session.query(User).filter(User.unname=='Vink').first()
# up_user.unname = 'Devgan'
# up_user.id = 18
# session.commit()

# #deleting a data
# del_user = session.query(User).filter(User.unname=='Devgan').first()
# session.delete(del_user)
# session.commit()

# #deleting a data
# session.query(User).filter(User.unname=='Jack').delete()
# session.commit()

# #order
# users_asc = session.query(User).order_by(User.unname).all()
# users_desc = session.query(User).order_by(desc(User.unname)).all()
# for u in users_desc:
#     print(u)

