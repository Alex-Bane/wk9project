from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_page(self):
        with patch("requests.get") as g:
            with patch("requests.post") as p:
                g.return_value.text = "water"
                p.return_value.text = "Jeanne"

                response = self.client.get(url_for("index"))
                self.assertIn(b'you rolled a water its affluence is water and its called Jeanne', response.data)