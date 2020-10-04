from .models import YoutubeAPIResults
from rest_framework import serializers


class YoutubeAPIResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = YoutubeAPIResults
        fields = "__all__"
