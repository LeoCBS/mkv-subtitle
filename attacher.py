import os
from pyunpack import Archive

for dirname, dirnames, filenames in os.walk('/run/media/leonardo/DOC3/merge'):
#for dirname, dirnames, filenames in os.walk('/mkvtemp'):
    #extract subtitle
    for subdirname in dirnames:
        dir_path = os.path.join(dirname, subdirname)
        for _file in os.listdir(dir_path):
            if _file.endswith(".rar"):
                file_path_absolute = os.path.join(dir_path, _file)
                Archive(file_path_absolute).extractall(dir_path)
                #print(_file)

    for subdirname in dirnames:
        dir_path = os.path.join(dirname, subdirname)
        for _file in os.listdir(dir_path):
            if _file.endswith(".mkv"):
                try:
                    mkv_path_absolute = os.path.join(dir_path, _file)
                    file_converted = _file.replace(".mkv", "converted.mkv")
                    subtitle_path = mkv_path_absolute.replace(".mkv", ".srt")
                    iconv = "iconv -t UTF-8 -f ISO-8859-1 {} > {}.tmp"
                    iconv = iconv.format(subtitle_path, subtitle_path)
                    os.system(iconv)
                    cp_temp = "mv " + subtitle_path + ".tmp " + subtitle_path
                    os.system(cp_temp)
                    docker_mkverge_cli = ("docker run -ti --rm -v "+ dir_path +":/mkvtemp "
                                          "leocbs/mkvmergetool ")
                    mkvmerge_cli = (docker_mkverge_cli + "mkvmerge -o " + file_converted + " " +
                                _file + " " + _file.replace(".mkv", ".srt"))
                    print(mkvmerge_cli)
                    os.system(mkvmerge_cli)
                    #print(os.system("docker run -ti --rm -v $(pwd)"+ dirname +":/mkvtemp"
                    #        " leocbs/mkvmergetool ls"))
                    #hd_path = 
                    #cp = "cp " + os.path.join(dir_path, file_converted) + 
                    #print
                except Exception as e:
                    print(e)

#mkvmerge -o Vikings.S04E15c.mkv Vikings.S04E15.mkv Vikings.S04E15.str        
