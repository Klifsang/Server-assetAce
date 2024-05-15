from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from ..app import db

class Employee(db.Model, SerializerMixin):
    __tablename__ = 'employees'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    department = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(20), unique=True)
    phonenumber = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    # role
    
    
    # requests = db.relationship("Requests", backref="employee")
# Table Employee {
#   id integer
#   username varchar
#   department varchar
#   address varchar
#   phonenumber varchar
# }