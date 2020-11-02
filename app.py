from flask import Flask, render_template, request, json
from models import db, TaskTime, MoodTime, AVRecordTime
from datetime import datetime
from conf import TIME_ON_PAGE_TASK, TIME_ON_PAGE_CALMING, TIME_ON_PAGE_TO_READ, TIME_ON_PAGE_MOOD, INDEX_BG_IMAGE, \
    CALMING_VIDEO_1, CALMING_VIDEO_2, CALMING_VIDEO_3, CALMING_VIDEO_4, GREEN_ZONE_VIDEO, BLUE_ZONE_VIDEO
import subprocess

app = Flask(__name__, template_folder="./templates", static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///saved-times.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
RECORD_AV_PROCESS = None
STARTING_TIME_AV_RECORD = None
ENDING_TIME_AV_RECORD = None


@app.route('/', methods=['GET'])
def index_page():
    info = {}
    timestamp = datetime.now()
    adding_db_task_timestamp('index_page', timestamp)
    return render_template('index.html', **info, image_bg=INDEX_BG_IMAGE)


def adding_db_task_timestamp(page, timestamp):
    db_new_entry = TaskTime(page=page, timestamp=timestamp)
    db.session.add(db_new_entry)
    db.session.commit()


@app.route('/first_task', methods=['GET'])
def first_task():
    timestamp = datetime.now()
    adding_db_task_timestamp('first_task', timestamp)
    time_on_page = json.dumps(TIME_ON_PAGE_TASK)
    return render_template('first_task.html', time_on_page=time_on_page, green_video=GREEN_ZONE_VIDEO)


@app.route('/second_task', methods=['GET'])
def second_task():
    timestamp = datetime.now()
    adding_db_task_timestamp('second_task', timestamp)
    time_on_page = json.dumps(TIME_ON_PAGE_TASK)
    return render_template('second_task.html', time_on_page=time_on_page)


@app.route('/third_task', methods=['GET'])
def third_task():
    timestamp = datetime.now()
    adding_db_task_timestamp('third_task', timestamp)
    time_on_page = json.dumps(TIME_ON_PAGE_TASK)
    return render_template('third_task.html', time_on_page=time_on_page)


@app.route('/forth_task', methods=['GET'])
def forth_task():
    timestamp = datetime.now()
    adding_db_task_timestamp('forth_task', timestamp)
    time_on_page = json.dumps(TIME_ON_PAGE_TASK)
    return render_template('forth_task.html', time_on_page=time_on_page, blue_video=BLUE_ZONE_VIDEO)


@app.route('/calming_content', methods=['GET'])
def calming_content():
    timestamp = datetime.now()
    adding_db_task_timestamp('calming_content_1', timestamp)
    time_on_page = json.dumps(TIME_ON_PAGE_CALMING)
    return render_template('calming_content.html', time_on_page=time_on_page, calming_video=CALMING_VIDEO_1)


@app.route('/calming_content_2', methods=['GET'])
def calming_content_2():
    timestamp = datetime.now()
    adding_db_task_timestamp('calming_content_2', timestamp)
    time_on_page = json.dumps(TIME_ON_PAGE_CALMING)
    return render_template('calming_content_2.html', time_on_page=time_on_page, calming_video=CALMING_VIDEO_2)


@app.route('/calming_content_3', methods=['GET'])
def calming_content_3():
    timestamp = datetime.now()
    adding_db_task_timestamp('calming_content_3', timestamp)
    time_on_page = json.dumps(TIME_ON_PAGE_CALMING)
    return render_template('calming_content_3.html', time_on_page=time_on_page, calming_video=CALMING_VIDEO_3)


@app.route('/calming_content_4', methods=['GET'])
def calming_content_4():
    timestamp = datetime.now()
    adding_db_task_timestamp('calming_content_4', timestamp)
    time_on_page = json.dumps(TIME_ON_PAGE_CALMING)
    return render_template('calming_content_4.html', time_on_page=time_on_page, calming_video=CALMING_VIDEO_4)


@app.route('/ending', methods=['GET'])
def ending():
    # this is the timestamp the video record will end
    timestamp = datetime.now()
    adding_db_task_timestamp('ending_page', timestamp)
    # global RECORD_AV_PROCESS
    # RECORD_AV_PROCESS.communicate(b'q')
    global ENDING_TIME_AV_RECORD
    ENDING_TIME_AV_RECORD = timestamp
    if STARTING_TIME_AV_RECORD is not None:
        store_av_record_time(STARTING_TIME_AV_RECORD, ENDING_TIME_AV_RECORD)
    # RECORD_AV_PROCESS.send_signal(signal.SIGINT)
    return render_template('ending.html')


@app.route('/game', methods=['GET'])
def game():
    timestamp = datetime.now()
    adding_db_task_timestamp('game_page', timestamp)
    time_on_page = json.dumps(TIME_ON_PAGE_TASK)
    return render_template('game.html', time_on_page=time_on_page)


@app.route('/end_game', methods=['GET'])
def end_game():
    timestamp = datetime.now()
    adding_db_task_timestamp('ending_game_page', timestamp)
    time_on_page = json.dumps(TIME_ON_PAGE_TO_READ)
    return render_template('end_game.html', time_on_page=time_on_page)


@app.route('/schedule', methods=['GET'])
def schedule():
    # this is the timestamp the record video will start
    timestamp = datetime.now()
    adding_db_task_timestamp('schedule_page_initial', timestamp)
    time_on_page = json.dumps(TIME_ON_PAGE_TO_READ)
    # global RECORD_AV_PROCESS
    # RECORD_AV_PROCESS = subprocess.Popen(['python', 'audio_video_record.py'], stdin=subprocess.PIPE)
    global STARTING_TIME_AV_RECORD
    STARTING_TIME_AV_RECORD = timestamp
    return render_template('schedule.html', time_on_page=time_on_page)


@app.route('/schedule_after_1', methods=['GET'])
def schedule_after_1():
    timestamp = datetime.now()
    adding_db_task_timestamp('schedule_page_after_task_1', timestamp)
    time_on_page = json.dumps(TIME_ON_PAGE_TO_READ)
    return render_template('schedule_after_1.html', time_on_page=time_on_page)


@app.route('/schedule_after_2', methods=['GET'])
def schedule_after_2():
    timestamp = datetime.now()
    adding_db_task_timestamp('schedule_page_after_task_2', timestamp)
    time_on_page = json.dumps(TIME_ON_PAGE_TO_READ)
    return render_template('schedule_after_2.html', time_on_page=time_on_page)


@app.route('/schedule_after_3', methods=['GET'])
def schedule_after_3():
    timestamp = datetime.now()
    adding_db_task_timestamp('schedule_page_after_task_3', timestamp)
    time_on_page = json.dumps(TIME_ON_PAGE_TO_READ)
    return render_template('schedule_after_3.html', time_on_page=time_on_page)


@app.route('/schedule_ending', methods=['GET'])
def schedule_ending():
    timestamp = datetime.now()
    adding_db_task_timestamp('schedule_page_ending', timestamp)
    time_on_page = json.dumps(TIME_ON_PAGE_TO_READ)
    return render_template('schedule_ending.html', time_on_page=time_on_page)


@app.route('/mood', methods=['GET'])
def mood():
    time_on_page = json.dumps(TIME_ON_PAGE_MOOD)
    return render_template('mood.html', time_on_page=time_on_page)


@app.route('/store_mood', methods=['POST'])
def store_mood():
    # print(request.is_json)
    req_data = request.get_json()
    # print(req_data)
    mood = req_data['mood']
    # print(mood)
    task = req_data['task']
    timestamp = datetime.now()
    # test first to store in DB with given values.
    # mood = 'happy'
    # task = 'first_task'
    # timestamp = datetime.now()

    db_entry = MoodTime(mood=mood, task=task, timestamp=timestamp)
    db.session.add(db_entry)
    db.session.commit()
    return 'mood saved on DB'
    # return 'testing POST'


def store_av_record_time(start_time, end_time):
    db_entry = AVRecordTime(timestamp_start=start_time, timestamp_end=end_time)
    db.session.add(db_entry)
    db.session.commit()


if __name__ == '__main__':
    #  comment the lines below
    # app.app_context().push()
    # db.drop_all()
    # db.create_all()
    app.run(debug=True, host='0.0.0.0', port=90)
