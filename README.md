[![Build
Status](https://travis-ci.org/LeoCBS/mkv-subtitle.svg?branch=master)](https://travis-ci.org/LeoCBS/mkv-subtitle) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/0929cf8d82a94343bd46124008592b8e)](https://www.codacy.com/app/LeoCBS/mkv-subtitle?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=LeoCBS/mkv-subtitle&amp;utm_campaign=Badge_Grade)



# mkv-subtitle

Embed subtitle to mkv container using [mkvmerge](https://github.com/mbunkus/mkvtoolnix) tool version 5.8.0.

Why using one old version?

Some hardware (TVs, HTs) don't have full compatibility with mkv specification.. mkvmerge tends to use all the latest features all the time, and this can pose problems for such players.. See this [link](https://github.com/mbunkus/mkvtoolnix/wiki/Improving-playback-compatibility-with-players) for more information about mkv compatibility

## How this works?

This using Docker to compile and install mkv merge tool 5.8.0 in one Docker image

## Requirements

Docker 1.9.0 +

## How to use:

Just use mkvmerge cli directly in docker container:

    docker run --rm -v $(pwd):/mkvtemp leocbs/mkvmergetool:1.0.0 mkvmerge -V

output:   
    
    mkvmerge v5.8.0 ('No Sleep / Pillow') built on Jan 15 2017 18:04:03

Must set one volume `/mkvtemp` with your mkv and subtitle files.

Simple example to embed subtitle:
 
    docker run -ti --rm -v $(pwd):/mkvtemp leocbs/mkvmergetool mkvmerge -o Vikings.S04E15c.mkv Vikings.S04E15.mkv Vikings.S04E15.str


## Virtual env


## Python requirements

If you wish use attacher.py, you will need some extra libs

    * pyunpack
