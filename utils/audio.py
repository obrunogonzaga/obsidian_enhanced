import os
from moviepy.editor import VideoFileClip
from faster_whisper import WhisperModel
from dotenv import load_dotenv

load_dotenv()

class Audio:
    def extract(video_path):
        '''Extract audio from a video file and save in WAV format'''
        print(f'\nExtracting audio from video: {video_path}')

        video_path = video_path.replace("'", "")

        print(f'video_path = {video_path}')

        output_path = os.path.dirname(video_path)
        output_path = output_path.replace('videos', 'audios')

        print(f'output_path = {output_path}')

        base_name = os.path.splitext(os.path.basename(video_path))[0]
        print(f'basename = {base_name}')

        audio_path = f'{output_path}/{base_name}.mp3'
        print(f'audio_path = {audio_path}')

        video = VideoFileClip(video_path)

        if not os.path.exists(output_path):
            os.makedirs(output_path)
            print(f'Folder { output_path } created!')
        
        video.audio.write_audiofile(audio_path)

        print(f'Audio saved in: {audio_path}')
        return audio_path
    
    def transcribing(audio_path: str) -> str:
        '''Transcribing a audio file in audio_path in a text using speach recoginize'''
        print(f'Transcribe audio: {audio_path}')

        audio_path = audio_path.replace("'", "")
        model = WhisperModel('medium')

        result = model.transcribe(audio_path, language='pt')

        transcribe = ''

        for segment in result[0]:
            transcribe = segment.text + " "

        output_path = os.path.dirname(audio_path)
        output_path = output_path.replace('audios', 'transcribes')
        base_name = os.path.splitext(os.path.basename(audio_path))[0]
        transcribe_path = f'{output_path}/{base_name}.md'

        if not os.path.exists(output_path):
            os.makedirs(output_path)
            print(f'Folder { output_path } created!')
        
        with open(transcribe_path, 'w', encoding='utf-8') as f:
            f.write(transcribe.strip())
        
        print(f'Transcrição salva em: {transcribe_path}')
        return transcribe_path
    
if __name__ == '__main__':
    video_path = '_videos/_Como_Aprender_Qualquer_Coisa_RÁPIDO.mp4'
    audio_path = Audio.extract(video_path)
    transcribe_path = Audio.transcribing(audio_path)