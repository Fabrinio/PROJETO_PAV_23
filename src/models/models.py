from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy

Base = declarative_base()
db = SQLAlchemy()

class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(60), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String(12), nullable=False)
    height = Column(Float, nullable=False)
    weight = Column(Float, nullable=False)

    user_exercises = relationship('User_Exercises', back_populates='user')

    def __init__(self, name, age, gender, height, weight):

        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight


class Exercises(Base):
    __tablename__ = 'exercises'
    __table_args__ = {'extend_existing': True}

    exercise_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(60), nullable=False)
    description = Column(String(255), nullable=False)
    dificulty = Column(Integer, nullable=False)
    muscular_groups = Column(String(45), nullable=False)

    user_exercises = relationship('User_Exercises', back_populates='exercise')

    def __init__(self, name, description, dificulty, muscular_groups):

        self.name = name
        self.description = description
        self.dificulty = dificulty
        self.muscular_groups = muscular_groups


class User_Exercises(Base):
    __tablename__ = 'user_exercises'
    __table_args__ = {'extend_existing': True}

    user_exercises_id = Column(Integer, primary_key=True, autoincrement=True)
    id_user = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    id_exercise = Column(Integer, ForeignKey('exercises.exercise_id'), nullable=False)
    date = Column(Date)
    duration = Column(Float)
    weight = Column(Float)
    repetitions = Column(Integer)

    user = relationship("User", back_populates="user_exercises")
    exercise = relationship("Exercises", back_populates="user_exercises")

    def __init__(self, id_user, id_exercises, date, duration, weight, repetitions):

        self.id_user = id_user
        self.id_exercises = id_exercises
        self.date = date
        self.duration = duration
        self.weight = weight
        self.repetitions = repetitions


engine = create_engine('postgresql://postgres:#LFls1412@localhost:5432/PROJETO_PAV2023')
Base.metadata.create_all(engine)