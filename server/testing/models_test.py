from app import app
from server.models import db, Earthquake
from sqlalchemy_serializer import SerializerMixin


class TestEarthquake:
    '''Earthquake model in models.py'''

    def test_can_be_instantiated(self):
        '''can be invoked to create a Python object.'''
        quake = Earthquake()
        assert quake
        assert isinstance(quake, Earthquake)

    def test_has_attributes(self):
        '''can be instantiated with an id, magnitude, location, year.'''
        quake = Earthquake(magnitude=9.5, location="Chile", year=1960)
        assert quake.id is None  # Not persisted in database yet
        assert quake.magnitude == 9.5
        assert quake.location == "Chile"
        assert quake.year == 1960

    def test_superclasses(self):
        '''inherits from db.Model and SerializerMixin'''
        quake = Earthquake()
        assert isinstance(quake, db.Model)
        assert isinstance(quake, SerializerMixin)

    def test_dictionary(self):
        '''to_dict() result'''
        quake = Earthquake(magnitude=9.5, location="Chile", year=1960)
        assert quake.to_dict()