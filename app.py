import os

import requests
from flask import Flask, redirect
from urllib.parse import urlparse, parse_qs
from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

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

# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'),
#                                'favicon.ico', mimetype='image/vnd.microsoft.icon')
# 
# @app.route('/hello', methods=['POST'])
# def hello():
#    name = request.form.get('name')
# 
#    if name:
#        print('Request for hello page received with name=%s' % name)
#        return render_template('hello.html', name = name)
#    else:
#        print('Request for hello page received with no name or blank name -- redirecting')
#        return redirect(url_for('index'))


if __name__ == '__main__':
   app.run()

# http://127.0.0.1:5000/uVWJoU1Yv1U,aTvtb6syC9Q,khwlvvKc8Dk
