from flask import Flask, render_template

app = Flask(__name__, template_folder="./templates")


def hello_world():
    return 'Hello World!'


@app.route('/', methods=['GET'])
def index_page():
    info = {}
    return render_template('index.html', **info)


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


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=90)
