from decouple import config

one_second = 1000
one_minute = 60 * one_second
temp_time = 60 * one_minute
temp_time = one_second * 1000
five_minutes = one_minute * 5
three_seconds = one_second * 3
TIME_ON_PAGE_TASK = config('TIME_ON_PAGE_TASK', default=temp_time)
TIME_ON_PAGE_CALMING = config('TIME_ON_PAGE_CALMING', default=temp_time)
TIME_ON_PAGE_TO_READ = config('TIME_ON_PAGE_TO_READ', default=temp_time)
TIME_ON_PAGE_MOOD = config('TIME_ON_PAGE_MOOD', default=temp_time)
INDEX_BG_IMAGE = config('INDEX_BG_IMAGE', default='static/images/background_image.png')
CALMING_VIDEO_1 = config('CALMING_VIDEO_1',
                         default='https://www.youtube.com/embed/9A0S54yAgEg?controls=0&start=21&autoplay=1')
CALMING_VIDEO_2 = config('CALMING_VIDEO_2',
                         default='https://www.youtube.com/embed/uUIGKhG_Vq8?controls=0&amp;start=17&autoplay=1')
CALMING_VIDEO_3 = config('CALMING_VIDEO_3',
                         default='https://www.youtube.com/embed/V1-0JJJw_IQ?controls=0&amp;start=14c&autoplay=1')
CALMING_VIDEO_4 = config('CALMING_VIDEO_4',
                         default='https://www.youtube.com/embed/9_vEZTrmtyA?controls=0&amp;start=21&autoplay=1')

GREEN_ZONE_VIDEO = config('GREEN_ZONE_VIDEO',
                          default="static/videos/green_zone_edit_smaller.mp4")

BLUE_ZONE_VIDEO = config('BLUE_ZONE_VIDEO',
                         default='static/videos/blue_boring_smaller.mp4')
