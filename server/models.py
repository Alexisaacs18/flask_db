from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

db = SQLAlchemy()


class Companies(db.Model, SerializerMixin):
    __tablename__ = "companies"

    serialize_rules = ("-open_positions.companies", )

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    amount_of_employees = db.Column(db.String)
    total_open_positions = db.Column(db.Integer)

    open_positions = db.relationship(
        "Open_Positions", back_populates="companies", cascade="all,delete")

    @validates("companies")
    def validate_company(self, key, val):
        if len(val) <= 0:
            raise ValueError
        else:
            return val


class Open_Positions(db.Model, SerializerMixin):
    __tablename__ = "open_positions"

    serialize_rules = ("-companies.open_positions", "-contacts.open_positions")

    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey("companies.id"))
    hiring_contact = db.Column(db.Integer, db.ForeignKey("contact.id"))
    position_title = db.Column(db.String)
    salary_range = db.Column(db.String)

    companies = db.relationship("Companies", back_populates="open_positions")
    contacts = db.relationship("Contact", back_populates="open_positions")


class Contact(db.Model, SerializerMixin):
    __tablename__ = "contact"

    serialize_rules = ("-open_positions.contacts", "-linkedin.contacts")

    id = db.Column(db.Integer, primary_key=True)
    linkedin_id = db.Column(db.Integer, db.ForeignKey("linkedin.id"))
    name = db.Column(db.String)
    position = db.Column(db.String)

    open_positions = db.relationship(
        "Open_Positions", back_populates="contacts", cascade="all,delete")
    linkedin = db.relationship("Linkedin", back_populates="contacts")


class Linkedin(db.Model, SerializerMixin):
    __tablename__ = "linkedin"

    serialize_rules = ("-contacts.linkedin", )

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String, nullable=False)
    length_of_position = db.Column(db.String)

    contacts = db.relationship(
        "Contact", back_populates="linkedin", cascade="all,delete")
