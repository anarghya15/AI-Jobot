import os
from flask import Flask, render_template, request
from models.keras_first_go import KerasModel

app = Flask(__name__)


def train_model():
    global first_go_model

    print("Training the model")
    first_go_model = KerasModel()


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/first", methods=['POST', 'GET'])
def first():
    return render_template('first.html')


@app.route("/second", methods=['POST', 'GET'])
def second():
    return render_template('second.html')


@app.route("/third", methods=['POST', 'GET'])
def third():
    return render_template('third.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form.getlist('Job')
        train_model()
        processed_text = first_go_model.prediction(result[0])
        result = {'Job': processed_text}
        return render_template("result.html", result=result)


def clear_bash():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    clear_bash()
    print("---------------------------------")
    print("JOB PREDICTION APPLICATION")
    print("---------------------------------")
    clear_bash()

    print(("*Flask starting server..."
           "please wait until server has fully started"))
    app.run()