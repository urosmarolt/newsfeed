from django.test import TestCase
from newsfeed.models import EventregistryPost
from newsfeed.factories import EventRegistryPostFactory

# Create your model tests here.
class EventRegistryPostTest(TestCase):

    def setUp(self):
        self.post = EventregistryPost(title='TestPostTitle')
        #self.post.save()

    def tearDown(self):
        pass#self.post.delete()

    def test_string_model(self):
        self.assertEqual("TestPostTitle", self.post.__str__())