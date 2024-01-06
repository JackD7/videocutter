# Video downloader and cutter
## Description
Download video from youtube and cut it into segments \
Cut can also be done on local mp4 video files
## Dependencies
```
pip3 install pytube
```
```
pip3 install moviepy
```
### Usage
With Youtube url
```
python3 videocutter.py --url <Youtube URL> --outputdir <Output Directory (default='.')> --segduration <Segment Duration in s (default=60)> --resolution <Resolution from [144p, 240p, 360p, 480p, 720p, 1080p] (default='720p')>
```
With local file
```
python3 videocutter.py --input <local mp4> --outputdir <Output Directory (default='.')> --segduration <Segment Duration in s (default=60)>
```

### Example
```
python3 videocutter.py --url https://youtu.be/fregObNcHC8?feature=shared --outputdir ./clip --segduration 61 --resolution 1080p
```
