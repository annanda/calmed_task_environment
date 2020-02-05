from decouple import config

temp_time = 15000
TIME_ON_PAGE_TASK = config('TIME_ON_PAGE_TASK', default=temp_time)
TIME_ON_PAGE_CALMING = config('TIME_ON_PAGE_CALMING', default=temp_time)
TIME_ON_PAGE_TO_READ = config('TIME_ON_PAGE_TO_READ', default=temp_time)
TIME_ON_PAGE_MOOD = config('TIME_ON_PAGE_MOOD', default=temp_time)

