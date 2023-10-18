from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy import Date
import re

from config import bcrypt, db

class User(db.Model, SerializerMixin):
    __tablename__ = 'users' 

    id = db.Column(db.Integer, primary_key = True)
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, )
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.Integer)
    username = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    _password_hash = db.Column(db.String, nullable=False)
    image = db.Column(db.String)

    #ASSOCIATION PROXY
    #one user has many goals THROUGH UserGoals
    goals = association_proxy(
        "user_goals", "goal"
    )

class UserGoal(db.Model, SerializerMixin):
    __tablename__ = 'user_goals'

    id = db.Column(db.Integer, primary_key = True)
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    goals_id = db.Column()
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    goal_id = db.Column(db.Integer, db.ForeignKey('goals.id'))


    user = db.relationship('User', backref='user_goals')
    goal = db.relationship('Goal', backref='user_goals')
    serialize_rules = ('-user', 'goal',)











class Goal(db.Model, SerializerMixin):
    __tablename__ = "goals"
    
    id = db.Column(db.Integer, primary_key = True)

    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, server_default = db.func.now())
    date = db.Column(db.DateTime, server_default = db.func.now())

    goal_name = db.Column(db.String)
    goal_def = db.Column(db.String)

    #FOREIGN KEY
    data_type_id = db.Column(db.Integer, db.ForeignKey("data_types.id"))



    #RELATIONSHIP
    #one goal has many users
    #one goal has many data_types; many data types have one goal
    data_types = db.relationship(
        "DataType", back_populates="goals")

  



    #SERIALIZE RULES


    #VALIDATION


class DataType(db.Model, SerializerMixin):
    __tablename__ = "data_types"
    
    id = db.Column(db.Integer, primary_key = True)

    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, server_default = db.func.now())

    frequency = db.Column(db.Integer)
    duration = db.Column(db.Integer)
    rating_scale = db.Column(db.Integer)
    latency = db.Column(db.Integer)
    abc_data = db.Column(db.String)

    #RELATIONSHIP
    ##one goal has many data_types; many data types have one goal
    data_types = db.relationship(
        "Goal", back_populates="data_types")

    #ASSOCIATION PROXY


    #SERIALIZE RULES


    #VALIDATION    
    

