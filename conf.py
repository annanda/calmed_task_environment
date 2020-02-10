from decouple import config

one_second = 1000
one_minute = 60 * one_second
temp_time = 60 * one_minute
TIME_ON_PAGE_TASK = config('TIME_ON_PAGE_TASK', default=temp_time)
TIME_ON_PAGE_CALMING = config('TIME_ON_PAGE_CALMING', default=temp_time)
TIME_ON_PAGE_TO_READ = config('TIME_ON_PAGE_TO_READ', default=temp_time)
TIME_ON_PAGE_MOOD = config('TIME_ON_PAGE_MOOD', default=temp_time)
INDEX_BG_IMAGE = config('INDEX_BG_IMAGE', default='static/images/background_image.png')
