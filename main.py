from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://sys:51@127.0.0.1:3306/python")

Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    age = Column(Integer)


session = sessionmaker()
session.configure(bind=engine)

s = session()

# insert
a = User(id=2, name='fuck', age=24)
s.add(a)
a = User(id=5, name='kb', age=8)
s.add(a)
s.commit()

# select
ret = s.query(User).filter(User.id > 1).all()
for user in ret:
    print(user.name)

# update
s.query(User).filter(User.name == 'fuck').update({User.age: User.age + 1})
s.commit()

# delete
s.query(User).filter(User.name == 'fuck').delete()
s.commit()

s.close()
