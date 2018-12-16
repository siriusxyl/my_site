from django.test import TestCase, Client


# Create your tests here.


class WgameTest(TestCase):
    def test_version_view(self):
        result = Client().get("/version/my_game/1.0.1/1/")
        print result.content