import abc
from typing import List

from people_web_app.domain.model import Person, PersonDB

repo_instance = None


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def __iter__(self):
        raise NotImplementedError

    @abc.abstractmethod
    def __next__(self) -> Person:
        raise NotImplementedError

    @abc.abstractmethod
    def get_person(self, id: int):
        raise NotImplementedError


class PeopleRepository(AbstractRepository):
    def __init__(self, *args):
        self._people: List[Person] = list()

        for person in args:
            self._people.append(person)

    def __iter__(self):
        self._current = 0
        return self

    def __next__(self):
        if self._current >= len(self._people):
            raise StopIteration
        else:
            self._current += 1
            return self._people[self._current-1]

    def get_person(self, id: int):
        return next((person for person in self._people if person.id_number == id), None)

    def update_repo(self):
        pass


class DatabaseRepository(AbstractRepository):
    def __init__(self):
        self._people: List[Person] = list()

    def __iter__(self):
        self._current = 0
        return self

    def __next__(self):
        if self._current >= len(self._people):
            raise StopIteration
        else:
            self._current += 1
            return self._people[self._current-1]

    def get_person(self, id: int):
        return next((person for person in self._people if person.id_number == id), None)

    def update_repo(self):
        people = PersonDB.query.all()
        self._people = []
        for person in people:
            self._people.append(Person(person.id_number, person.firstname, person.lastname))