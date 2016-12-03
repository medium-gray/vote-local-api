from django.contrib.auth.models import User, Group
from rest_framework import serializers

from quickstart.models import Voter


class VoterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Voter
        fields = ('address', 'party', 'name')
        user = User()

    def create(self, validated_data):
        voter = Voter.objects.create(
            address=validated_data['address'],
            party=validated_data['party'],
            name=validated_data['name'],
        )

        return voter


class UserSerializer(serializers.HyperlinkedModelSerializer):
    voter = VoterSerializer()

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups', 'voter')

    def create(self, validated_data):
        voter_data = validated_data.pop('voter')
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
            # voter=voter
            # first_name=validated_data['first_name'],
            # last_name=validated_data['last_name']
        )
        Voter.objects.create(
            address=voter_data['address'],
            party=voter_data['party'],
            name=voter_data['name'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

