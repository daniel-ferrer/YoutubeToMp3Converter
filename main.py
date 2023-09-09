import os
from pytube import YouTube
from moviepy.editor import VideoFileClip


def download_video(url, output_path):
    try:
        # create YouTube object
        yt = YouTube(url)

        # select highest resolution stream & download mp4
        video_stream = yt.streams.filter(only_video=False, file_extension="mp4").first()
        video_stream.download(output_path=output_path)

        return video_stream.default_filename

    except Exception as e:
        print(f"Error downloading video: {str(e)}")
        return None


def convert_to_mp3(input_path, output_path):
    try:
        # load mp4
        video = VideoFileClip(input_path)

        # convert to mp3
        audio = video.audio
        audio.write_audiofile(output_path)
        audio.close()

        return True

    except Exception as e:
        print(f"Error converting to MP3: {str(e)}")
        return False


if __name__ == "__main__":

    output_dir = "downloads"

    yt_url = input("Enter the YouTube video URL: ")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    mp4_filename = download_video(yt_url, output_dir)
    if mp4_filename is None:
        print("Video download failed.")
        exit(1)

    mp3_filename = mp4_filename.replace(".mp4", ".mp3")

    # set source (mp4) & target (mp3) file paths
    mp4_filepath = os.path.join(output_dir, mp4_filename)
    mp3_filepath = os.path.join(output_dir, mp3_filename)

    if convert_to_mp3(mp4_filepath, mp3_filepath):
        print(f"MP3 file saved at {mp3_filepath}")
    else:
        print("Conversion to MP3 failed.")

    os.remove(mp4_filepath)
