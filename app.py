from flask import Flask, render_template
from models import db, TaskTime
from datetime import datetime

app = Flask(__name__, template_folder="./templates", static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///saved-times.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route('/', methods=['GET'])
def index_page():
    info = {}
    timestamp = datetime.now()
    adding_db('index_page', timestamp)
    return render_template('index.html', **info)


def adding_db(task, timestamp):
    db_new_entry = TaskTime(task=task, timestamp=timestamp)
    db.session.add(db_new_entry)
    db.session.commit()


@app.route('/first_task', methods=['GET'])
def first_task():
    timestamp = datetime.now()
    adding_db('first_task', timestamp)
    return render_template('first_task.html')


@app.route('/calming_content', methods=['GET'])
def calming_content():
    timestamp = datetime.now()
    adding_db('calming_content', timestamp)
    return render_template('calming_content.html')


@app.route('/calming_content_2', methods=['GET'])
def calming_content_2():
    return render_template('calming_content_2.html')


@app.route('/calming_content_3', methods=['GET'])
def calming_content_3():
    return render_template('calming_content_3.html')


@app.route('/calming_content_4', methods=['GET'])
def calming_content_4():
    return render_template('calming_content_4.html')


@app.route('/second_task', methods=['GET'])
def second_task():
    return render_template('second_task.html')


@app.route('/third_task', methods=['GET'])
def third_task():
    # return "this is the third task"
    return render_template('third_task.html')


@app.route('/forth_task', methods=['GET'])
def forth_task():
    # return "this is the forth task"
    return render_template('forth_task.html')


@app.route('/ending', methods=['GET'])
def ending():
    return render_template('ending.html')


@app.route('/store_timestamp', methods=['POST'])
def store_timestamp():
    pass


@app.route('/game', methods=['GET'])
def game():
    return render_template('game.html')


@app.route('/end_game', methods=['GET'])
def end_game():
    return render_template('end_game.html')


@app.route('/schedule', methods=['GET'])
def schedule():
    return render_template('schedule.html')


@app.route('/schedule_after_1', methods=['GET'])
def schedule_after_1():
    return render_template('schedule_after_1.html')


if __name__ == '__main__':
    # TODO comment the lines below
    # app.app_context().push()
    # db.drop_all()
    # db.create_all()
    app.run(debug=True, host='0.0.0.0', port=90)
