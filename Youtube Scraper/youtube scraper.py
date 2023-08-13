import requests
import re
import os


def download_youtube_video(video_url):
    """Downloads a YouTube video from the given URL."""

    # Get the video ID from the URL.
    video_id = re.search(r'\/watch\?v=(\w+)', video_url).group(1)

    # Make a request to the YouTube API to get the video details.
    response = requests.get(
        'https://www.googleapis.com/youtube/v3/videos?part=snippet,contentDetails&id=' + video_id)

    # Check if the request was successful.
    if response.status_code != 200:
        print('Error downloading video: ' + response.status_code)
        return

    # Get the video title and thumbnail URL from the response.
    video_title = response.json()['items'][0]['snippet']['title']
    video_thumbnail_url = response.json(
    )['items'][0]['snippet']['thumbnails']['high']['url']

    # Create a directory to store the video.
    video_dir = os.path.join('downloads', video_title)
    if not os.path.exists(video_dir):
        os.mkdir(video_dir)

    # Download the video file.
    video_filename = os.path.join(video_dir, video_title + '.mp4')
    response = requests.get(
        response.json()['items'][0]['contentDetails']['url'], stream=True)
    with open(video_filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            f.write(chunk)

    # Download the video thumbnail.
    video_thumbnail_filename = os.path.join(video_dir, video_title + '.jpg')
    response = requests.get(video_thumbnail_url, stream=True)
    with open(video_thumbnail_filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            f.write(chunk)

    print('Video downloaded successfully!')


if __name__ == '__main__':
    video_url = input('Enter the YouTube video URL: ')
    download_youtube_video(video_url)
