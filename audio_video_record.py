import subprocess
import re
from datetime import datetime

time_video_seconds = 18
device_index = None

cmd_devices = 'ffmpeg -f avfoundation -list_devices true -i "" &> devices.txt'
subprocess.call(cmd_devices, shell=True)
with open('devices.txt', 'r') as file:
    rows = file.read()
    x = re.search(".{3}( Built-in Microphone)", rows)
    string_result = x.group()
    device_index = int(string_result[1:2])

now = datetime.now()
date_time = now.strftime("%d-%m-%Y__%H-%M-%S")
cmd = f'ffmpeg -f avfoundation -r 30 -s 1280x720 -pix_fmt yuyv422 -i "0:{device_index}" -t {time_video_seconds} -y -c:v libx264 -c:a ac3 data/av_{date_time}.mp4'
subprocess.call(cmd, shell=True)
