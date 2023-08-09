import unittest
from app import app


class Login_test(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_login_with_valid_data(self):
        response = self.app.post('/login', data={'username': 'admin', 'password': '12345678'}, follow_redirects=True)
        assert len(response.history) == 1
        assert response.request.path == '/'

    def test_login_with_invalid_username(self):
        response = self.app.post('/login', data={'username': 'test_username', 'password': '12345678'}, follow_redirects=True)
        assert len(response.history) == 1
        assert response.request.path == '/login'

    def test_login_with_invalid_password(self):
        response = self.app.post('/login', data={'username': 'admin', 'password': '12345'}, follow_redirects=True)
        assert len(response.history) == 1
        assert response.request.path == '/login'

    def test_login_with_missing_username(self):
        response = self.app.post('/login', data={'username': '', 'password': '12345678'}, follow_redirects=True)
        assert len(response.history) == 1
        assert response.request.path == '/login'

    def test_login_with_missing_password(self):
        response = self.app.post('/login', data={'username': 'admin', 'password': ''}, follow_redirects=True)
        assert len(response.history) == 1
        assert response.request.path == '/login'


if __name__ == '__main__':
    unittest.main()
