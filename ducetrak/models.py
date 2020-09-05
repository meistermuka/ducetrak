from sqlalchemy import Column, Integer, String
from ducetrak.db import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(32), index=True, unique=True)
    email = Column(String(255), index=True, unique=True)
    password = Column(String(128))
    first_name = Column(String(255))
    last_name = Column(String(255))

    def __repr__(self):
        return f'<User {self.username}>'
