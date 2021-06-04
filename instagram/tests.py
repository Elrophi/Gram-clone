from django.test import TestCase

from .models import UserProfile, Post
from django.contrib.auth.models import User

# Create your tests here.
class TestUserProfile(TestCase):
    def setUp(self):
        self.user = User(username='Ben')
        self.user.save()

        self.profile_test = UserProfile(id=1, name='Ben', picture='default.jpg', bio='this is a test profile',
                                    user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile_test, UserProfile))

    def test_save_profile(self):
        self.profile_test.save_profile()
        after = UserProfile.objects.all()
        self.assertTrue(len(after) > 0)


class TestPost(TestCase):
    def setUp(self):
        self.profile_test = UserProfile(name='Ben', user=User(username='Benny'))
        self.profile_test.save()

        self.image_test = Post(image='default.png', name='test', caption='default test', user=self.profile_test)

    def test_insatance(self):
        self.assertTrue(isinstance(self.image_test, Post))

    def test_save_image(self):
        self.image_test.save_image()
        images = Post.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_image(self):
        self.image_test.delete_image()
        after = UserProfile.objects.all()
        self.assertTrue(len(after) < 1)