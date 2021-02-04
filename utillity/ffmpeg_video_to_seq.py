from os import getenv, environ as env, system as start, chdir
from os.path import abspath, dirname, join,normpath, pathsep as sep
import subprocess


FILE_PATH = "F:\\download\\mov\\"
FILE = 'wi3.mp4'
OUT_FILE = 'F:\\download\\mov\\TTP\\TTP_%03d.png' #where %03d frame number 001, %04d - 0001, %02d - 01



DIR = dirname(abspath(__file__)).replace("\\", "/")
ffmpeg_path = join(DIR, 'ffmpeg/bin')
env['PATH'] = normpath(sep.join([x for x in[ffmpeg_path, getenv('PATH', '')]if x]))
chdir(FILE_PATH)
subprocess.call(['ffmpeg', '-y', '-i', FILE,'-vf', 'fps=24', OUT_FILE])