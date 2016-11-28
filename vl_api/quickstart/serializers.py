from django.contrib.auth.models import User, Group
from rest_framework import serializers

from quickstart.models import Voter


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class VoterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Voter
        fields = ('user', 'address', 'party', 'name')
