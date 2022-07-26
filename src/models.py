import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    UserName = Column(String(100), unique=True, nullable=False)
    FirstName = Column(String(50), unique=True, nullable=False)
    LastName = Column(String(50),)
    Email = Column(String(50), unique=True, nullable=False)

class Favorite_Vehicle(Base):
    __tablename__ = 'Favorite_Vehicle'
    Userid = Column(String(100), ForeignKey('User.id'), nullable=False, primary_key=True)
    Vehicleid = Column(Integer, ForeignKey('Vehicle.id') )

class Favorite_People(Base):
    __tablename__ = 'Favorite_People'
    Userid = Column(String(100), ForeignKey('User.id'), nullable=False, primary_key=True)
    Peopleid = Column(Integer, ForeignKey('People.id'), unique=True, nullable=False)

class Favorite_Planets(Base):
    __tablename__ = 'Favorite_Planets'
    Userid = Column(String(100), ForeignKey('User.id'), nullable=False, primary_key=True)
    Planetsid = Column(Integer, ForeignKey('Planets.id'))
    
class Vehicle(Base):
    __tablename__ = 'Vehicle'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    Name = Column(String(250), nullable=False)
    Model = Column(String(250))
    Manufacturer = Column(String(250), nullable=False)
    CostInCredits = Column(Integer)
    Length = Column(Integer)
    max_atmosphering_speed = Column(Integer, unique=True, nullable=False)
    Crew = Column(Integer, unique=True, nullable=False)
    Passengers = Column(Integer, unique=True, nullable=False)
    cargo_capacity = Column(Integer, unique=True, nullable=False)
    Consumables = Column(String(100), unique=True, nullable=False)
    vehicle_class = Column(String(100), unique=True, nullable=False)
    Pilots = Column(String(100), unique=True, nullable=False)

class People(Base):
    __tablename__ = 'People'
    id = Column(Integer, primary_key=True)
    Name = Column(String(250), nullable=False)
    Heigth = Column(Integer) 
    Mass = Column(Integer)
    HairColor = Column(String(250), nullable=False)
    SkinColor = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    Birth_Year = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)

class Planets(Base):
    __tablename__ = 'Planets'
    ID = Column(Integer, primary_key=True)
    Name = Column(String(250), nullable=False)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    diamneter = Column(Integer)
    Climate = Column(String(250), nullable=False)
    Gravity = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    surface_water = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False) 
    Residents = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')