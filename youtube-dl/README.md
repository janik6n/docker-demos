README
======

Containerized version of [youtube-dl](https://rg3.github.io/youtube-dl/). 

Container info:

- Built on top of `Alpine Linux 3.6`
- Has the version `2017.08.23` of `youtube-dl` installed via `Python 3 pip`.
- `ffmpeg` to combine video and audio tracks
- *All packed in 114 MB!*

## Usage

To use, run the following command:
```
docker run -it --rm -v "$(pwd):/src" janikarh/youtube-dl:latest \
    -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]' \
    -o '/src/%(title)s.mp4' --restrict-filenames \
    https://www.youtube.com/watch?v=[video_id]
```
