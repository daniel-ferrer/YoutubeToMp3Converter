# YoutubeToMp3Converter
Here's a bit of background about this script that nobody asked for:

I typically use other converters out there to download music when I hear an unreleased Drake song that I really like. 
For some reason, I never thought about making my own... and these days no games are fun to play so I spent about 45 minutes putting this together.

You'll have to have ffmpeg installed, you can do so with the following commands:

For Linux:

        sudo apt-get install ffmpeg

For macOS(using Homebrew)

        brew install ffmpeg

For Windows:

You can download the FFmpeg executable from the official 
website (https://www.ffmpeg.org/download.html) and add the FFmpeg bin directory to your 
system's PATH. Make sure to select the "Windows Builds" section for Windows installations.

Other than that I'm pretty sure this will work straight out the box for anyone who wants to try, just install the required pip packages:

        pip install -r requirements.txt

Feel free to modify the ``output_dir`` variable in the driver to change where the mp3 is downloaded.
Nothing special about this script, ideally you can point this at some import folder for your music streaming service (only Apply Music to my knowledge lol).
