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

    open_positions = db.relationship("Open_Positions", back_populates="companies", cascade="all,delete")

    @validates("name")
    def validate_name(self, key, val):
        if len(val) <= 0:
            raise ValueError
        elif not type(val) == str:
            raise ValueError
        else:
            return val
        
    @validates("amount_of_employees")
    def validate_amount_of_employees(self, key, val):
        if len(val) <= 0:
            raise ValueError
        elif not type(val) == str:
            raise ValueError
        else:
            return val
        
    @validates("total_open_positions")
    def validate_total_open_positions(self, key, val):
        if not type(val) == int:
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

    @validates("company_id")
    def validate_company_id(self, key, val):
        if not type(val) == int:
            raise ValueError
        else:
            return val
        
    @validates("hiring_contact")
    def validate_hiring_contact(self, key, val):
        if not type(val) == int:
            raise ValueError
        else:
            return val
        
    @validates("position_title")
    def validate_position_title(self, key, val):
        if len(val) <= 0:
            raise ValueError
        elif not type(val) == str:
            raise ValueError
        else:
            return val
        
    @validates("salary_range")
    def validate_salary_range(self, key, val):
        if len(val) <= 0:
            raise ValueError
        if not type(val) == str:
            raise ValueError
        else:
            return val


class Contact(db.Model, SerializerMixin):
    __tablename__ = "contact"

    serialize_rules = ("-open_positions.contacts", "-linkedin.contacts")

    id = db.Column(db.Integer, primary_key=True)
    linkedin_id = db.Column(db.Integer, db.ForeignKey("linkedin.id"))
    name = db.Column(db.String)
    position = db.Column(db.String)

    open_positions = db.relationship("Open_Positions", back_populates="contacts", cascade="all,delete")
    linkedin = db.relationship("Linkedin", back_populates="contacts")

    @validates("linkedin_id")
    def validate_linkedin_id(self, key, val):
        if not type(val) == int:
            raise ValueError
        else:
            return val
        
    @validates("name")
    def validate_name(self, key, val):
        if not type(val) == str:
            raise ValueError
        elif len(val) <= 0:
            raise ValueError
        else:
            return val
        
    @validates("positions")
    def validate_position(self, key, val):
        if not type(val) == str:
            raise ValueError
        if len(val) <= 0:
            raise ValueError
        else:
            return val


class Linkedin(db.Model, SerializerMixin):
    __tablename__ = "linkedin"

    serialize_rules = ("-contacts.linkedin", )

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String, nullable=False)
    length_of_position = db.Column(db.String)

    contacts = db.relationship("Contact", back_populates="linkedin", cascade="all,delete")

    @validates("url")
    def validate_url(self, key, val):
        if not type(val) == str:
            raise TypeError
        elif len(val) <= 0:
            raise TypeError
        else:
            return val

    @validates("length_of_position")
    def validate_length_of_position(self, key, val):
        if not type(val) == str:
            raise ValueError
        elif len(val) <= 0:
            raise TypeError
        else:
            return val