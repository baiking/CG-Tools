from os import getenv, environ as env, system as start, chdir
from os.path import abspath, dirname, join,normpath, pathsep as sep
import subprocess


FILE_PATH = 'G:\\vfx\\mov\\'
SOURCE_FILE = 'test.%04d.jpg' #where %04d frame number 0001, %03d - 001, %02d - 01
FRAME = '1001'
CODEC = 'libx264'
BITRATE = '15000k'
OUT_FILE = 'TEST_0010.mov'




DIR = dirname(abspath(__file__)).replace("\\", "/")
ffmpeg_path = join(DIR, 'ffmpeg/bin')
env['PATH'] = normpath(sep.join([x for x in[ffmpeg_path, getenv('PATH', '')]if x]))
chdir(FILE_PATH)
subprocess.call(['ffmpeg', '-r', '1','-start_number', FRAME,'-y', '-i', SOURCE_FILE, '-c:v', CODEC, '-b:v', BITRATE, OUT_FILE])