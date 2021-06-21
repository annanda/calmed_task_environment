from decouple import config

one_second = 1000
one_minute = 60 * one_second
five_minutes = one_minute * 5
three_seconds = one_second * 3
three_and_half = (3 * one_minute) + (30 * one_second)
temp_time = five_minutes * 1
two_minutes = 2 * one_minute
thirty_five_seconds = 35 * one_second
forty_seconds = 40 * one_second
TIME_ON_PAGE_TASK = config('TIME_ON_PAGE_TASK', default=three_and_half)
TIME_ON_GAME = config('TIME_ON_GAME', default=two_minutes)
TIME_ON_PAGE_CALMING = config('TIME_ON_PAGE_CALMING', default=two_minutes)
TIME_ON_PAGE_TO_READ = config('TIME_ON_PAGE_TO_READ', default=thirty_five_seconds)
TIME_ON_PAGE_MOOD = config('TIME_ON_PAGE_MOOD', default=forty_seconds)
INDEX_BG_IMAGE = config('INDEX_BG_IMAGE', default='static/images/start_image.jpeg')
CALMING_VIDEO_1 = config('CALMING_VIDEO_1',
                         default='https://www.youtube.com/embed/POP5BzZLOKk?controls=0&start=21&autoplay=1')
CALMING_VIDEO_2 = config('CALMING_VIDEO_2',
                         default='https://www.youtube.com/embed/qUJ6nGK7wrw?controls=0&amp;start=17&autoplay=1')
CALMING_VIDEO_3 = config('CALMING_VIDEO_3',
                         default='https://www.youtube.com/embed/y4BLQW1lCDE?controls=0&amp;start=14&autoplay=1')
CALMING_VIDEO_4 = config('CALMING_VIDEO_4',
                         default='https://www.youtube.com/embed/TlQ1EEbBlcI?controls=0&amp;start=21&autoplay=1')

GREEN_ZONE_VIDEO = config('GREEN_ZONE_VIDEO',
                          default="static/videos/green_zone_option_1_480p.mp4")

BLUE_ZONE_VIDEO = config('BLUE_ZONE_VIDEO',
                         default='static/videos/BORING_video_480p.mp4')
SESSION_NUMBER = config('SESSION_NUMBER', default=1)
