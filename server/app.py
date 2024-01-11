from config import app
from flask import make_response, request

from models import db, Companies, Open_Positions, Contact, Linkedin


@app.route("/companies", methods=["GET"])
def companies():
    companies = Companies.query.all()

    companies_dict = [company.to_dict() for company in companies]

    response = make_response(
        companies_dict,
        200
    )

    return response


@app.route("/open_positions", methods=["GET"])
def open_positions():
    open_positions = Open_Positions.query.all()

    open_positions_dict = [open_position.to_dict()
                           for open_position in open_positions]

    response = make_response(
        open_positions_dict,
        200
    )

    return response


@app.route("/contacts", methods=["GET"])
def contact():
    contacts = Contact.query.all()

    contacts_dict = [contact.to_dict() for contact in contacts]

    response = make_response(
        contacts_dict,
        200
    )

    return response


@app.route("/linkedin", methods=["GET"])
def linkedin():
    linkedin_for_contacts = Linkedin.query.all()

    linkedin_dict = [contact_linkedin.to_dict()
                     for contact_linkedin in linkedin_for_contacts]

    response = make_response(
        linkedin_dict,
        200
    )

    return response


@app.route("/companies/<int:id>", methods=["GET", "DELETE"])
def companies_id(id):
    companies_id = Companies.query.filter(Companies.id == id).first()

    if companies_id:
        if request.method == "GET":
            companies_id_dict = companies_id.to_dict()

            response = make_response(
                companies_id_dict,
                200
            )

        elif request.method == "DELETE":
            db.session.delete(companies_id)
            db.session.commit()

            response = make_response(
                {},
                202
            )
    else:
        response = make_response(
            {"error": "ID does not exist"},
            404
        )

    return response


if __name__ == '__main__':
    app.run(port=5555, debug=True)
