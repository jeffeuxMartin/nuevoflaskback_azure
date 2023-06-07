import requests
from flask import Flask, redirect
from urllib.parse import urlparse, parse_qs

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"


@app.route('/<video_ids>')
def get_playlist_page(video_ids):
    url = f"https://www.youtube.com/watch_videos?video_ids={video_ids}"
    response = requests.get(url)
    redirected_url = response.url

    parsed_url = urlparse(redirected_url)
    query_params = parse_qs(parsed_url.query)

    if 'list' in query_params:
        [playlist_id] = query_params['list']
        return redirect(f"https://www.youtube.com/playlist?list={playlist_id}")
    else:
        return "No playlist ID found."

if __name__ == '__main__':
    app.run()

# http://127.0.0.1:5000/uVWJoU1Yv1U,aTvtb6syC9Q,khwlvvKc8Dk
