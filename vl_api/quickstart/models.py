from django.db import models
from django.contrib.auth.models import User


class VoterManager(models.Manager):
    def create_voter(self, username, email, password, address, party, name):
        user = User.objects.create_user(username=username,
                                        email=email,
                                        password=password)
        voter = self.create(user=user, address=address, party=party, name=name)

        return voter


class Voter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    party = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    objects = VoterManager()
