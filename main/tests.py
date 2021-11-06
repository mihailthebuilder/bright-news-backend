from django.test import TestCase

# Complete test for the main app.

API_PATH = "/api/calculate"


class TestMain(TestCase):
    def good_request(self):
        response = self.client.post(path=API_PATH, data={"url": "ft.com"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response.data["score"]), int)

    def bad_request(self):
        response = self.client.post(path=API_PATH, data={"url": "ssre"})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["error"], "Bad request")