from .viewsBase import *
from .models import *

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenVerifySerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView
from rest_framework_simplejwt.tokens import AccessToken

########################################################################################
########################################################################################
class CoreTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['username'] = self.user.username
        data['visibleUsername'] = self.user.visibleUsername
        data['organization'] = OrganizationSerializer(self.user.organization, read_only=True).data
        data['permissions'] = self.user.get_all_permissions()
        return data
class CoreTokenObtainPairView(TokenObtainPairView):
    serializer_class = CoreTokenObtainPairSerializer
########################################################################################
########################################################################################
class CoreTokenVerifySerializer(TokenVerifySerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user = User.objects.get(id=AccessToken(attrs['token'])['user_id'])
        data['username'] = user.username
        data['visibleUsername'] = user.visibleUsername
        data['organization'] = OrganizationSerializer(user.organization, read_only=True).data
        data['permissions'] = user.get_all_permissions()
        return data
class CoreTokenVerifyView(TokenVerifyView):
    serializer_class = CoreTokenVerifySerializer

