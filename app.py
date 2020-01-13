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


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=90)
