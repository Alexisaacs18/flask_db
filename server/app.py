from config import app
from flask import make_response

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


if __name__ == '__main__':
    app.run(port=5555, debug=True)
