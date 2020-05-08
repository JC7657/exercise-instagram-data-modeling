import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False, unique=True)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    bio = Column(String(250))
    posts = relationship('Post', backref='user', lazy=True)
    stories = relationship('Story')

class Post(Base):
    __tablename__ = 'posts'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    image = Column(String(250), nullable=False)
    likes = Column(Integer, nullable=False)
    description = Column(String(250))
    comments = relationship('Comment')
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    content = Column(String(250), nullable=False)
    likes = Column(Integer)
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

class Story(Base):
    __tablename__ = 'stories'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    creation_time = Column(DateTime, default=datetime.now(), nullable=False)
    views = Column(Integer, nullable=False)
    isHighlighted = Column(Boolean, default=False)
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')