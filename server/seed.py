from config import app

from models import db, Companies, Open_Positions, Contact, Linkedin

if __name__ == '__main__':
    with app.app_context():

        print("deleting tables...")

        Companies.query.delete()
        Open_Positions.query.delete()
        Contact.query.delete()
        Linkedin.query.delete()

        db.session.commit()

        print("creating companies...")

        companies = [
            Companies(
                name="Abridge",
                amount_of_employees="11-50",
                total_open_positions=3
            ),
            Companies(
                name="Spiral",
                amount_of_employees="11-50",
                total_open_positions=3
            ),
            Companies(
                name="Orum",
                amount_of_employees="51-200",
                total_open_positions=2
            )
        ]

        db.session.add_all(companies)
        db.session.commit()

        op = [
            Open_Positions(
                company_id=companies[0].id,
                hiring_contact=1,
                position_title="Lead Data Engineer",
                salary_range="$190k - $220k"
            ),
            Open_Positions(
                company_id=companies[0].id,
                hiring_contact=1,
                position_title="Senior Platform Engineer",
                salary_range="$175k - $205k"
            ),
            Open_Positions(
                company_id=companies[0].id,
                hiring_contact=1,
                position_title="Senior Platform Engineer",
                salary_range="$175k - $205k"
            ),
        ]
