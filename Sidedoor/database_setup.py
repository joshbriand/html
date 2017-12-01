from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Admin(Base):
    __tablename__ = 'admin'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    position = Column(String(250), nullable=False)
    city = Column(String(250), nullable=False)
    province = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    bio = Column(String(1000), nullable=False)
    facebook = Column(String(250))
    twitter = Column(String(250))
    instagram = Column(String(250))


class Host(Base):
    __tablename__ = 'host'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    address = Column(String(500), nullable=False)
    city = Column(String(250), nullable=False)
    province = Column(String(250), nullable=False)
    capacity = Column(Integer, nullable=False)
    phone = Column(String(250), nullable=False)
    bio = Column(String(1000), nullable=False)
    facebook = Column(String(250))
    twitter = Column(String(250))
    instagram = Column(String(250))
    email = Column(String(250), nullable=False)


class Artist(Base):
    __tablename__ = 'artist'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    website = Column(String(500), nullable=False)
    video = Column(String(250), nullable=False)
    audio = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    phone = Column(String(250), nullable=False)
    bio = Column(String(1000), nullable=False)
    facebook = Column(String(250))
    twitter = Column(String(250))
    instagram = Column(String(250))


class Guest(Base):
    __tablename__ = 'guest'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    phone = Column(String(250), nullable=False)
    bio = Column(String(1000), nullable=False)
    facebook = Column(String(250))
    twitter = Column(String(250))
    instagram = Column(String(250))


class Show(Base):
    __tablename__ = 'show'

    id = Column(Integer, primary_key=True)
    host = relationship(Host)
    artist = relationship(Artist)
    date = Column(DateTime)


class Ticket(Base):
    __tablename__ = 'ticket'

    id = Column(Integer, primary_key=True)
    show = relationship(Show)
    guest = relationship(Guest)
    quantity = Column(Integer)


class Rating(Base):
    __tablename__ = 'rating'

    id = Column(Integer, primary_key=True)

engine = create_engine('sqlite:///sidedoor.db')


Base.metadata.create_all(engine)
