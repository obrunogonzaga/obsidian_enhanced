import os
import re

from pytubefix import YouTube

class YoutubeDownloader:
    def download_video(self, url):
        print(f'Downloading Youtuve videos from URL: { url }')
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        title = yt.title

        output_path = '_videos'
        if not os.path.exists(output_path):
            os.makedirs(output_path)
            print(f'Folder { output_path } created!')

        title = re.sub(r'[<>:"/\\|?*]', '', title)
        title = title.replace("'", "")
        title = title.strip().replace(' ', '_')
        title = f'_{title}.mp4'

        video_path = stream.download(output_path, title)
        print(f'Downloading "{title}" video to "{video_path}"')
        video_path = f'{output_path}/{title}'
        print(f'Youtube video download in {video_path}')
        return video_path
    
if __name__ == '__main__':
    yt = YoutubeDownloader()
    youtube_url = 'https://www.youtube.com/watch?v=cuQReNaVgq0'
    yt.download_video(youtube_url)