from os import getenv, environ as env, system as start, chdir
from os.path import abspath, dirname, join,normpath, pathsep as sep
import subprocess


FILE_PATH = 'G:\\vfx\\mov\\'
SOURCE_FILE = 'lighting_v001.mov'
CODEC = 'libx265'
BITRATE = '500000k'
OUT_FILE = 'lighting_v002.mov'



DIR = normpath(dirname(abspath(__file__))).replace("\\", "/") # root folder
ffmpeg_path = join(DIR, 'ffmpeg/bin')
env['PATH'] = normpath(sep.join([x for x in[ffmpeg_path, getenv('PATH', '')]if x]))
chdir(FILE_PATH)
subprocess.call(['ffmpeg', '-y', '-i', SOURCE_FILE, '-c:v', CODEC,'-b:v', BITRATE, '-pass', '1', OUT_FILE ])