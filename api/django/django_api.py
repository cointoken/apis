from django.conf.urls import url,include
from django.contrib.auth.models import User
from rest_framework import routers,serializers,viewsets

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = {'username','password','phone','is_active'}


class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer


router = routers.DefaultRouter()
router.register(r'users',UserViewSet)

urlpatters = [
    url(r'^',include(router.urls)),
    url(r'api-auth/',include('rest_framework.urls',namespace='rest_framework'))
]