from django.test import TestCase

# Create your tests here.
class TestMain(TestCase):
    def test_main_page(self):
        response = self.client.post(path="/api/calculate", data={"url": "ft.com"})
        self.assertEqual(response.status_code, 200)