from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['firstName'] = user.first_name
        token['lastName'] = user.last_name
        token['email'] = user.email
        token['groups'] = list(user.groups.values_list('name', flat=True))

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('base.urls')),
    path('api/', include('base.api.urls')),

    path('api/auth/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
