from django.test import TestCase
from django.urls import reverse
from .models import Post
# Create your tests here.


class PostModelTest(TestCase):
    def setUp(self) -> None:
        Post.objects.create(title='Mavzu', text='yangilik matni')

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_objects_title = f'{Post.title}'
        expected_objects_text = f'{Post.text}'
        self.assertEqual(expected_objects_title, 'Mavzu')
        self.assertEqual(expected_objects_text, 'yangilik matni')


class HomePageViewTest(TestCase):
    def setUp(self) -> None:
        Post.objects.create(title='Mavzu 2', text='boshqa yangilik matni')

    def test_urls_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_urls_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_urls_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')

