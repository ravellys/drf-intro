from django.urls import include, path
from rest_framework import routers

from drf.base import views

router = routers.DefaultRouter()
router.register(r'members', views.MemberViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
    path('api/members2/', views.member_api),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
