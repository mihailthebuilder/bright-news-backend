from django.test import TestCase

# Complete test for the main app.

API_PATH = "/api/calculate"


class TestMain(TestCase):
    def test_good_request(self):
        response = self.client.post(path=API_PATH, data={"url": "ft.com"})
        self.assertEqual(response.status_code, 200)

        first_scored_url = response.data["website_li"][0]

        self.assertEqual(type(first_scored_url["score"]), float)
        self.assertEqual(type(first_scored_url["url"]), str)

    def test_bad_request(self):
        response = self.client.post(path=API_PATH, data={"url": "ssre"})
        self.assertEqual(response.status_code, 500)
        # TODO: Check text of the error message.
        # self.assertEqual(response.data["error"], "Bad request")