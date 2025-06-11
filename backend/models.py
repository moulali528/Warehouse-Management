from database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique = True)
    username = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    hased_password = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(String)
    # address = Column(String)

class Todos(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True, index=True)
    task = Column(String)
    description = Column(String)
    status = Column(Boolean, default=False)
    is_deleted = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey("users.id"))
