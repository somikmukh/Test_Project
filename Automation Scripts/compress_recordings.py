from asyncio import streams
import ffmpeg
import sys
from pprint import pprint

def get_recording_metadata():

    #reading the media file from command line arguments
    media_file_args = sys.argv[1]

    pprint(ffmpeg.probe(media_file_args)[streams])


def main():
    get_recording_metadata()

if __name__ == __main__():
    main()