from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()


class Companies(db.Model, SerializerMixin):
    __tablename__ = "companies"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    amount_of_employees = db.Column(db.String)
    total_open_positions = db.Column(db.Integer)


class Open_Positions(db.Model, SerializerMixin):
    __tablename__ = "open_positions"

    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey("companies.id"))
    hiring_contact = db.Column(db.Integer, db.ForeignKey("contact.id"))
    position_title = db.Column(db.String)
    salary_range = db.Column(db.String)


class Contact(db.Model, SerializerMixin):
    __tablename__ = "contact"

    id = db.Column(db.Integer, primary_key=True)
    linkedin_id = db.Column(db.Integer, db.ForeignKey("linkedin.id"))
    name = db.Column(db.String)
    position = db.Column(db.String)


class Linkedin(db.Model, SerializerMixin):
    __tablename__ = "linkedin"

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String, nullable=False)
    length_of_position = db.Column(db.Integer)
