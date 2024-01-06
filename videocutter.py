#!/usr/bin/python3
import argparse
from pytube import YouTube
from moviepy.video.io.VideoFileClip import VideoFileClip

def clean_filename(name):
    clean_name = name.replace('/','').replace(',','')
    return clean_name

def download_video(url, resolution, output_path):
    print(f'Downloading video from {url} ...', flush=True)
    yt = YouTube(url)
    video_stream = yt.streams.filter(file_extension='mp4', res=resolution).first()
    video_stream.download(output_path)
    return clean_filename(video_stream.title)

def cut_video(input_video, output_folder, segment_duration, video_title):
    print(f'Cuting video input_video ...', flush=True)
    video_clip = VideoFileClip(input_video)

    total_duration = video_clip.duration
    current_time = 0

    segment_number = 1
    while current_time < total_duration:
        print(f'Segment {segment_number} ...', flush=True)
        start_time = current_time
        end_time = min(current_time + segment_duration, total_duration)

        segment_clip = video_clip.subclip(start_time, end_time)
        segment_clip.write_videofile(f"{output_folder}/{video_title}_#{segment_number}.mp4", codec="libx264")

        current_time += segment_duration
        segment_number += 1

    video_clip.close()


def main():
    """
    Main entrypoint

    :return:
    """
    parser = argparse.ArgumentParser(description='Video Downloader and cutter')   
    parser.add_argument('--url', help='Youtube URL', default='')
    parser.add_argument('--input', help='Input video', default='')
    parser.add_argument('--outputdir', help='Output Directory', default='.')
    parser.add_argument('--segduration', help='Segment Duration in s', default=60)
    parser.add_argument('--resolution', help='Resolution from [144p, 240p, 360p, 480p, 720p, 1080p]', default='720p')
    args = parser.parse_args()

    if args.url == '' and args.input == '':
        print('Usage --url <Youtube URL> [--outputdir <Output Directory> --segduration <Segment Duration in s>]', flush=True)
        print('Usage --input <input mp4> [--outputdir <Output Directory> --segduration <Segment Duration in s>]', flush=True)
    else:
        
        youtube_url = args.url
        output_folder = args.outputdir
        segment_duration = int(args.segduration)
        resolution = args.resolution
        if args.input == '':
            video_title = download_video(youtube_url, resolution, output_folder)
        else:
            video_title = (args.input.split('/')[-1]).split('.mp4')[0]
        input_video = f"{output_folder}/{video_title}.mp4"
        cut_video(input_video, output_folder, segment_duration, video_title)

if __name__ == "__main__":
    main()
