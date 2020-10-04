from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .pagenation import ResultsSetPagination
from .models import YoutubeAPIResults
from .serializers import YoutubeAPIResultsSerializer


class YoutubeAPIResultsViewSet(viewsets.ModelViewSet):
    """
    This class handles the endpoint: /api/v1/get-all-videos and returns a
    paginated response for all the videos in the db
    """
    queryset = YoutubeAPIResults.objects.all().order_by('-publishedAt')
    serializer_class = YoutubeAPIResultsSerializer
    pagination_class = ResultsSetPagination


class YoutubeAPIResultsFilterViewSet(viewsets.ModelViewSet):
    """
    This class handles the endpoint: /api/v1/search-videos?search=<query> and
    returns a paginated response for all the videos in the db which match the
    criteria based on entered search query
    """
    queryset = YoutubeAPIResults.objects.all().order_by('-publishedAt')
    serializer_class = YoutubeAPIResultsSerializer
    pagination_class = ResultsSetPagination
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,
                       filters.SearchFilter)
    filterset_fields = {
        'videoDescription': ['icontains'],
        'videoTitle':['icontains']
    }
    search_fields = ['videoTitle', 'videoDescription']