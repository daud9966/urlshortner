import unittest
import app

class TestURLShortener(unittest.TestCase):
    def setUp(self):
        app.app.testing = True
        self.client = app.app.test_client()

    def test_encode(self):
        response = self.client.post('/encode', json={'url': 'https://uk.indeed.com/'})
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn('short_url', data)

    def test_decode(self):
        # First encode a URL to ensure it exists
        encode_response = self.client.post('/encode', json={'url': 'https://uk.indeed.com/'})
        short_url = encode_response.get_json()['short_url']

        # Now decode the short URL
        decode_response = self.client.post('/decode', json={'url': short_url})
        data = decode_response.get_json()
        self.assertEqual(decode_response.status_code, 200)
        self.assertEqual(data['long_url'], 'https://uk.indeed.com/')

    def test_encode_without_url(self):
        response = self.client.post('/encode', json={})
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], 'URL is required')

    def test_decode_without_url(self):
        response = self.client.post('/decode', json={})
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], 'URL is required')

    def test_decode_nonexistent_url(self):
        response = self.client.post('/decode', json={'url': 'http://short.est/invalid'})
        data = response.get_json()
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['error'], 'Short URL not found')

if __name__ == '__main__':
    unittest.main()
