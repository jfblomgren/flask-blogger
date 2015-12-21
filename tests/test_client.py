from flask import url_for

from app import user_datastore
from app.models import Post
from tests.general import AppTestCase


class TestClient(AppTestCase):
    def setUp(self):
        super().setUp()
        self.client = self.app.test_client(use_cookies=True)

        # Create user and log in
        user_datastore.create_user(email='foo@bar.com', password='foobar')
        self.client.post(url_for('security.login'), data={
            'email': 'foo@bar.com',
            'password': 'foobar'
        }, follow_redirects=True)

    def test_new_post(self):
        self.client.post(url_for('admin.new_post'), data={
            'title': 'foo',
            'body': 'bar',
            'tags': 'foobar'
        })
        post = Post.query.first()
        self.assertIsNotNone(post)
