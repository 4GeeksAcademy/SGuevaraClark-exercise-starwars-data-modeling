import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'username': self.username
        }

class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    height = Column(String)
    mass = Column(String)
    hair_color = Column(String)
    skin_color = Column(String)
    birth_year = Column(String)
    gender = Column(String)
    home_planet_id = Column(Integer, ForeignKey('planets.id'))
    planet = relationship('Planet', backref='residents')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'height': self.height,
            'mass': self.mass
        }

class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    rotation_period = Column(String)
    orbital_period = Column(String)
    diameter = Column(String)
    climate = Column(String)
    terrain = Column(String)
    population = Column(String)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'climate': self.climate,
            'population': self.population
        }

class Starship(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    model = Column(String)
    length = Column(String)
    crew = Column(String)
    passengers = Column(String)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'model': self.model,
            'manufacturer': self.manufacturer
        }

class Favorite(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', backref='favorites')
    character_id = Column(Integer, ForeignKey('characters.id'))
    character = relationship('Character')
    planet_id = Column(Integer, ForeignKey('planets.id'))
    planet = relationship('Planet')
    starship_id = Column(Integer, ForeignKey('starships.id'))
    starship = relationship('Starship')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'character_id': self.character_id,
            'planet_id': self.planet_id,
            'starship_id': self.starship_id
        }

try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem generating the diagram")
    raise e