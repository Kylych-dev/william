from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(
            username='dilon',
            password='dilon123'
        )
        testuser1.save()

        test_post = Post.objects.create(
            author=testuser1,
            title='Dilon\'s post',
            body='Body of dilon\'s post'
        )
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author, 'testuser1')
        self.assertEqual(title, 'Dilon\'s post')
        self.assertEqual(body, 'Body of dilon\'s post')


