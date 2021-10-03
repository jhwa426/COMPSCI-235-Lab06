from people_web_app import db

class Person:
    def __init__(self, id_number: int, firstname: str, lastname: str):
        self._id_number = id_number
        self._firstname = firstname
        self._lastname = lastname

    @property
    def id_number(self) -> int:
        return self._id_number

    @property
    def firstname(self) -> str:
        return self._firstname

    @property
    def lastname(self) -> str:
        return self._lastname


class PersonDB(db.Model):
    id_number = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(255), nullable=False)
    lastname = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"Person: ('{self.id_number}', '{self.firstname}', '{self.lastname}')"