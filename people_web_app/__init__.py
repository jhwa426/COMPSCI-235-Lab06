from flask import Flask, request, url_for
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # this creates the SQLAlchemy database instance.

def create_app():
    app = Flask(__name__)

    # Configure the app from configuration-file settings.
    app.config.from_object('config.Config')

    import people_web_app.adapters.repository as repo

    if app.config['REPOSITORY'] == 'memory':
        from people_web_app.domain.model import Person

        repo.repo_instance = repo.PeopleRepository(
            Person(74633, 'Julius', 'Caeser'),
            Person(88337, 'Genghis', 'Khan'),
            Person(92731, 'Winston', 'Churchill'),
            Person(12826, 'Mahatma', 'Ghandi'),
            Person(92213, 'Nelson', 'Mandela')
        )

    elif app.config['REPOSITORY'] == 'database':
        db.init_app(app)
        from people_web_app.domain.model import PersonDB as Person
        app.app_context().push()
        print(db.engine.table_names())
        if len(db.engine.table_names()) == 0:
            print("POPULATING DATABASE")
            db.create_all()
            person_1 = Person(id_number=74633, firstname='Julius', lastname='Caeser')
            person_2 = Person(id_number=88337, firstname='Genghis', lastname='Khan')
            person_3 = Person(id_number=92731, firstname='Winston', lastname='Churchill')
            person_4 = Person(id_number=12826, firstname='Mahatma', lastname='Ghandi')
            person_5 = Person(id_number=92213, firstname='Nelson', lastname='Mandela')
            db.session.add(person_1)
            db.session.add(person_2)
            db.session.add(person_3)
            db.session.add(person_4)
            db.session.add(person_5)
            db.session.commit()

        people = Person.query.all()

        repo.repo_instance = repo.DatabaseRepository()
        repo.repo_instance.update_repo()



    with app.app_context():
        from .people_blueprint import people
        app.register_blueprint(people.people_blueprint)

    return app