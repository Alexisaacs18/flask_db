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
                amount_of_employees="1-10",
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

        linkedin = [
            Linkedin(
                url = "https://www.linkedin.com/in/katiebowles/",
                length_of_position = "4 Months"
            ),
            Linkedin(
                url = "https://www.linkedin.com/in/andrew-dilosa/",
                length_of_position = "5 Years"
            ),
            Linkedin(
                url = "https://www.linkedin.com/in/lixuan/",
                length_of_position = "4 Months"
            )
        ]

        db.session.add_all(linkedin)
        db.session.commit()

        contact = [
            Contact(
                linkedin_id = linkedin[0].id,
                name = "KB Bowles",
                position = "Senior Technical Recruiter"
            ),
            Contact(
                linkedin_id = linkedin[1].id,
                name = "Andrew DiLosa",
                position = "CTO"
            ),
            Contact(
                linkedin_id = linkedin[2].id,
                name = "Xuan L",
                position = "VP of Engineering"
            ),
        ]

        db.session.add_all(contact)
        db.session.commit()

        op = [
            Open_Positions(
                company_id=companies[0].id,
                hiring_contact=contact[0].id,
                position_title="Lead Data Engineer",
                salary_range="$190k - $220k"
            ),
            Open_Positions(
                company_id=companies[0].id,
                hiring_contact=contact[0].id,
                position_title="Senior Platform Engineer",
                salary_range="$175k - $205k"
            ),
            Open_Positions(
                company_id=companies[0].id,
                hiring_contact=contact[0].id,
                position_title="Senior Platform Engineer",
                salary_range="$175k - $205k"
            ),
            Open_Positions(
                company_id=companies[1].id,
                hiring_contact=contact[1].id,
                position_title="Principal Software Engineer",
                salary_range="$150k - $200k"
            ),
            Open_Positions(
                company_id=companies[1].id,
                hiring_contact=contact[1].id,
                position_title="Senior Software Engineer",
                salary_range="$130k - $170k"
            ),
            Open_Positions(
                company_id=companies[1].id,
                hiring_contact=contact[1].id,
                position_title="Senior Software Engineer - AI/ML",
                salary_range="$130k - $170k"
            ),
            Open_Positions(
                company_id=companies[2].id,
                hiring_contact=contact[2].id,
                position_title="Staff Software Engineer",
                salary_range="$200k - $220k"
            ),
            Open_Positions(
                company_id=companies[2].id,
                hiring_contact=contact[2].id,
                position_title="Staff Software Engineer (Canada)",
                salary_range="$200k - $220k"
            )
        ]

        db.session.add_all(op)
        db.session.commit()
