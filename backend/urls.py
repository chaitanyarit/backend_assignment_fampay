from django.urls import include, path
from rest_framework import routers
from . import views

prefix = 'api/v1/'
router = routers.DefaultRouter()
router.register(r"get-all-videos", views.YoutubeAPIResultsViewSet)
router.register(r"search-videos", views.YoutubeAPIResultsFilterViewSet)

urlpatterns = [
    path(prefix, include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
