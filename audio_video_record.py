import subprocess
import re
from datetime import datetime

time_video_seconds = 10


def start_record(device_index):
    now = datetime.now()
    date_time = now.strftime("%d-%m-%Y__%H-%M-%S")
    # cmd = f'ffmpeg -f avfoundation -r 30 -s 1280x720 -pix_fmt yuyv422 -i "0:{device_index}" -t {time_video_seconds} -y -c:v libx264 -c:a ac3 data/av_{date_time}.mp4'
    cmd = f'ffmpeg -f avfoundation -r 30 -s 1280x720 -pix_fmt yuyv422 -i "1:{device_index}" -y -c:v libx264 -c:a ac3 data/av_{date_time}.mp4'
    subprocess.call(cmd, shell=True)
# TODO create a function to get the video device as well

def get_audio_device():
    cmd_devices = 'ffmpeg -f avfoundation -list_devices true -i "" &> devices.txt'
    subprocess.call(cmd_devices, shell=True)
    with open('devices.txt', 'r') as file:
        rows = file.read()
        x = re.search(".{3}( Built-in Microphone)", rows)
        string_result = x.group()
        device_index = int(string_result[1:2])
    return device_index


# def call_record():
#     device_index = get_audio_device()
#     start_record(device_index)


if __name__ == '__main__':
    try:
        device_index = get_audio_device()
        start_record(device_index)
    except KeyboardInterrupt:
        pass
