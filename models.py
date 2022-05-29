from datetime import datetime
from typing import Sequence
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Time
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    updated_at = Column(Time, default=datetime.now().time())
    created_at = Column(Time, default=datetime.now().time())
    is_active = Column(Boolean, default=True)

    records = relationship("Record", back_populates="user")


class Record(Base):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True, index=True)
    inputday = Column(Time)
    value = Column(Integer)
    updated_at = Column(Time, default=datetime.now().time())
    created_at = Column(Time, default=datetime.now().time())
    memo = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    tag_id = Column(Integer, ForeignKey("tags.id"))

    user = relationship("User", back_populates="records")
    tag = relationship("Tag", back_populates="records")


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    tag_name = Column(String, unique=True, index=True)
    unit = Column(String)
    updated_at = Column(Time, default=datetime.now().time())
    created_at = Column(Time, default=datetime.now().time())

    records = relationship("Record", back_populates="tag")
