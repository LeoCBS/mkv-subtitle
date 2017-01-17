# mkv-subtitle

Embed subtitle to mkv container using [mkvmerge](https://github.com/mbunkus/mkvtoolnix) tool version 5.8.0.

Why using one old version?  Some hardware (TVs, HTs) don't have full
compatibilite with mkv especification.. so this hardware coul'd reproduce mkv
files correctly. See this
[link](https://github.com/mbunkus/mkvtoolnix/wiki/Improving-playback-compatibility-with-players) for more information about mkv compatibility

## How this works?

This using Docker to compile and install mkv merge tool 5.8.0 in one Docker image

## Requeriments

Docker 1.9.0 +

## How to use:

Just use mkvmerge cli directly in docker container:

    docker run --rm -v $(pwd):/mkvtemp leocbs/mkvmergetool:1.0.0 mkvmerge -V    
    mkvmerge v5.8.0 ('No Sleep / Pillow') built on Jan 15 2017 18:04:03

Must set one volume `/mkvtemp` mapped with your mkv and subtittle files.

Simple example to embed subtitle:
 
    docker run -ti --rm -v $(pwd):/mkvtemp leocbs/mkvmergetool mkvmerge -o Vikings.S04E15c.mkv Vikings.S04E15.mkv Vikings.S04E15.str

