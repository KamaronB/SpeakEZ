from django.test import TestCase
from .models import Profile, Relationship, People, requests,Message, Room
# Create your tests here.



class ProfileTestCase(TestCase):

    def createUser(self):
        mcFakins= User.objects.create(first_name="fake", last_name="User" username="mcFakins")
        mcFakins= User.objects.create(first_name="fake", last_name="User" username="mcFakins")

        # mckFakins.profile.bio=


    def verify_Profiles(self):
