# H1 Python3 script using ffmpeg to download .m3u8 url to mp4 files
This is a **python3.11.7** script utilising **ffmpeg** command to download **.m3u8** videos as **.mp4** files.

As a prerequisite, you will need to install
1. [ffmpeg](https://ffmpeg.org/download.html)
2. [python3](https://www.python.org/downloads/)
3. libraries from requirements.txt

python main.py -h/--help to see the available arguments

Example Usage: python main.py [url] --filename [filename]

Downloaded videos will be available on [code folder]/videos directory.