from rest_framework.viewsets import ModelViewSet
from user.models import User
from user.serializers import RegisterSerializer, UserSerializer
from api.utils import CustomAllowAnyPost
from rest_framework.decorators import permission_classes
from rest_framework.response import Response

# Create your views here.

@permission_classes([CustomAllowAnyPost])
class RegisterViewSet(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class UserViewSet(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, pk=None):
        """
        If provided 'pk' is "me" then return the current user.
        """
        if request.user and pk == 'me':
            return Response(UserSerializer(request.user).data)
        return super(UserViewSet, self).retrieve(request, pk)