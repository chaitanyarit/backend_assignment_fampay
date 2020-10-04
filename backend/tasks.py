import os
from datetime import datetime, timedelta
from celery import shared_task
from apiclient.discovery import build
import apiclient

from .models import YoutubeAPIResults

from dotenv import load_dotenv
load_dotenv(".env")


YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
DEVELOPER_KEYS = os.getenv("GOOGLE_API_KEYS").split(',')

@shared_task
def fetch_latest_youtube_videos():
    """
    Function to fetch the videos details from the Youtube Data API. This runs as
    a task in the background executed by celery worker process every 3 minutes.
    First creates an object to fetch data, checks if its valid and adds the
    fetched data to the database.
    Reference for Youtube API: https://developers.google.com/youtube/v3/docs/
    """
    prev_time = datetime.now() - timedelta(minutes=5)
    time_from_last_request = prev_time.strftime("%Y-%m-%dT%H:%M:%SZ")
    result = None
    for key in DEVELOPER_KEYS:
        try:
            youtube_object = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                                   developerKey=key)
            result = youtube_object.search().\
                list(q="football", type="video",
                     part="snippet",
                     order="date", maxResults=50,
                     publishedAfter=time_from_last_request).execute()

            break
        except apiclient.errors.HttpError as e:
            error_code = e.resp.status
            if error_code == 403:
                continue
    if result:
        for data in result['items']:
            video_id = data['id']['videoId']
            video_title = data['snippet']['title']
            video_description = data['snippet']['description']
            channel_title = data['snippet']['channelTitle']
            published_at = data['snippet']['publishedAt']
            thumbnail_url = data['snippet']['thumbnails']['default']['url']
            thumbnail_height = data['snippet']['thumbnails']['default']['height']
            thumbnail_width = data['snippet']['thumbnails']['default']['width']
            YoutubeAPIResults.objects.create(
                videoID =video_id,
                videoTitle=video_title,
                videoDescription=video_description,
                channelTitle=channel_title,
                publishedAt=published_at,
                thumbnailURL=thumbnail_url,
                thumbnailHeight=thumbnail_height,
                thumbnailWidth=thumbnail_width
            )
