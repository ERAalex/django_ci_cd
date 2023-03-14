from django.test import TestCase


class TestEng_index(TestCase):
    def test_eng_index(self):
        response = self.client.get('http://127.0.0.1:8000/eng_version')
        self.assertEqual(response.status_code, 200)