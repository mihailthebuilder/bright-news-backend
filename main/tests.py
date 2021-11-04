from django.test import TestCase

# Complete test for the main app.
class TestMain(TestCase):
    def test_main_page(self):
        response = self.client.post(path="/api/calculate", data={"url": "ft.com"})
        self.assertEqual(response.status_code, 200)