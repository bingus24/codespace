import flask

app = flask.Flask(__name__)

@app.route('/')
def main():
    return "hi"

app.run()