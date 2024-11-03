from os import environ
import re
import json

from app import app


class TestApp:
    '''Flask application in flask_app.py'''

    def test_earthquake_magnitude_route(self):
        '''has a resource available at "/earthquakes/magnitude/<magnitude>".'''
        response = app.test_client().get('/earthquakes/magnitude/8.0')
        assert response.status_code == 200

    def test_earthquakes_magnitude_match_response(self):
        '''displays json in earthquake/magnitude route with keys for count, quakes'''

        response = app.test_client().get('/earthquakes/magnitude/9.0')
        # get the response body
        response_body = response.data.decode()
        # convert to JSON
        response_json = json.loads(response_body)
        # confirm JSON data
        assert response_json["count"] == 2
        assert len(response_json["quakes"]) == 2
        # confirm list contents
        quake1 = response_json["quakes"][0]
        assert quake1["id"] == 1
        assert quake1["magnitude"] == 9.5
        assert quake1["location"] == "Chile"
        assert quake1["year"] == 1960
        quake2 = response_json["quakes"][1]
        assert quake2["id"] == 2
        assert quake2["magnitude"] == 9.2
        assert quake2["location"] == "Alaska"
        assert quake2["year"] == 1964

        # confirm status
        assert response.status_code == 200

    def test_earthquakes_magnitude_no_match_response(self):
        '''displays json in earthquake/magnitude route with keys for count, quakes'''

        response = app.test_client().get('/earthquakes/magnitude/10.0')
        # get the response body
        response_body = response.data.decode()
        # convert to JSON
        response_json = json.loads(response_body)
        # confirm JSON data
        assert response_json["count"] == 0
        assert len(response_json["quakes"]) == 0

        # confirm status
        assert response.status_code == 200