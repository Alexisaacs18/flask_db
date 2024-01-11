from config import app
from flask import make_response, request

from models import db, Companies, Open_Positions, Contact, Linkedin


@app.route("/companies", methods=["GET", "POST"])
def companies():

    if request.method == "GET":

        companies = Companies.query.all()

        companies_dict = [company.to_dict(rules = ("-open_positions", )) for company in companies]

        response = make_response(
            companies_dict,
            200
        )

    elif request.method == "POST":
            
        try:

            form_data = request.get_json()

            new_company = Companies(
                name = form_data['name'],
                amount_of_employees = form_data['amount_of_employees'],
                total_open_positions = form_data['total_open_positions']
            )

            db.session.add(new_company)
            db.session.commit()

            response = make_response(
                new_company.to_dict(),
                201
            )

        except ValueError:

            response = make_response(
                    {"Error": "Invalid Request"},
                    400
                )

    else:

        response = make_response(
            {"Error": "Invalid Method"},
            400
        )

    return response


@app.route("/open_positions", methods=["GET", "POST"])
def open_positions():

    if request.method == "GET":

        open_positions = Open_Positions.query.all()

        open_positions_dict = [open_position.to_dict(rules = ("-contacts", "-companies")) for open_position in open_positions]

        response = make_response(
            open_positions_dict,
            200
        )

    elif request.method == "POST":

        try:

            form_data = request.get_json()

            new_open_positions = Open_Positions(
                company_id = form_data["company_id"],
                hiring_contact = form_data["hiring_contact"],
                position_title = form_data["position_title"],
                salary_range = form_data["salary_range"]
            )

            db.session.add(new_open_positions)
            db.session.commit()

            response = make_response(
                new_open_positions.to_dict(),
                201
            )

        except ValueError:

            response = make_response(
                {"Error" : "Invalid Value"},
                400
            )

    else:

        response = make_response(
            {"Error" : "Invalid Method"},
            400
        )

    return response


@app.route("/contacts", methods=["GET", "POST"])
def contact():
    
    if request.method == "GET":

        contacts = Contact.query.all()

        contacts_dict = [contact.to_dict(rules = ("-open_positions", "-linkedin")) for contact in contacts]

        response = make_response(
            contacts_dict,
            200
        )

    elif request.method == "POST":

        try:

            form_data = request.get_json()

            new_contact = Contact(
                linkedin_id = form_data["linkedin_id"],
                name = form_data["name"],
                position = form_data["position"]
            )

            db.session.add(new_contact)
            db.session.commit()

            response = make_response(
                new_contact.to_dict(),
                201
            )

        except ValueError:

            response = make_response(
                {"Error" : "Invalid Format"},
                400
            )

    else:

        response = make_response(
            {"Error" : "Invalid Method"}
        )

    return response


@app.route("/linkedin", methods=["GET"])
def linkedin():
    linkedin_for_contacts = Linkedin.query.all()

    linkedin_dict = [contact_linkedin.to_dict() for contact_linkedin in linkedin_for_contacts]

    response = make_response(
        linkedin_dict,
        200
    )

    return response


@app.route("/companies/<int:id>", methods=["GET", "PATCH", "DELETE"])
def companies_id(id):
    companies_id = Companies.query.filter(Companies.id == id).first()

    if companies_id:
        if request.method == "GET":
            companies_id_dict = companies_id.to_dict()

            response = make_response(
                companies_id_dict,
                200
            )

        elif request.method == "PATCH":
            try:
                form_data = request.get_json()

                for key in form_data:
                    setattr(companies_id, key, form_data[key])

                db.session.commit()

                response = make_response(
                    companies_id.to_dict(),
                    201
                )

            except ValueError:

                response = make_response(
                    {"Error": "Invalid Request"},
                    400
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

@app.route("/open_positions/<int:id>", methods={"GET", "PATCH", "DELETE"})
def open_position_id(id):
    open_position_id = Open_Positions.query.filter(Open_Positions.id == id).first()

    if open_position_id:
        if request.method == "GET":

            response = make_response(
                open_position_id.to_dict(),
                200
            )

        elif request.method == "PATCH":

            try:
            
                form_data = request.get_json()

                for key in form_data:
                    setattr(open_position_id, key, form_data[key])

                db.session.commit()

                response = make_response(
                    open_position_id.to_dict(),
                    201
                )

            except ValueError:

                response = make_response(
                    {"Error" : "Invalid format"},
                    400
                )

        elif request.method == "DELETE":

            db.session.delete(open_position_id)
            db.session.commit()

            response = make_response(
                {},
                202
            )

    else:

        response = make_response(
            {"Error" : "Invalid ID"},
            404
        )

    return response



if __name__ == '__main__':
    app.run(port=5555, debug=True)
