import argparse
import os
import random
import requests
import string
import subprocess
import traceback 

from urllib.parse import urlparse

SAVE_FOLDER_NAME = "videos"

def random_string(size=12):
    rstring = string.ascii_lowercase + string.digits
    return "".join([rstring[random.randint(0, len(rstring)-1)] for i in range(size)])

def is_url_callable(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        return False
    except:
        return False

def is_url_valid(url):
    try:
        result = urlparse(url)
        if result.scheme and result.netloc:
            # os.path.splitext will split the filename and extension
            filename, extension = os.path.splitext(result.path)
            if extension == ".m3u8" and is_url_callable(url):
                return True
            return False
        else:
            return False
    except:
        return False

def is_filename_valid(file):
    try:
        filename, extension = os.path.splitext(file)
        if extension == ".mp4":
            return True
        return False
    except:
        return False

def parse_args():
    parser = argparse.ArgumentParser(
        description="A python3 script to utilise ffmpeg command to download .m3u8 videos"
    )
    parser.add_argument("url", help=".m3u8 url to download video (mandatory)")
    parser.add_argument("--filename", help="file name for downloaded video (optional)")
    return parser.parse_args()

def main():
    """
    References:

    https://docs.python.org/3.10/howto/argparse.html#introducing-optional-arguments
    https://www.annasyme.com/docs/python_structure.html
    https://docs.python.org/3/library/functions.html#getattr
    https://stackoverflow.com/questions/89228/how-do-i-execute-a-program-or-call-a-system-command
    https://stackoverflow.com/questions/541390/extracting-extension-from-filename-in-python
    """

    try:
        arguments = parse_args()
        if not getattr(arguments, "url"):
            print("Error processing: Please provide m3u8 url for the video.")
            return
        
        video_url = arguments.url
        if not is_url_valid(video_url):
            print("Error processing: Video url is not valid.")
            return

        # os.path.realpath(__file__) will give you the file path to current file. 
        # os.path.dirname will omit current file from the path and get the directory.
        current_directory = os.path.dirname(os.path.realpath(__file__))
        filename = getattr(arguments, "filename") or random_string() + ".mp4"
        if not is_filename_valid(filename):
            print("Error processing: File name is not valid.")
            return

        download_dir = os.path.join(current_directory, SAVE_FOLDER_NAME)
        # os.path.isdir is to check whether the directory exists
        if not os.path.isdir(download_dir):
            os.mkdir(download_dir)
        
        download_path = os.path.join(download_dir, filename)
        command = 'ffmpeg -i "{url}" -codec copy "{path}"'.format(
            url=video_url, path=download_path
        )
        subprocess.run(command, shell=True, check=True)

    except Exception as e:
        print("Error processing: {}".format(e))
        print("Traceback: {}".format(traceback.format_exc()))

if __name__ == "__main__":
    main()