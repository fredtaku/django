from django.urls import path, include
from django.conf.urls import url, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()

router.register(r'courses', views.CourseView)



urlpatterns = [
    # here you include your router
    path('', include(router.urls)),
    # here you include the authentication paths
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
