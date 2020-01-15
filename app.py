from flask import Flask, render_template
from models import db, User

app = Flask(__name__, template_folder="./templates", static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///saved-times.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route('/', methods=['GET'])
def index_page():
    info = {}
    adding_db()
    return render_template('index.html', **info)


def adding_db():
    admin = User(username='admin6', email='admin6@example.com')
    guest = User(username='guest6', email='guest6@example.com')
    db.session.add(admin)
    db.session.add(guest)
    db.session.commit()


@app.route('/first_task', methods=['GET'])
def first_task():
    return render_template('first_task.html')


@app.route('/calming_content', methods=['GET'])
def calming_content():
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


if __name__ == '__main__':
    # app.app_context().push()
    # db.drop_all()
    # db.create_all()
    app.run(debug=True, host='0.0.0.0', port=90)
