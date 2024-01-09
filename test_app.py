import unittest
from flask import Flask, request, url_for
from app import app, items


class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_add_item(self):
        # Test adding an item
        response = self.app.post('/add', data=dict(item="Test Item"), follow_redirects=True)
        self.assertEqual(response.status_code, 200, "Response should be 200 OK")
        self.assertIn(b'Test Item', response.data, "Item not found in response")

    def test_delete_item(self):
        # Add an item first for testing deletion
        items.append('Item to be deleted')
        response = self.app.get('/delete/0', follow_redirects=True)
        self.assertEqual(response.status_code, 200, "Response should be 200 OK")
        self.assertNotIn(b'Item to be deleted', response.data, "Item still present after deletion")


if __name__ == '__main__':
    unittest.main()
