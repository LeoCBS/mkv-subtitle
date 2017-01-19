import os
from pyunpack import Archive
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--mkvsource', help='pass mkv folder source. ex:'
        '/home/user/mkvs', required=True)
parser.add_argument('--hddtest', help='path to external disk. ex:'
        '/home/user/mkvs', required=True)
args = parser.parse_args()

for dirname, dirnames, filenames in os.walk(args.mkvsource):
    #extract subtitle
    for subdirname in dirnames:
        dir_path = os.path.join(dirname, subdirname)
        for _file in os.listdir(dir_path):
            if _file.endswith(".rar"):
                file_path_absolute = os.path.join(dir_path, _file)
                Archive(file_path_absolute).extractall(dir_path)

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
                    print("converting ", _file)
                    os.system(mkvmerge_cli)
                    converted_absolute_path = os.path.join(dir_path, file_converted)
                    cp_command = "cp " + converted_absolute_path + " " + args.hddtest
                    print("copying to hdd")
                    os.system(cp_command)
                except Exception as e:
                    print(e)
