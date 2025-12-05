from django.test import Client, TestCase


class HelloTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_index_html(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertIn('Hello, world', resp.content.decode())

    def test_index_json(self):
        resp = self.client.get('/?format=json', HTTP_ACCEPT='application/json')
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertEqual(data['status'], 'ok')
        self.assertEqual(data['message'], 'Hello, world!')
