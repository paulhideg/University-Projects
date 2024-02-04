from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from flask_marshmallow import Marshmallow

#init db
db = SQLAlchemy()
marshmallow = Marshmallow()

"""
    Create the model:
        add columns with db.Column(type)
        type can be db.Integer, db.String(lenght)

    e.g.:

    class Person(db.Model):
        id = db.Column(db.Integer, primary_key = True)
        name = db.Column(db.String(100))
        is_hired = db.Column(db.Boolean)
"""

class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))


class Admin(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))

class SessionID(db.Model):
    # we need this because sqlite autoincrements the primary key
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(128)) # length of sha512

    # depending on the role either User or Admin
    person_id = db.Column(db.Integer)
    role = db.Column(db.String(5)) # "user" | "admin"

    # used for checking if the session is expired
    timestamp = db.Column(db.Float)

class Destination(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(100))
    image = db.Column(db.String(500)) # link to the image
    geolocation = db.Column(db.String(100))
    start_date = db.Column(db.String(100))
    end_date = db.Column(db.String(100))

class DestinationSchema(marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model = Destination

class PublicList(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    destination_id = db.Column(db.Integer, ForeignKey(Destination.id))

class BucketList(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    user_id = db.Column(db.Integer, ForeignKey(User.id))
    destination_id = db.Column(db.Integer, ForeignKey(Destination.id))

