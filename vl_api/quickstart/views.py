from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from quickstart.serializers import (
    UserSerializer, GroupSerializer, VoterSerializer)
from quickstart.models import Voter
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    @detail_route(methods=['post'])
    def new_user(self, request, pk=None):
        print('new user hit')
        # user = self.get_object()
        #
        # serializer = UserSerializer(data=request.data)
        # serializer.is_valid(raise_exception=True)

        # trying to create an instance using the ReturnDict from the serializer
        VoterManager.create_voter(request.data)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class VoterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Voter.objects.all()
    serializer_class = VoterSerializer
